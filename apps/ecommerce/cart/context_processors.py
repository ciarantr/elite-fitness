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

    for item_id, count in cart.items():
        product =  get_object_or_404(Product, pk=item_id)
        max_stock = product.stock
        actual_quantity = min(count, max_stock)
        cart_items.append({
            'product': product,
            'quantity': actual_quantity,
            'price': product.price,
            'total': product.price * actual_quantity,
            'stock': max_stock,
            'image': product.images.first().image if product.images.count() > 0 else None,
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

    context = {
        'cart_items': cart_items,
        'cart_total_quantity': total_quantity,
        'delivery_cost': delivery_cost,
        'subtotal': subtotal,
        'grand_total': grand_total,
    }

    return context
