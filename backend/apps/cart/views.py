from django.shortcuts import render, redirect

from django.views import View
# Create your views here.

from .form import CartAddForm
from .cart import Cart
from backend.apps.menu.models import Product

class AddCartView(View):

	form_class = CartAddForm

	def get(self, request, pk):
		product_id = self.kwargs.get('pk')
		cart = Cart(request)
		product = Product.objects.get(id=pk) 
		cart.add(product=product)
		return redirect("index")

class CartDetailView(View):

	def get(self, request):
		cart = Cart(request)
		context = {"cart":cart}
		return render(self.request, "cart.html", context)
