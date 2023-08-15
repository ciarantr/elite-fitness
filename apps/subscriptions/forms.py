from django import forms

from .models import Subscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('first_name', 'last_name', 'email',)
        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'First Name *'}),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Last Name *'}),
            'email': forms.TextInput(
                attrs={'placeholder': 'Email Address *'}),
        }

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if self.errors.get(name):
                continue
            field.help_text = ""
