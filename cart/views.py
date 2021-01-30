from django.shortcuts import render

# Create your views here.


def view_cart(request):
    # will open the cart
    return render(request, 'cart/cart.html')
