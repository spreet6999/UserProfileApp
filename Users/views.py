from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import get_user_model

from . import forms
from .forms import UserCreateForm, ProfileForm, DocumentForm

from django.contrib.auth.models import User
from .models import Profile, Document

from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "Users/profile.html", {})


def SignUp(request):
            form = UserCreateForm(request.POST or None)
            profile_form = ProfileForm(request.POST, request.FILES)

            if form.is_valid() and request.method == 'POST':
                username = form.cleaned_data.get("username")
                email = form.cleaned_data.get("email")
                password = form.cleaned_data.get("password")

                new_user = User.objects.create_user(
                    username, email, password,

                )

                upload_pic(request, profile_form, username=username)
                login(request, new_user)
                return redirect('Users:home')
            else :
                form = UserCreateForm()
                profile_form = ProfileForm()
            context = {
                "form": form,
                "profile_form": profile_form
            }
            return render(request, "Users/signup.html", context)

def upload_pic(request, form, username):
        if request.method == 'POST':
            if form.is_valid():
                User = get_user_model()
                user = User.objects.get(username=username)
                profile_image = form.cleaned_data.get('profile_image')
                profile_info = form.cleaned_data.get("information")
                new_user_profile = Profile.objects.create(user=user, profile_image=profile_image, information=profile_info)
                new_user_profile.save()


@login_required
def document_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, )
        if form.is_valid():
            User = get_user_model()
            user = User.objects.get(username=request.user.username)
            doc_title = form.cleaned_data.get("title")
            doc_file = form.cleaned_data.get('document')
            new_doc = Document.objects.create(user=user, title=doc_title, document=doc_file)

            new_doc.save()
            return redirect('Users:home')
    else:
        form = DocumentForm()
    return render(request, 'Users/document_upload.html', {
        'form': form
    })
