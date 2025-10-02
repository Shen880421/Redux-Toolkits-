from django.db import models


class User(models.Model):
    GENDER_CHOICES = [("male", "男性"), ("female", "女性"), ("other", "其他")]

    ROLE_CHOICES = [("customer", "顧客"), ("admin", "管理員")]
    id = models.AutoField("使用者ID", primary_key=True)
    account = models.CharField("帳號", max_length=100, unique=True)
    password_hash = models.CharField("密碼雜湊", max_length=255)
    username = models.CharField("使用者名稱", max_length=100)
    email = models.EmailField("電子郵件", null=True, blank=True)
    phone = models.CharField("手機號碼", max_length=20)
    birthdate = models.DateField("生日", null=True, blank=True)
    gender = models.CharField("性別", max_length=10, choices=GENDER_CHOICES)
    role = models.CharField(
        "角色", max_length=10, choices=ROLE_CHOICES, default="customer"
    )
    created_at = models.DateTimeField("建立時間", auto_now_add=True)
    updated_at = models.DateTimeField("更新時間", auto_now=True)

    class Meta:
        verbose_name = "使用者"
        verbose_name_plural = "使用者"

    def __str__(self):
        return self.username
