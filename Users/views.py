from django.shortcuts import render
# Create your views here.
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from . import forms
from .models import Profile, User

# Create your views here.


def home(request):
    return render(request, "Users/profile.html", {})

class ProfileDetail(DetailView):
    model = User
    template_name='Users/profile.html'

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "Users/signup.html"
