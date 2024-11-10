from django.db import models


class RequiredChat(models.Model):
    CHAT_TYPE_CHOICES = [
        ("group", "Группа"),
        ("channel", "Канал"),
    ]

    chat_id = models.CharField(
        max_length=255, unique=True, verbose_name="ID чата"
    )
    title = models.CharField(max_length=255, verbose_name="Название чата")
    username = models.CharField(
        max_length=255, unique=True, verbose_name="Никнейм чата"
    )
    type = models.CharField(
        max_length=7, verbose_name="Тип чата", choices=CHAT_TYPE_CHOICES
    )

    class Meta:
        verbose_name = "Требуемый чат"
        verbose_name_plural = "Требуемые чаты"

    def __str__(self):
        return f"{self.title} ({self.type})"


class FAQ(models.Model):
    question = models.CharField(max_length=255, verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"

    def __str__(self):
        return self.question
