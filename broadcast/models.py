from django.db import models


class BroadcastMessage(models.Model):
    message_text = models.TextField("Текст сообщения")
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_time = models.DateTimeField("Время отправки", null=True, blank=True)
    is_sent = models.BooleanField("Отправлено", default=False)

    class Meta:
        verbose_name = "Сообщение для рассылки"
        verbose_name_plural = "Сообщения для рассылки"

    def __str__(self):
        return f"Рассылка от {self.created_at}"
