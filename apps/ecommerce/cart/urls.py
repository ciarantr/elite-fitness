from django.urls import path

from .views import (AddToCartView, AdjustCartView, CartPageView,
                    RemoveFromCartView)

urlpatterns = [
    path('', CartPageView.as_view(), name='cart'),
    path('add/<item_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove/<item_id>/', RemoveFromCartView.as_view(),
         name='remove_from_cart'),
    path('adjust/<item_id>/', AdjustCartView.as_view(), name='adjust_cart'),
]
