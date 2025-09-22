from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def signup(request):
    if request.method == "POST":
        # 解析 JSON 數據
        data = json.loads(request.body)
        account = data.get("account")
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")
        phone = data.get("phone")
        birthdate = data.get("birthdate")
        gender = data.get("gender")
        role = data.get("role", "customer")  # 預設為 'customer'

        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists."}, status=400)

        user = User(
            account=account,
            username=username,
            email=email,
            password_hash=make_password(password),
            phone=phone,
            birthdate=birthdate,
            gender=gender,
            role=role,
        )
        user.save()

        return JsonResponse(
            {
                "message": "User created successfully",
                "user": {"username": user.username, "email": user.email},
            }
        )

    return JsonResponse({"error": "Method not allowed"}, status=405)
