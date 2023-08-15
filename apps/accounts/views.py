from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from core import settings
from .forms import CustomLoginForm, CustomUserCreationForm
from .forms import CustomerProfileForm
from .models import CustomerProfile


class AccountLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html'
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)
    redirect_authenticated_user = True


class AccountRegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = settings.LOGIN_REDIRECT_URL
    template_name = 'register.html'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(*args, **kwargs)


class AccountLogoutView(LogoutView):
    next_page = settings.LOGOUT_REDIRECT_URL


class CustomerProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'profile.html'
    model = CustomerProfile
    form_class = CustomerProfileForm
    success_url = '/profile/'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_object_or_404(CustomerProfile, user=self.request.user)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Profile updated successfully')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = self.object.orders.all()
        context['on_profile_page'] = True
        return context
