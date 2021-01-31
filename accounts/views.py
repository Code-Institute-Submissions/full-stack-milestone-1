  
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


def account(request):
    """ Display the user's profile. """
    account = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed please ensure it is filled out properly.')
    else:
        form = UserProfileForm(instance=account)
    orders = account.orders.all()
    template = 'accounts/account.html'
    context = {
        'form': form,
        'orders': orders,
        'on_account_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f' this is a past conformation for order number {order_number}.'
        ' A confirmatoion email was sent on the order date'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_account': True,
    }

    return render(request, template, context)