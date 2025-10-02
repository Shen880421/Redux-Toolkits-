import enum
from django.db import models
from orders.models import Order


# Create your models here.
class Shipment(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="訂單")
    carrier = models.CharField(
        max_length=20,
        choices=[
            ("BlackCat", "黑貓"),
            ("FamilyMart", "全家"),
            ("7-11", "7-11"),
            ("HiLife", "萊爾富"),
            ("ChunghwaPost", "中華郵政"),
            ("Other", "其他"),
        ],
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "待運送"),
            ("in_transit", "運送中"),
            ("delivered", "已送達"),
            ("returned", "已退回"),
            ("cancelled", "已取消"),
        ],
    )
    shipped_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "物流狀況"
        verbose_name_plural = "物流狀況"
        ordering = ["-created_at"]  # 依建立時間排序，最新的在前面

    def __str__(self):
        return f"物流狀況 {self.order_id} - {self.status}"
