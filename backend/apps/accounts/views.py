from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, FormView
from backend.apps.accounts.forms import UserRegisterForm
from django.urls import reverse_lazy
from backend.apps.accounts.forms import LoginForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

class LoginView(FormView):
	template_name = "login.html"
	form_class = LoginForm
	
	def form_valid(self, form):
		data = form.cleaned_data
		username = data["username"]
		password = data["password"]
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(self.request,user)
				return redirect("index")
			return HttpResponse("<h1>Your account is not active</h1>")
		return HttpResponse("<h1> Invalid user data </h1>")

class UserRegisterView(CreateView):
    template_name = "register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("index")

