from django.views.generic import TemplateView

from apps.ecommerce.products.models import Product


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(
            category__name__icontains='supplements')[:3]
        # Assign image to each product
        for product in context['products']:
            product.image = product.images.first()

        return context
