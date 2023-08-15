from django import forms

from apps.ecommerce.orders.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['autofocus'] = True
        placeholders = {field: field.replace("_", " ").title() for field in
                        self.fields}

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'placeholder': placeholders[field],
                'class': 'stripe-style-input'
            })
            self.fields[field].label = False
