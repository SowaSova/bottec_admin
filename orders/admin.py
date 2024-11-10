from django.contrib import admin
from import_export.admin import ExportActionMixin

from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(ExportActionMixin, admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItemAdmin(ExportActionMixin, admin.ModelAdmin):
    pass
