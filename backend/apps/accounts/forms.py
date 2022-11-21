from operator import attrgetter
from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from backend.apps.accounts.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        label = "Логин",
        widget = forms.TextInput(
            attrs={"class":"form-control"}
        )
    )
    password = forms.CharField(
        label = "Пароль",
        widget = forms.PasswordInput(
            attrs={"class":"form-control"}
        )
    )

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label = "Пароль",
        widget = forms.PasswordInput(
            attrs={"class":"form-control"}
        )
    )

    password2 = forms.CharField(
        label = "Повторите пароль",
        widget = forms.PasswordInput(
            attrs = {"class":"form-control"}
        )
    )

    class Meta:
        model = User
        fields = [
            "username",
            "phone",
        ]
        form_control = {"class":"form-control"}
        widgets = {
            "username":forms.TextInput(attrs=form_control),
            "phone":forms.TextInput(attrs=form_control),
        }