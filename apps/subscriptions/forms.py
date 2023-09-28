from django import forms

from .models import Subscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('first_name', 'last_name', 'email',)
        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'First Name *', 'minlength': 3}),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Last Name *', 'minlength': 3}),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Email Address *'}),
        }
