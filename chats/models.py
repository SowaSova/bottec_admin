from django.db import models


class RequiredChat(models.Model):
    CHAT_TYPE_CHOICES = [
        ("group", "Группа"),
        ("channel", "Канал"),
    ]

    chat_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    chat_type = models.CharField(max_length=7, choices=CHAT_TYPE_CHOICES)

    class Meta:
        verbose_name = "Требуемый чат"
        verbose_name_plural = "Требуемые чаты"

    def __str__(self):
        return f"{self.name} ({self.chat_type})"
