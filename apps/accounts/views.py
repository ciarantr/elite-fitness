from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .forms import CustomerDeliveryForm, UserUpdateForm
from .models import DeliveryDetails


class ProfileView(LoginRequiredMixin, UpdateView):
    """
    This view is responsible for displaying the user's profile information
    """
    template_name = 'profile.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('profile')
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        #     return logged in user
        return get_object_or_404(User, pk=self.request.user.pk)

    def form_valid(self, form):
        messages.success(self.request, 'Profile updated successfully')
        return super().form_valid(form)


class OrderProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'delivery_information.html'
    model = DeliveryDetails
    form_class = CustomerDeliveryForm
    success_url = reverse_lazy('order_information')
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_object_or_404(
            DeliveryDetails.objects.prefetch_related('orders'),
            user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request,
                         'Delivery information updated successfully')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = self.object.orders.all()
        context['on_profile_page'] = True
        return context
