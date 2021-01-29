from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.


def all_products(request):
    # Will show all products, searches and sorting.

    products = Product.objects.all()
    query = None
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter some text to search")
                return redirect(reverse('products'))

            queries = Q(model_name__icontains=query) | Q(description__icontains=query) | Q(device_type__icontains=query) | Q(cpu__icontains=query) | Q(cpu__icontains=query) | Q(gpu__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products
    }
    return render(request, 'products/products.html', context)


def product_single(request, product_name):
    # Will open the single product page
    # seo friendly as the url is the product name

    product = get_object_or_404(Product, model_name=product_name)
    context = {
        'product': product
    }
    return render(request, 'products/product_single.html', context)
