from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.conf import settings


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields