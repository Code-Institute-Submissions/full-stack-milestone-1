
from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def account(request):
    """ Display the user's profile. """
    account = get_object_or_404(UserProfile, user=request.user)

    template = 'accounts/account.html'
    context = {
        'account': account,
    }

    return render(request, template, context)