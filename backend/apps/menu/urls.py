from django.urls import path

from backend.apps.menu.views import index
from .views import *
from backend.apps.menu import views
urlpatterns = [
    # path("", index,name="index"),
    # path('getSubcategory/', get_subcategories, name="get_subcategory")
    path("", views.IndexPage.as_view(), name="index"),
    path("product/list/", views.ProductListView.as_view(), name="product_list"),
    path("product/list/<slug:category_slug>/", ProductListView.as_view(), name="category_products"),
    path("product/list/<int:product_range>/", ProductListView.as_view(), name="price_product"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("search/", ProductSearchListView.as_view(), name="product_search")
]