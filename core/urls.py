"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import Handler403View, Handler404View, Handler500View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('apps.accounts.urls')),
    path('account/', include('allauth.urls')),
    path('', include('apps.home.urls')),
    path('products/', include('apps.ecommerce.products.urls')),
    path('cart/', include('apps.ecommerce.cart.urls')),
    path('', include('apps.ecommerce.wishlist.urls')),
    path('checkout/', include('apps.ecommerce.checkout.urls')),
    path('support/', include('apps.customer_support.urls')),
    path('subscriptions/', include('apps.subscriptions.urls')),
    path('', include('apps.ecommerce.orders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = Handler500View.as_view()
handler403 = Handler403View.as_view()
handler404 = Handler404View.as_view()
