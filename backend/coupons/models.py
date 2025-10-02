from django.db import models


# Create your models here.
class Coupon(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100, unique=True)
    discount_type = models.CharField(
        max_length=10,
        choices=[
            ("percentage", "打折"),
            ("fixed", "固定金額"),
        ],
    )
    discount_value = models.IntegerField()
    min_order_amount = models.IntegerField()
    usage_limit = models.IntegerField()
    used_count = models.IntegerField(default=0)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "優惠券"
        verbose_name_plural = "優惠券"
        ordering = ["-created_at"]  # 依建立時間排序，最新的在前面

    def __str__(self):
        return f"優惠券 {self.code} - {self.discount_value}"
