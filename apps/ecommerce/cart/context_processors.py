# context_processors.py
from django.conf import settings
from django.shortcuts import get_object_or_404

from apps.ecommerce.products.models import Product


def cart_processor(request):
    cart = request.session.get('cart', {})
    total_quantity = 0
    subtotal = 0
    grand_total = 0
    cart_items = []
    path = request.path

    for item_id, count in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        max_stock = product.stock
        actual_quantity = min(count, max_stock)
        cart_items.append({
            'product': product,
            'quantity': actual_quantity,
            'price': product.price,
            'total': product.price * actual_quantity,
            'stock': max_stock,
            # get the first image of the product or media placeholder.svg
            'image': product.images.first().image.url
            if product.images.count() > 0
            else settings.MEDIA_URL + 'products/placeholder.svg',
        })
        total_quantity += actual_quantity
        subtotal += product.price * actual_quantity

    grand_total = subtotal
    # Calculate delivery cost
    if subtotal >= settings.FREE_DELIVERY_THRESHOLD:
        delivery_cost = 0

    else:
        delivery_cost = settings.STANDARD_DELIVERY_COST
        grand_total += delivery_cost

    excluded_paths = [
        '/cart/',
        '/account/profile/',
        '/checkout/',
        '/wishlist/',
        '/account/confirm-email/',
        '/support/contact/',
        'subscriptions/confirm-signup/<uuid:confirmation_token>/',
        'subscriptions/confirm-signup/94bee8f-97d2-4fc1-accf-fc61610a787b/',
    ]

    exclude_path = any(path.startswith(excluded_path) for excluded_path in
                       excluded_paths)

    context = {
        'cart_items': cart_items,
        'cart_total_quantity': total_quantity,
        'delivery_cost': delivery_cost,
        'subtotal': subtotal,
        'grand_total': grand_total,
        'is_excluded_path': exclude_path,
    }

    return context
