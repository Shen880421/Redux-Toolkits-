from django.contrib import admin

from .models import OrderItems


# Register your models here.
@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order_id",
        "product_id",
        "quantity",
        "unit_price",
        "subtotal",
        "created_at",
    )  # 在列表中顯示這些欄位
    list_filter = ("order_id", "product_id")  # 添加篩選器
    search_fields = ("order_id", "product_id")  # 添加搜尋欄位
    readonly_fields = ("id", "created_at", "updated_at")  # ID 和時間戳設為唯讀
