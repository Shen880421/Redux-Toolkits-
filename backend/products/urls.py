from django.urls import path
from . import views

urlpatterns = [
    path("productsList/", views.list_products, name="list_products"),
    path("addProduct/", views.add_product, name="add_product"),
]
