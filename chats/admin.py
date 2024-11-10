from django.contrib import admin

from .models import FAQ, RequiredChat


@admin.register(RequiredChat)
class ChatAdmin(admin.ModelAdmin):
    pass


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    pass
