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
                "user": {"id": user.id, "username": user.username, "email": user.email},
            }
        )

    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def list_users(request):
    if request.method == "GET":
        users = User.objects.all()
        user_list = [
            {
                "id": user.id,
                "account": user.account,
                "username": user.username,
                "email": user.email,
                "phone": user.phone,
                "birthdate": user.birthdate,
                "gender": user.gender,
                "role": user.role,
                "created_at": user.created_at,
            }
            for user in users
        ]
        return JsonResponse({"users": user_list})
    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def get_user(request, user_id):
    if request.method == "GET":
        try:
            user = User.objects.get(id=user_id)
            user_data = {
                "account": user.account,
                "username": user.username,
                "email": user.email,
                "phone": user.phone,
                "birthdate": user.birthdate,
                "gender": user.gender,
                "role": user.role,
                "created_at": user.created_at,
                "updated_at": user.updated_at,
            }
            return JsonResponse({"user": user_data})
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)

    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def delete_user(request, user_id):
    if request.method == "DELETE":
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return JsonResponse({"message": "User deleted successfully"})
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def update_user(request, user_id):
    if request.method == "PUT":
        try:
            user = User.objects.get(id=user_id)
            data = json.loads(request.body)
            user.account = data.get("account", user.account)
            user.username = data.get("username", user.username)
            user.email = data.get("email", user.email)
            if "password" in data:
                user.password_hash = make_password(data["password"])
            user.phone = data.get("phone", user.phone)
            user.birthdate = data.get("birthdate", user.birthdate)
            user.gender = data.get("gender", user.gender)
            user.role = data.get("role", user.role)
            user.save()
            return JsonResponse({"message": "User updated successfully"})
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
    return JsonResponse({"error": "Method not allowed"}, status=405)
