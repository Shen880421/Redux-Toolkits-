from django.db import models
from users.models import User
from coupons.models import Coupon


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="顧客", related_name="orders"
    )
    total_amount = models.DecimalField("總金額", max_digits=10, decimal_places=2)
    PAYMENT_METHOD_CHOICES = [
        ("credit_card", "信用卡"),
        ("line_pay", "Line Pay"),
        ("cash", "貨到付款"),
    ]

    PAYMENT_STATUS_CHOICES = [
        ("pending", "待付款"),
        ("paid", "已付款"),
        ("failed", "付款失敗"),
        ("refunded", "已退款"),
    ]

    SHIPPING_METHOD_CHOICES = [
        ("home_delivery", "宅配"),
        ("convenience_store", "超商取貨"),
    ]

    SHIPPING_STATUS_CHOICES = [
        ("preparing", "備貨中"),
        ("shipped", "已出貨"),
        ("delivered", "已送達"),
        ("returned", "已退貨"),
    ]

    payment_method = models.CharField(
        "付款方式", max_length=50, choices=PAYMENT_METHOD_CHOICES
    )
    payment_status = models.CharField(
        "付款狀態", max_length=50, choices=PAYMENT_STATUS_CHOICES, default="pending"
    )
    shipping_method = models.CharField(
        "運送方式", max_length=50, choices=SHIPPING_METHOD_CHOICES
    )
    shipping_status = models.CharField(
        "運送狀態", max_length=50, choices=SHIPPING_STATUS_CHOICES, default="preparing"
    )
    receiver_name = models.CharField("收件人姓名", max_length=100)
    receiver_phone = models.CharField("收件人電話", max_length=15)
    receiver_address = models.CharField("收件地址", max_length=255)
    coupon = models.ForeignKey(
        "coupons.Coupon",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="優惠券",
    )
    created_at = models.DateTimeField("建立時間", auto_now_add=True)
    updated_at = models.DateTimeField("更新時間", auto_now=True)

    class Meta:
        verbose_name = "訂單"
        verbose_name_plural = "訂單"
        ordering = ["-created_at"]  # 依建立時間排序，最新的在前面

    def __str__(self):
        return f"訂單 {self.id} - {self.receiver_name}"
