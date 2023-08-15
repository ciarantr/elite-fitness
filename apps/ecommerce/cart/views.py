from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, reverse
from django.views import View
from django.views.generic import TemplateView

from apps.ecommerce.products.models import Product


class CartPageView(TemplateView):
    template_name = 'cart.html'


class AddToCartView(View):
    def post(self, request, item_id):
        product = Product.objects.get(pk=item_id)
        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')

        cart = request.session.get('cart', {})

        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request,
                             f'Updated {product.name} quantity to '
                             f'{cart[item_id]}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart')

        request.session['cart'] = cart
        return redirect(redirect_url)


class RemoveFromCartView(View):
    def post(self, request, item_id):
        try:
            product = get_object_or_404(Product, pk=item_id)

            cart = request.session.get('cart', {})

            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

            request.session['cart'] = cart
            return redirect(reverse('cart'))

        except Exception as e:
            messages.error(request, f'Error removing item: {e}')
            return HttpResponse(status=500)


class AdjustCartView(View):
    def post(self, request, item_id):
        product = get_object_or_404(Product, pk=item_id)
        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')

        cart = request.session.get('cart', {})

        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Updated {product.name}'
                                      f' quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return redirect(redirect_url)

