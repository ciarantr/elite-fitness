from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from .models import Order


class OrderView(LoginRequiredMixin, TemplateView):
    """
    This view handles the display of the order page
    """
    template_name = 'checkout_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order_number = kwargs.get('order_number')
        order = get_object_or_404(Order, order_number=order_number)
        if order.user_profile.user.id == self.request.user.id:
            context['order'] = order
        else:
            raise PermissionDenied()

        return context
