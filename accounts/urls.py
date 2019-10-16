from django.contrib.auth.views import LoginView
from accounts.views import RegistrationView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path("login/", LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path("register/", RegistrationView.as_view(), name='register')
]
