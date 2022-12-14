# Generated by Django 4.1.3 on 2022-12-14 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0003_filterprice'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('phone', models.CharField(max_length=14, verbose_name='Номер телефона')),
                ('notice', models.CharField(max_length=255, verbose_name='Комментарий')),
                ('status', models.CharField(choices=[('new', 'Новый '), ('confirmed', 'Подвержден'), ('rejected', 'Отменен')], default='new', max_length=9, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='menu.product', verbose_name='Продукт')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='cart.OrderItem', to='menu.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
