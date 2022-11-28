from operator import attrgetter
from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from backend.apps.accounts.models import User

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Электронная почта",
        widget=forms.EmailInput(attrs={"class":"form-control"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "type":"password",
                "autocomplete":"off",
                "placeholder":"Пароль",
            }
            )
    )

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class":"form-control"})
        )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class":"form-control"})
    )
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'phone',
        ]
        form_control = {"class":"form-control"}
        widgets = {
            "email":forms.EmailInput(attrs=form_control),
            "first_name":forms.TextInput(attrs=form_control),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "phone":forms.TextInput(attrs={"class":"form-control"}),
        
        }