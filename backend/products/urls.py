from django.urls import path
from . import views

urlpatterns = [
    path("productsList/", views.list_products, name="list_products"),
    path("addProduct/", views.add_product, name="add_product"),
    path("<int:product_id>/", views.get_product, name="get_product"),
    path("<int:product_id>/delete/", views.delete_product, name="delete_product"),
    path("<int:product_id>/update/", views.update_product, name="update_product"),
]
