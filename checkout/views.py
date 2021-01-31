from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from django.conf import settings

# Create your views here.


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "You don't have any items in your cart right now")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'stripe_secret_key': settings.STRIPE_SECRET_KEY,
    }

    return render(request, template, context)