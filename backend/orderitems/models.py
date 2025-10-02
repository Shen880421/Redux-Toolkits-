from django.db import models
from orders.models import Order
from products.models import Product


# Create your models here.
class OrderItems(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "訂單項目"
        verbose_name_plural = "訂單項目"
        ordering = ["-created_at"]  # 依建立時間排序，最新的在前面

    def __str__(self):
        return (
            f"訂單項目 {self.order_id} - 產品 {self.product_id} - 數量 {self.quantity}"
        )
