# Generated by Django 5.1.3 on 2024-11-07 15:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0002_alter_cart_options_alter_cartitem_options"),
        ("catalog", "0003_alter_category_parent_alter_category_slug_and_more"),
        ("users", "0002_remove_telegramuser_is_subscribed_channel_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cart",
                to="users.telegramuser",
                verbose_name="Пользователь",
            ),
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="cart",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="cart.cart",
                verbose_name="Корзина",
            ),
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cart_items",
                to="catalog.product",
                verbose_name="Товар",
            ),
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="quantity",
            field=models.PositiveIntegerField(default=1, verbose_name="Количество"),
        ),
    ]