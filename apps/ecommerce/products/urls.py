from django.urls import path

from apps.ecommerce.products.views import AllProductsView, ProductDetailView

urlpatterns = [
    path('', AllProductsView.as_view(), name='products'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]
