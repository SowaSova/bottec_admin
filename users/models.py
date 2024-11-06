from django.db import models


class TelegramUser(models.Model):
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    telegram_id = models.CharField(max_length=20, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "TG-Пользователь"
        verbose_name_plural = "TG-Пользователи"

    def __str__(self):
        return self.username or self.telegram_id
