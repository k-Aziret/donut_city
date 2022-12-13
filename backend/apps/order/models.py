from django.db import models

# Create your models here.
from backend.apps.menu.models import Product
from backend.apps.accounts.models import User


class Order(models.Model):
	STATUS_NEW = "new"
	STATUS_CONFIRMED = "confirmed"
	STATUS_REJECTED = "rejected"
	ORDER_STATUSES = (
		(STATUS_NEW, "Новый "),
		(STATUS_CONFIRMED, "Подвержден"),
		(STATUS_REJECTED, "Отменен")
	)
	name = models.CharField(max_length=255)
	address = models.TextField()
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	products = models.ManyToManyField(Product, through='OrderItem')


	user = models.ForeignKey(User, on_delete=models.CASCADE)
	phone = models.CharField("Номер телефона", max_length=14)
	notice = models.CharField("Комментарий", max_length=255)
	status = models.CharField("Статус", max_length=9, choices=ORDER_STATUSES, default=STATUS_NEW)

	class Meta:
		verbose_name = "Заказ"
		verbose_name_plural = "Заказы"
	def __str__(self):
		return f"Заказы-{self.id}"


class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name="Продукт")
	order  = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
	price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField("Количество", default=1)

	def __str__(self):
		return f"{self.id}"
