from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Category
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse
from django.db.models.functions import Lower

# Create your views here.


def all_products(request):
    # Will show all products, searches and sorting.

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'model_name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('model_name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter some text to search")
                return redirect(reverse('products'))

            queries = Q(model_name__icontains=query) | Q(description__icontains=query) | Q(
                device_type__icontains=query) | Q(cpu__icontains=query) | Q(ram__icontains=query) | Q(gpu__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
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
