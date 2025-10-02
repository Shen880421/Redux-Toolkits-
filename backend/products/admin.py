from django.contrib import admin

from .models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "price",
        "stock",
        "attribute",
        "expiration_days",
        "created_at",
    )  # 在列表中顯示這些欄位
    list_filter = ("attribute",)  # 添加篩選器
    search_fields = ("name", "description")  # 添加搜尋欄位
    readonly_fields = ("id", "created_at", "updated_at")  # ID 和時間戳設為唯讀
