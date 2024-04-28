from django.urls import path, include
from users.views import ActivateUser, TestLoginView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('activate/<str:uid>/<str:token>/', ActivateUser.as_view({'get': 'activation'})),
    path('test-login/', TestLoginView.as_view(), name='test-login')
]