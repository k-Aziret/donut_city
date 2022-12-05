from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
from .models import SubCategory
from django.views.generic import TemplateView, ListView, DetailView
from .models import Product, Category


def index(request):
    return HttpResponse("<h1> Главная страница </h1>")

def get_subcategories(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
    category_id=int(id)).values('id', 'name'))
    return  HttpResponse(json.dumps(result), content_type="application/json")



class IndexPage(TemplateView):
	template_name = "index.html" 

class ProductListView(ListView):
    template_name = "product_list.html" 
    model = Product
    paginate_by = 3

    def get_queryset(self, **kwargs):
        category = self.kwargs.get("category_slug")
        if category: 
            return Product.objects.filter(category__slug=category)
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"]= Category.objects.all()
        return context
        
# class ProductDetailCart(View):

# 	def get(self, request):
        
		
# 		return render(self.request, "product_details.html")

class ProductDetailView(DetailView):
    
    model = Product
    template_name = "product_details.html"
    context_object_name = "product"

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

		# product = Product.objects.get(id=pk) 

# def get_product_detail(request, pk):
#     # try:
#     #     product = Product.objects.get(id=pk)
#     # except:
#     #     pass
#     # context ={
#     #     "product":product
#     # }
#     # return render(request, 'product_details.html', context)
