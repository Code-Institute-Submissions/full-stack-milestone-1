from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Category, Device, Reviews, Upgrade
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm, UpgradeForm, ProductForm
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
    product = get_object_or_404(Product, pk=product_id)

    form = ReviewForm()
    # displays and assigns review model / form
    if 'review' in request.POST:
        review = request.POST.get("review")
        review = Reviews(user=request.user, product=product, review=review)
        review.save()
    reviews_already_posted = Reviews.objects.filter(product=product)

    form2 = UpgradeForm()
    # displays and assigns review model / form
    if 'upgrade' in request.POST:
        upgrade = request.POST.get("upgrade")
        upgrade = Upgrade(user=request.user, product=product, upgrade=upgrade)
        upgrade.save()
    upgrades_already_posted = Upgrade.objects.filter(product=product)

    print(product_id)
    context = {
        'product': product,
        'form': form,
        'form2': form2,
        'reviews': reviews_already_posted,
        'upgrade': upgrades_already_posted,
    }
    return render(request, 'products/product_single.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_single', args=[product.pk]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_single', args=[product.pk]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.model_name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)



@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))