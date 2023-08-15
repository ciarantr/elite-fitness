from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import CustomerProfile


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update(
            {'placeholder': 'Password'})


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            # Adding placeholder
            field.widget.attrs['placeholder'] = field.label
            # Hiding initial help_text
            field.help_text = ''

    class Meta(UserCreationForm.Meta):
        model = UserCreationForm.Meta.model
        fields = UserCreationForm.Meta.fields


class CustomerProfileForm(forms.ModelForm):

    class Meta:
        model = CustomerProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated labels
        """

        super().__init__(*args, **kwargs)

        placeholders = {
            'username': 'Username',
            'full_name': 'Full Name',
            'email': 'Email Address',
            'default_phone_number': 'Phone Number',
            'default_country': 'Country',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                self.fields[field].required = \
                    True if field == 'username' else False
                placeholder = f'{placeholders[field]} *' \
                    if self.fields[field].required else placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
