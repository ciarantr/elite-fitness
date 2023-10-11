from django.urls import path

from .views import OrderView

urlpatterns = [
    path('account/order/<str:order_number>/',
         OrderView.as_view(), name='order_history_view'),
]
