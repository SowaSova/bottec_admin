from django.db import models

from catalog.models import Product
from users.models import TelegramUser


class Order(models.Model):
    STATUS_CHOICES = [
        ("new", "Новый"),
        ("in_progress", "В процессе"),
        ("completed", "Завершен"),
        ("canceled", "Отменен"),
    ]
    user = models.ForeignKey(
        TelegramUser, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    delivery_address = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ No{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"

    def __str__(self):
        return f"Товар No{self.id}"
