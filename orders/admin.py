from django.contrib import admin
from .models import Order, OrderItem
from import_export.admin import ExportActionMixin


@admin.register(Order)
class OrderAdmin(ExportActionMixin, admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItemAdmin(ExportActionMixin, admin.ModelAdmin):
    pass
