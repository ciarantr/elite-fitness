from allauth.account.views import (ConfirmEmailView, EmailVerificationSentView,
                                   LoginView,
                                   PasswordResetDoneView,
                                   PasswordResetFromKeyDoneView,
                                   PasswordResetFromKeyView, PasswordResetView,
                                   SignupView)
from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import OrderProfileView, ProfileView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'),
         name='login'),
    path('register/', SignupView.as_view(template_name='register.html'),
         name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(),
         name='profile'),
    path('profile/order-information', OrderProfileView.as_view(),
         name='order_information'),
    path('password-reset/',
         PasswordResetView.as_view(template_name='password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(
             template_name='password_reset_confirm.html'),
         name='account_reset_password_done'),
    path('password/reset/key/<uidb36>/<key>/',
         PasswordResetFromKeyView.as_view(
             template_name='password_reset_from_key.html'),
         name='account_reset_password_from_key'),
    path(
        "password/reset/key/done/",
        PasswordResetFromKeyDoneView.as_view(
            template_name='password_reset_done.html'),
        name="account_reset_password_from_key_done",
    ),
    path('confirm-account/<str:key>/',
         ConfirmEmailView.as_view(template_name='email_confirm.html'),
         name='account_confirm_email'),
    path('confirm-email/',
         EmailVerificationSentView.as_view(
             template_name='verification_sent.html'),
         name='account_email_verification_sent'),
]
