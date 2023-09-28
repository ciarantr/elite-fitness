from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView

from apps.ecommerce.products.models import (Brand, Category, Product)


class AllProductsView(ListView):
    """ A view to display all products"""
    template_name = 'products.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 15

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.category_name = None
        self.brand_name = None

    def get_queryset(self):
        filters = Q()
        fields = ['q', 'brand', 'category']

        for field in fields:
            value = self.request.GET.get(field)

            if value:
                if field == 'q':
                    # for other fields ('brand' and 'category'),
                    # do an exact match (case-insensitive)
                    filters |= (Q(name__icontains=value) |
                                Q(description__icontains=value) |
                                Q(category__slug__icontains=value) |
                                Q(brand__slug__icontains=value))
                elif field == 'brand':
                    brand = get_object_or_404(Brand, slug=value)
                    self.brand_name = brand.name
                    filters |= Q(brand__slug__iexact=value)
                elif field == 'category':
                    category = get_object_or_404(Category, slug=value)
                    self.category_name = category.name
                    filters |= Q(category__slug__iexact=value)
                else:
                    filters |= Q(**{f"{field}__slug__iexact": value})

        queryset = Product.objects.filter(filters)

        sort = self.request.GET.get('sort')
        if sort:
            if sort == 'reset':
                queryset = queryset.order_by('pk')
            if sort == 'price-low-high':
                queryset = queryset.order_by('price')
            elif sort == 'price-high-low':
                queryset = queryset.order_by('-price')
            elif sort == 'newest':
                queryset = queryset.order_by('-created')

        return queryset.prefetch_related('images')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Sort the products by the selected option
        context['sort_options'] = {
            'Reset': 'reset',
            'Price (Low-High)': 'price-low-high',
            'Price (High-Low)': 'price-high-low',
            'Newest': 'newest',
        }
        context['current_sort'] = self.request.GET.get('sort', '')

        # Get all the product categories and add them to the context
        product_categories = (
            Product.objects.values('category__name', 'category__slug')
            .distinct().order_by('category__name')
        )
        context['categories'] = {item['category__name']: item['category__slug']
                                 for item in product_categories}

        # Get all the product brands and add them to the context
        product_brands = (
            Product.objects.values('brand__name', 'brand__slug')
            .distinct().order_by('brand__name')
        )
        context['brands'] = {
            item['brand__name']: item['brand__slug'] for item in product_brands
        }

        # Add the first image of each product to the context
        for product in context[self.context_object_name]:
            if product.images.exists():
                product.image = product.images.first().image.url
            else:
                # set the default image
                product.image = '/media/products/placeholder.svg'

        # Count the number of matching results and add to the context
        results_count = context[self.context_object_name].count()

        context['results_count'] = results_count
        context['query'] = self.request.GET.get('q')
        context['brand'] = self.request.GET.get('brand')
        context['category'] = self.request.GET.get('category')
        context['category_name'] = self.category_name
        context['brand_name'] = self.brand_name

        return context


class ProductDetailView(TemplateView):
    """ A view to display a single product"""
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the product otherwise return 404
        product = get_object_or_404(
            Product.objects.prefetch_related('images'),
            slug=self.kwargs['slug'])

        if product.images.exists():
            product.image = product.images.first().image.url
        else:
            # set the default image
            product.image = '/media/products/placeholder.svg'

        context['product'] = product
        context['category'] = product.category.first()
        context['benefits'] = product.benefits.all()
        context['key_benefits'] = product.key_benefits.all()

        if product.brand:
            product_brand_name = product.brand.name.split()
            product_name_parts = product.name.split()
            #  remove brand name from product name if it exists
            if product_name_parts[0].lower() == product_brand_name[0].lower():
                context['product_brand_name'] = ' '.join(
                    product_name_parts[1:]).strip()

        return context
