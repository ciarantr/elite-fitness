from django.urls import path

from .views import (WishListDetailView, WishListView, WishlistAddProductView,
                    WishlistCreateView, WishlistDeleteFormView,
                    WishlistRemoveProductView, WishlistUpdateView)

urlpatterns = [
    path('wishlist/', WishListView.as_view(), name='wishlist'),
    path('wishlist/details/<int:pk>/', WishListDetailView.as_view(),
         name='wishlist_details'),
    path('wishlist/create/', WishlistCreateView.as_view(),
         name='wishlist_create'),
    path('wishlist/edit/<int:pk>/', WishlistUpdateView.as_view(),
         name='wishlist_update'),
    path('wishlist/delete/<int:pk>/', WishlistDeleteFormView.as_view(),
         name='wishlist_delete'),
    path('wishlist/add/<int:product_id>/', WishlistAddProductView.as_view(),
         name='wishlist_product_add'),
    path('wishlist/<int:list_id>/product-remove/<int:product_id>/',
         WishlistRemoveProductView.as_view(),
         name='wishlist_product_remove'),
]
