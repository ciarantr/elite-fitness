from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

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
