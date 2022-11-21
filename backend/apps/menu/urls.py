from django.urls import path

from backend.apps.menu.views import index
urlpatterns = [
    path("", index,name="index"),
]