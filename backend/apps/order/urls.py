from django.urls import path
from .views import order_create, order_success

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('success/', order_success, name='order_success'),
]

# orders/order_create.html