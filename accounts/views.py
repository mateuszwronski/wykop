from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = '/posts/'
