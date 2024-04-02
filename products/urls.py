from django.urls import path
from .views import ProductList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete

urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),
    path('products/<int:id>', ProductDetail.as_view(), name='product-detail'),
    path('products/create/', ProductCreate.as_view(), name='product-create'),
    path('products/edit/<int:id>', ProductUpdate.as_view(), name='product-edit'),
    path('products/delete/<int:id>', ProductDelete.as_view(), name='product-delete'),
]
