from django.contrib import admin
from .models import Order


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer_id",
        "shipping_status",
        "payment_status",
        "receiver_name",
        "receiver_phone",
        "receiver_address",
        "total_amount",
        "created_at",
    )  # 在列表中顯示這些欄位
    list_filter = ("shipping_status", "payment_status")  # 添加篩選器
    search_fields = (
        "customer_id",
        "id",
        "receiver_name",
        "receiver_phone",
        "receiver_address",
    )  # 添加搜尋欄位
    readonly_fields = ("id", "created_at", "updated_at")  # ID 和時間戳設為唯讀
