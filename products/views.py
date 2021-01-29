from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

# Create your views here.


def all_products(request):
    # Will show all products, searches and sorting.

    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/products.html', context)
