from django.contrib.auth import login as auth_login
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import SignUpForm


# Create your views here.

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
