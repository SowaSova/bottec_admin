from django.db import models


class BroadcastMessage(models.Model):
    message_text = models.TextField(verbose_name="Текст сообщения")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    scheduled_time = models.DateTimeField(
        null=True, blank=True, verbose_name="Время отправки"
    )
    is_sent = models.BooleanField(default=False, verbose_name="Отправлено")

    class Meta:
        verbose_name = "Сообщение для рассылки"
        verbose_name_plural = "Сообщения для рассылки"

    def __str__(self):
        return f"Рассылка от {self.created_at}"
