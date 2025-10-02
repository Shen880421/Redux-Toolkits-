from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def add_product(request):
    if request.method == "POST":
        # 解析 JSON 數據
        data = json.loads(request.body)
        name = data.get("name")
        attribute = data.get("attribute")
        expiration_days = data.get("expiration_days")
        image_url = data.get("image_url")
        price = data.get("price")
        stock = data.get("stock")
        description = data.get("description")

        if Product.objects.filter(name=name).exists():
            return JsonResponse({"error": "Product already exists."}, status=400)

        product = Product(
            name=name,
            attribute=attribute,
            expiration_days=expiration_days,
            image_url=image_url,
            price=price,
            stock=stock,
            description=description,
        )
        product.save()

        return JsonResponse(
            {
                "message": "Product added successfully",
                "product": {"name": product.name, "price": product.price},
            }
        )

    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def list_products(request):
    if request.method == "GET":
        products = Product.objects.all()
        product_list = [
            {
                "id": product.id,
                "name": product.name,
                "attribute": product.attribute,
                "expiration_days": product.expiration_days,
                "image_url": product.image_url,
                "price": str(product.price),
                "stock": product.stock,
                "description": product.description,
            }
            for product in products
        ]
        return JsonResponse({"products": product_list})
    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def get_product(request, product_id):
    if request.method == "GET":
        try:
            product = Product.objects.get(id=product_id)
            product_data = {
                "id": product.id,
                "name": product.name,
                "attribute": product.attribute,
                "expiration_days": product.expiration_days,
                "image_url": product.image_url,
                "price": str(product.price),
                "stock": product.stock,
                "description": product.description,
            }
            return JsonResponse({"product": product_data})
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product not found"}, status=404)
    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def delete_product(request, product_id):
    if request.method == "DELETE":
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            return JsonResponse({"message": "Product deleted successfully"})
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product not found"}, status=404)
    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def update_product(request, product_id):
    if request.method == "PUT":
        try:
            product = Product.objects.get(id=product_id)
            data = json.loads(request.body)
            product.name = data.get("name", product.name)
            product.attribute = data.get("attribute", product.attribute)
            product.expiration_days = data.get(
                "expiration_days", product.expiration_days
            )
            product.image_url = data.get("image_url", product.image_url)
            product.price = data.get("price", product.price)
            product.stock = data.get("stock", product.stock)
            product.description = data.get("description", product.description)
            product.save()
            return JsonResponse({"message": "Product updated successfully"})
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product not found"}, status=404)
    return JsonResponse({"error": "Method not allowed"}, status=405)
