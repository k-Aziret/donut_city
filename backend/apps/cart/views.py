from django.shortcuts import render, redirect

from django.views import View
from django.http import Http404, JsonResponse
# Create your views here.

from .form import CartAddForm
from .cart import Cart
from backend.apps.menu.models import Product
from backend.apps.cart.form import OrderForm
from django.views.generic import CreateView

class AddCartView(View):

	form_class = CartAddForm

	def get(self, request, pk):
		product_id = self.kwargs.get('pk')
		cart = Cart(request)
		product = Product.objects.get(id=pk) 
		cart.add(product=product)
		return redirect("cart_detail")
class CartDetailView(View):

	def get(self, request):
		form = OrderForm(request)
		context = {"form":form}
		return render(self.request, "cart.html", context)


class RemoveCartView(View):
	
	def get(self, request, pk):
		cart = Cart(request)
		try:
			product=Product.objects.get(id=pk)
		except Product.DoesNotExist:
			raise Http404()
		cart.remove(product)
		return redirect('cart_detail')

class ClearCartView(View):

	def get(self, request):
		cart = Cart(request)
		cart.clear()
		return redirect('cart_detail')
	
class CartDesign(View):

	def get(self, request):
		form = OrderForm(request)
		context = {"form":form}
		return render(self.request, "contact.html", context)



class AddOrderView(View):

	form_class = CartAddForm

	def get(self, request, pk):
		product_id = self.kwargs.get('pk')
		cart = Cart(request)
		product = Product.objects.get(id=pk) 
		cart.add(product=product)
		return redirect("order")

class OrderCreateView(CreateView):
	form_class = OrderForm
	template_name = "contact.html"
