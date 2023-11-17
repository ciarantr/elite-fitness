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

    def __init__(self, user, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        self.user = user
        super().__init__(*args, **kwargs)

        placeholders = {field: self.Meta.model._meta.get_field(
            field).verbose_name for field in self.fields}

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'placeholder': placeholders.get(field),
            })
        if self.Meta.model._meta.get_field(field).blank:
            self.fields[field].widget.attrs['placeholder'] += ' (optional)'

    def clean_name(self):
        name = self.cleaned_data.get('name').lower()

        if List.objects.filter(user=self.user, name=name).exists():
            raise ValidationError(
                'You already have a wishlist with this name.')

        return name


class EditWishlistForm(forms.ModelForm):
    """
    Form for editing a wishlist
    """

    class Meta:
        model = List
        fields = ['name', 'description']
        labels = {
            'name': 'Update name',
            'description': 'Update description',
        }
        widgets = {
            'description': Textarea(attrs={'cols': 20, 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        placeholders = {field: self.Meta.model._meta.get_field(
            field).verbose_name for field in self.fields}

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'placeholder': placeholders.get(field),
            })
            if self.Meta.model._meta.get_field(field).blank:
                self.fields[field].widget.attrs['placeholder'] += ' (optional)'

        for field_name, field in self.fields.items():
            field.widget.attrs['id'] = 'id_edit_' + field_name


class AddProductToWishlistForm(forms.Form):
    """
    Form for adding a product to a wishlist
    """

    wishlist = forms.ModelMultipleChoiceField(
        queryset=None,
        label='',
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        self.user = kwargs.pop('user')
        # self.product = kwargs.pop('product')
        super().__init__(*args, **kwargs)
        self.fields['wishlist'].queryset = List.objects.filter(user=self.user)
