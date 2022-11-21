from django.urls import path

from backend.apps.accounts.views import UserRegisterView, LoginView



urlpatterns = [
    path("login/", LoginView.as_view(), name="sign_in"),
    path("registration/", UserRegisterView.as_view(), name="register"),
    # path("form_html/", UserRegisterView.as_view(), name="log_in"),
    # path("register/", UserRegisterView.as_view(), name="form.html")
]