from django.urls import path

from .views import AccountLoginView, AccountLogoutView, AccountRegisterView, \
    CustomerProfileView

urlpatterns = [
    path('login/', AccountLoginView.as_view(), name='login'),
    path('register/', AccountRegisterView.as_view(), name='register'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    path('profile/', CustomerProfileView.as_view(), name='profile'),
]
