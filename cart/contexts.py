from django.conf import settings


def cart_items(request):

    cart_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = settings.STANDARD_DELIVERY_COST
    else:
        delivery = 0

    if cart_items:
        grand_total = delivery + total
    else: 
        grand_total = 0

    context = {
        'delivery': delivery,
        'total': total,
        'grand_total': grand_total,
        'product_count': product_count,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'cart_items': cart_items,
    }

    return context