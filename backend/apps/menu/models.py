from django.db import models

# Create your models here.
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
    price = models.DecimalField("Цена", max_digits=6, decimal_places=2)
    image = models.ImageField("Фото", upload_to = "product_images/")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, related_name="products")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # is_available = models.

    class Meta:
        verbose_name = "Мен"
        verbose_name_plural = "Меню"
        ordering = ['-created']
    
    def __str__(self):
        return self.name
