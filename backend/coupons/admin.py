from django.contrib import admin

from .models import Coupon


# Register your models here.
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "code",
        "discount_type",
        "discount_value",
        "min_order_amount",
        "usage_limit",
        "created_at",
        "is_active",
        "updated_at",
    )  # 在列表中顯示這些欄位
    list_filter = ("is_active",)  # 添加篩選器
    search_fields = ("code",)  # 添加搜尋欄位
    readonly_fields = ("id", "created_at", "updated_at")  # ID 和時間戳設為唯讀
