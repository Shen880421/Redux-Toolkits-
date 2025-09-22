from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import User


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {"error": "Username already exists."})

        user = User(
            username=username,
            email=email,
            password_hash=make_password(password),  # 密碼雜湊
        )
        user.save()

        return render(request, "signup_success.html", {"user": user})
