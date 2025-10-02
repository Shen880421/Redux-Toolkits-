from django.db import models


class Product(models.Model):
    attribute_choices = [
        ("frozen", "冷凍"),
        ("refrigeration", "冷藏"),
        ("room_temperature", "常溫"),
    ]
    name = models.CharField("產品名稱", max_length=200)
    price = models.DecimalField("價格", max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField("庫存量")
    attribute = models.CharField(
        "產品屬性", max_length=100, blank=True, choices=attribute_choices
    )
    expiration_days = models.PositiveIntegerField("保存天數", null=True, blank=True)
    image_url = models.URLField("產品圖片 URL", blank=True)
    description = models.TextField("產品描述", blank=True)
    created_at = models.DateTimeField("建立時間", auto_now_add=True)
    updated_at = models.DateTimeField("更新時間", auto_now=True)

    class Meta:
        verbose_name = "產品"
        verbose_name_plural = "產品"

    def __str__(self):
        return self.name
