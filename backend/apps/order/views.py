# from django.views.generic import CreateView
# from backend.apps.order.forms import OrderForm
# from backend.apps.order.models import Order, Order

# class Order

# from django.shortcuts import render
# from django.views.generic import CreateView
# from backend.apps.order.forms import OrderForm
# from backend.apps.order.models import Order, OrderItem


# class OrderCreateView(CreateView):
# 	form_class = OrderForm
# 	template_name = "order_create.html"


# from django.shortcuts import render, redirect
# from django.urls import reverse
# from .models import Order, OrderItem
# from .forms import OrderForm

# def order_create(request):
#     cart = request.session.get('cart')
#     if not cart:
#         return redirect('cart:cart_detail')

#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             order = form.save()
#             for item in cart.items.all():
#                 OrderItem.objects.create(
#                     order=order,
#                     product=item.product,
#                     name=item.product.name,
#                     price=item.product.price,
#                     quantity=item.quantity
#                 )
#             # очищаем корзину
#             cart.clear()
#             # перенаправляем на страницу успешного оформления заказа
#             return redirect(reverse('orders:order_success'))
#     else:
#         form = OrderForm()

#     return render(request, "{% url 'purchase' %}", {'form': form})

# def order_success(request):
#     return render(request, 'order_success.html')
