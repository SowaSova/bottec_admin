from django.db import models
from django.core.validators import MinValueValidator
from storages.backends.s3boto3 import S3Boto3Storage
from utils.image_path import product_image_upload_to


class Category(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, verbose_name="URL")
    parent = models.ForeignKey(
        "self",
        related_name="children",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Родительская категория",
    )

    class Meta:
        unique_together = ("parent", "slug")
        ordering = ("title",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL")
    image = models.ImageField(
        upload_to=product_image_upload_to,
        blank=True,
        verbose_name="Изображение",
        storage=S3Boto3Storage(),
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Цена",
    )

    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.CASCADE,
        verbose_name="Категория",
    )

    is_available = models.BooleanField(default=False, verbose_name="Доступен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        ordering = ("title",)
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title
