Financial management system using DRF
                                                     

# CURRENT FEATURES:

You can Add and Delete expense categories

Record your completed transactions

You can add your own sources of incomes

Viewing the current balance

View all transactions

Swagger

Celery

Sending monthly transaction statistics in PDF format



# Requirements:

To start the project, you need to install

Python3.8+

PostgreSQL database

RabbitMQ

Celery

Postman

Django

Django-Rest-Framework

Flower

Django-environ

Django-pytest

# Installation
Clone the repo with

git clone https://github.com/NikitaZhukovsky/financial-management.git

Create .env file inside the root directory and include the following variables

SECRET_KEY=YOUR_SECRET_KEY

DATABASE_NAME=YOUR_DATABASE

DATABASE_USER=YOUR_DATABASE_USER

DATABASE_PASSWORD=YOUR_PASSWORD

DATABASE_HOST=YOUR_HOST

DATABASE_PORT=YOUR_PORT


# Email config

EMAIL_HOST_USER=your_email@gmail.com

EMAIL_HOST_PASSWORD=YOUR_PASSWORD



# Other

DEBUG=True
CELERY_HOST=YOUR_HOST

CELERY_PORT=YOUR_PORT


References

Show your support by ⭐️ this project!
