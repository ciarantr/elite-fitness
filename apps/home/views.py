from django.shortcuts import redirect
from django.views.generic import TemplateView

from apps.ecommerce.products.models import Product
from apps.subscriptions.forms import SubscriptionForm
from apps.subscriptions.models import Subscription


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(
            category__name__icontains='supplements')[:3]
        # Assign image to each product
        for product in context['products']:
            product.image = product.images.first()
        # Add a subscription form
        context['form'] = SubscriptionForm()

        return context

    def post(self, request, *args, **kwargs):
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if not Subscription.objects.filter(email=email).exists():
                form.save()
                return redirect('home')
        else:
            # add form errors to context
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
