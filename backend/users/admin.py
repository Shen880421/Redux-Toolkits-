from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "account",
        "username",
        "role",
        "created_at",
    )  # 在列表中顯示這些欄位
    list_filter = ("role", "gender")  # 添加篩選器
    search_fields = ("account", "username", "email")  # 添加搜尋欄位
    readonly_fields = ("id", "created_at", "updated_at")  # ID 和時間戳設為唯讀
