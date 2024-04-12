import io
from datetime import timedelta
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils import timezone
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from celery import shared_task

from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from management.models import Transaction


def generate_pdf(transactions):
    pdf_buffer = io.BytesIO()

    doc = SimpleDocTemplate(pdf_buffer, pagesize=A4)

    styles = getSampleStyleSheet()

    elements = []

    categories = [transaction.category for transaction in transactions]
    amounts = [transaction.amount for transaction in transactions]
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.axis('equal')
    plt.title('Expenses by Category')
    plt.tight_layout()

    with PdfPages(pdf_buffer) as pdf_pages:
        plt.savefig(pdf_pages, format='pdf')
        plt.close()

    table_data = [['Transaction ID', 'Category', 'Amount', 'Payment Method']]

    for transaction in transactions:
        table_data.append([
            str(transaction.id),
            transaction.category,
            str(transaction.amount),
            transaction.payment_method
        ])

    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
        ('TOPPADDING', (0, -1), (-1, -1), 12),
    ]))

    elements.append(Paragraph('Transactions:', styles['Heading1']))
    elements.append(table)

    doc.build(elements)
    pdf_buffer.seek(0)

    return pdf_buffer.getvalue()


@shared_task()
def check_orders_and_send_mails():
    start_date = timezone.now() - timedelta(days=30)
    transactions = Transaction.objects.filter(date__gte=start_date)

    pdf = generate_pdf(transactions)

    message = 'Here is the financial report for the last month.'

    email = EmailMessage(
        'Financial Report',
        message,
        from_email=settings.EMAIL_HOST_USER,
        to=[transaction.user.email for transaction in transactions],
    )
    email.attach('report.pdf', pdf, 'application/pdf')
    email.send()
