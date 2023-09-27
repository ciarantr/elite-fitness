from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView, FormView, ListView, \
    UpdateView

from .forms import AddProductToWishlistForm, CreateWishlistForm, \
    EditWishlistForm
from .models import List
from ..products.models import Product


class WishListView(LoginRequiredMixin, ListView):
    """
    This view is responsible for displaying and managing the user's wishlists
    """
    model = List
    template_name = 'wishlist.html'
    context_object_name = 'wishlists'
    paginate_by = 5

    def get_queryset(self):
        """
        This method is an in-built method in ListView used to
        control the list of items that the view operates upon.
        """
        return List.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_wishlist_form'] = CreateWishlistForm()
        context['edit_wishlist_form'] = EditWishlistForm()
        return context


class WishlistCreateView(LoginRequiredMixin, FormView):
    """
    This view handles the creation of a wishlist
    """
    model = List
    form_class = CreateWishlistForm
    success_url = reverse_lazy('wishlist')
    template_name = 'wishlist.html'

    def form_valid(self, form):
        wishlist = form.save(commit=False)
        wishlist.user = self.request.user
        wishlist.save()
        messages.success(self.request, 'Wishlist successfully created.')
        return super().form_valid(form)

    def form_invalid(self, form):
        #  displays all errors in the form
        for field in form.errors:
            for error in form.errors[field]:
                messages.error(self.request, error)

        return redirect('wishlist')


class WishlistDeleteFormView(LoginRequiredMixin,
                             SuccessMessageMixin, DeleteView):
    """
    This view handles the removal of a wishlist
    """
    model = List
    success_url = reverse_lazy('wishlist')
    template_name = 'wishlist.html'
    success_message = 'Wishlist successfully removed.'

    def get_object(self, queryset=None):
        """Return the wishlist to be deleted."""
        return get_object_or_404(
            List, pk=self.kwargs['pk'], user=self.request.user)


class WishListDetailView(LoginRequiredMixin, View):
    """
    This view is responsible for returning the description
    of a specific wishlist
    """

    def get(self, request, *args, **kwargs):
        wishlist = get_object_or_404(List, pk=self.kwargs['pk'],
                                     user=self.request.user)
        if wishlist.description is None:
            return JsonResponse({'description': ''})
        else:
            return JsonResponse({'description': wishlist.description})


class WishlistUpdateView(LoginRequiredMixin, UpdateView):
    """
    This view handles the editing of a wishlist
    """
    model = List
    fields = ['name', 'description']
    success_url = reverse_lazy('wishlist')
    template_name = 'wishlist.html'

    def form_valid(self, form):
        messages.success(self.request, 'Wishlist successfully updated.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Wishlist could not be updated.')
        return super().form_invalid(form)


class WishlistAddProductView(LoginRequiredMixin, View):
    """
    This view handles the addition of a product to a wishlist
    """

    def post(self, request, product_id):
        form = AddProductToWishlistForm(request.POST, user=request.user)
        if form.is_valid():
            product = get_object_or_404(Product, pk=product_id)

            selected_wishlists_ids = {
                wishlist.id for wishlist in form.cleaned_data['wishlist']}
            user_wishlists = form.fields['wishlist'].queryset

            cart = request.session.get('cart', {})

            for wishlist in user_wishlists:
                if product in wishlist.products.all():
                    if wishlist.id in selected_wishlists_ids:
                        # If the product is in the wishlist and the wishlist
                        # is selected, do nothing
                        pass
                    else:
                        # If the product is in the wishlist but the wishlist
                        # is not selected, remove the product from the wishlist
                        wishlist.products.remove(product)
                        messages.success(request, 'Product removed from '
                                                  'wishlist.')
                else:
                    if wishlist.id in selected_wishlists_ids:
                        # If the product is not in the wishlist but the
                        # wishlist is selected, add the product to the wishlist
                        wishlist.products.add(product)
                        # remove the product from the cart
                        if str(product.id) in cart:
                            cart.pop(str(product.id))
                            request.session['cart'] = cart
                        messages.success(request, 'Product moved to wishlist.')

            return redirect('cart')
        messages.error(request, 'Failed to update wishlist.', form.errors)
        return redirect('cart')


class WishlistRemoveProductView(LoginRequiredMixin, View):
    """
    This view handles the removal of a product from a wishlist
    """

    def post(self, request, *args, **kwargs):
        # get the wishlist and product objects
        list_obj = get_object_or_404(List, id=kwargs['list_id'])

        try:
            list_obj.products.remove(kwargs['product_id'])
            messages.success(request, 'Product removed from wishlist.')
        except Exception as e:
            messages.error(request, f'Failed to remove product: {str(e)}')

        return redirect('wishlist')
