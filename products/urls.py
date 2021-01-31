from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('add/', views.add_product, name='add_product'),
    path('<int:product_id>/', views.product_single, name='product_single'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
]