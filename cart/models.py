from django.db import models
from users.models import TelegramUser
from catalog.models import Product


class Cart(models.Model):
    user = models.OneToOneField(
        TelegramUser,
        on_delete=models.CASCADE,
        related_name="cart",
        verbose_name="Пользователь",
    )

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return f"Корзина пользователя {self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="items", verbose_name="Корзина"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="cart_items",
        verbose_name="Товар",
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")

    class Meta:
        unique_together = ("cart", "product")
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"

    def __str__(self):
        return (
            f"{self.product} в корзине {self.cart.user} (количество: {self.quantity})"
        )
