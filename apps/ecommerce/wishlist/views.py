from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView

from .forms import CreateWishlistForm, \
    EditWishlistForm
from .models import List


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

