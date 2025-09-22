from django.shortcuts import render
from .models import User


# Create your views here.
def signup(request):
    if request.method == "POST":
        # Handle signup logic here
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        user.save()
        return render(request, "signup.html", {"success": True})
    return render(request, "signup.html")
