from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Category, Device
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
    devices = None
    sort = None
    direction = None
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'modname':
                sortkey = 'lower_modname'
                products = products.annotate(lower_modname=Lower('model_name'))

            if sortkey == "catergory":
                sortkey = "category__name"

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'device' in request.GET:
            devices = request.GET['device'].split(',')
            products = products.filter(device__name__in=devices)
            devices = Device.objects.filter(name__in=devices)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter some text to search")
                return redirect(reverse('products'))

            queries = Q(model_name__icontains=query) | Q(description__icontains=query) | Q(
                cpu__icontains=query) | Q(ram__icontains=query) | Q(gpu__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_devices': devices,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_single(request, product_id):
    # Will open the single product page
    product = get_object_or_404(Product, model_name=product_id)

    print(product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_single.html', context)



