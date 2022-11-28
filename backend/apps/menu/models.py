from django.db import models

# Create your models here.

from backend.apps.accounts.models import User


class Category(models.Model):
    name = models.CharField("Название", max_length=100,unique=True)
    slug = models.SlugField("Slug", max_length=120, unique=True)
    order_number = models.SmallIntegerField("Номер заказа", blank=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["-order_number"]

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories"
    )
    name = models.CharField("Название", max_length=70, unique=True)
    slug = models.SlugField("Слаг", max_length=80, unique=True)

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        ordering = ['category', 'name']

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    image = models.ImageField("Фото", upload_to = "products/img")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, related_name="products")



    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
    
    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    reveiw = models.TextField("Отзыв")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created']

    def __str__(self):
        return f'{self.id}'

