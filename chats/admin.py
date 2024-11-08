from django.contrib import admin
from .models import RequiredChat, FAQ


@admin.register(RequiredChat)
class ChatAdmin(admin.ModelAdmin):
    pass


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    pass
