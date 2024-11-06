from django.contrib import admin
from .models import RequiredChat


@admin.register(RequiredChat)
class ChatAdmin(admin.ModelAdmin):
    pass
