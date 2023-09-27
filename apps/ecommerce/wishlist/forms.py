from django import forms
from django.core.exceptions import ValidationError
from django.forms import Textarea

from .models import List


class CreateWishlistForm(forms.ModelForm):
    """
    Form for creating a wishlist
    """

    class Meta:
        model = List
        fields = ['name', 'description']
        widgets = {
            'description': Textarea(attrs={'cols': 20, 'rows': 5})
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True
        placeholders = {field: self.Meta.model._meta.get_field(
            field).verbose_name for field in self.fields}

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'placeholder': placeholders.get(field),
            })
        if self.Meta.model._meta.get_field(field).blank:
            self.fields[field].widget.attrs['placeholder'] += ' (optional)'
        self.fields[field].label = False

    def clean_name(self):
        name = self.cleaned_data.get('name').lower()
        if List.objects.filter(name__iexact=name).exists():
            raise ValidationError('A wishlist with this name already exists.'
                                  ' Please choose another.')
        return name
