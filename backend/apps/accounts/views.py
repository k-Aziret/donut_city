
from django.shortcuts import render, redirect
from django.views.generic import (
    FormView, 
    CreateView,
    TemplateView,
    DetailView
    )
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import LoginForm, UserRegisterForm
from backend.apps.accounts.models import User
from django.contrib.auth.mixins import LoginRequiredMixin # Нужен для проверки



class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm


    def form_valid(self, form):
        data = form.cleaned_data
        email = data['email']
        password = data['password']     
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('index')
            else:
                return HttpResponse("Ваш аккаунт неактивен")
        return HttpResponse("Такого юзера не существует")
    



class UserRegisterView(CreateView):
    template_name = "register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy('register_done')


#generic - готовый классы с готовым решением,
# для стандартных задач
class RegisterDoneView(TemplateView):
    template_name = "base.html"



def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.changed_data['password'])
            new_user.save()
            login(request, new_user)
            return render(request, 'base.html', {'new_user':new_user})
    else:
        user_form = UserRegisterForm()
    return render(request, 'register.html', {'user_form':user_form })

class UserProfileView(LoginRequiredMixin, DetailView): # LoginRequiredMixin - проверяет залогинен ли юзер
    template_name = "user_profile.html"
    model = User
    queryset = User.objects.all()
