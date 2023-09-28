from django.urls import path

from .views import ConfirmSignupView

urlpatterns = [
    path('confirm-signup/<uuid:confirmation_token>/',
         ConfirmSignupView.as_view(),
         name='confirm-signup'),
]
