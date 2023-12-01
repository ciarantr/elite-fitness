from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import DeliveryDetails


class UserUpdateForm(forms.ModelForm):
    """
    A customer profile model for maintaining default
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].initail = self.instance.email

        for field in self.fields.values():
            # Adding placeholder
            field.widget.attrs['placeholder'] = field.label
            # Hiding initial help_text
            field.help_text = ''
            # Ensure the email field is required
            self.fields['email'].required = True
            # Add * to required placeholder
            if field.required:
                field.widget.attrs['placeholder'] = f'{field.label} *'


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


class CustomerDeliveryForm(forms.ModelForm):
    """
    A customer profile model for maintaining default delivery information
    """

    class Meta:
        model = DeliveryDetails
        exclude = ('user',)
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        non_required_fields = ('default_phone_number',
                               'default_street_address2',
                               'default_postcode',
                               'default_county')
        # Replace underscores with spaces and title case field names
        placeholders = {field: field.replace("_", " ").title() for field in
                        self.fields}

        # Update placeholders and set autofocus on first field
        for field in self.fields:
            field_obj = self.fields[field]

            # set the required attribute for all fields including select
            if field not in non_required_fields:
                field_obj.required = True

            # Skip placeholder for select fields (django-countries)
            if field_obj.widget.input_type == 'select':
                continue

            field_obj.widget.attrs.update({'placeholder': placeholders[field]})

            if field not in non_required_fields:
                field_obj.widget.attrs['placeholder'] += ' *'
