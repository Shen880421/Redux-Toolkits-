from enum import unique
from django.db import models


# Create your models here.
class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    status = models.CharField(
        max_length=10,
        choices=[
            ("pending", "待付款"),
            ("success", "已付款"),
            ("failed", "付款失敗"),
            ("refunded", "已退款"),
        ],
    )
    transaction_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "付款"
        verbose_name_plural = "付款"
        ordering = ["-created_at"]  # 依建立時間排序，最新的在前面

    def __str__(self):
        return f"付款 {self.order_id} - {self.status} - {self.amount}"
