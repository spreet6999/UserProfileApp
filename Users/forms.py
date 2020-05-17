from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Document, Profile
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model


class UserCreateForm(forms.ModelForm):
    email = forms.EmailField()
    confirm_email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','confirm_email','username','password']

    def clean_confirm_email(self):
        email = self.cleaned_data.get("email")
        confirm_email = self.cleaned_data.get("confirm_email")
        if email != confirm_email:
            raise forms.ValidationError("Emails do not match")

        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Email already used")
        return email

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return password

class ProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(required=True)
    information = forms.Textarea()
    class Meta:
        model = Profile
        fields = ['profile_image', 'information']


class DocumentForm(forms.ModelForm):
    document = forms.FileField()
    class Meta:
        model = Document
        fields = ('title', 'document',)