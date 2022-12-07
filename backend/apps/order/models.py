# from django.db import models

# # Create your models here.
# from backend.apps.menu.models import Product
# from backend.apps.accounts.models import User

# class Order(models.Model):
# 	STATUS_NEW = "new"
# 	STATUS_CONFIRMED = "confirmed"
# 	STATUS_REJECTED = "rejected"
# 	ORDER_STATUSES = (
# 		(STATUS_NEW, "Новый "),
# 		(STATUS_CONFIRMED, "Подвержден"),
# 		(STATUS_REJECTED, "Отменен")
		
# 	)

# 	user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	phone = models.CharField("Номер телефона", max_length=14)
# 	notice = models.CharField("Комментарий", max_length=255)
# 	status = models.CharField("Статус", max_length=9, choices=ORDER_STATUSES, default=STATUS_NEW)


# class Order(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.TextField()
#     email = models.EmailField()
#     phone = models.CharField(max_length=20)
#     products = models.ManyToManyField(Product, through='OrderItem')

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.PositiveIntegerField()
