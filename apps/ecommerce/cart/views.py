from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView

from apps.ecommerce.products.models import Product
from apps.ecommerce.wishlist.forms import AddProductToWishlistForm
from apps.ecommerce.wishlist.models import List


class CartPageView(TemplateView):
    """
    This view handles the display of the cart page
    """

    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context['wishlist_exists'] = List.objects.filter(
                user=self.request.user).exists()
            context['add_to_wishlist_form'] = AddProductToWishlistForm(
                user=self.request.user)
        return context


class AddToCartView(View):
    """
    This view handles the addition of a product to the cart
    """

    def post(self, request, item_id):
        product = Product.objects.get(pk=item_id)
        quantity = int(request.POST.get('quantity')) if request.POST.get(
            'quantity') else 1
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
    """
    This view handles the removal of a product from the cart
    """

    def post(self, request, item_id):
        try:
            product = get_object_or_404(Product, pk=item_id)

            cart = request.session.get('cart', {})

            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

            request.session['cart'] = cart
            redirect_url = request.POST.get('redirect_path')

            return redirect(redirect_url)

        except Exception as e:
            messages.error(request, f'Error removing item: {e}')
            return HttpResponse(status=500)


class AdjustCartView(View):
    """
    This view handles the adjustment of a product quantity in the cart
    """

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
