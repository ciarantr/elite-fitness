from django import forms
from django.core.validators import RegexValidator
from django.utils.safestring import mark_safe


class ContactForm(forms.Form):
    """
    Form for the Contact Us page.
    """
    # +()-0-9
    alphanumeric_regex = RegexValidator(
        r'^[0-9+()-]*$',
        mark_safe(f"""Please enter a valid phone number <br>
                  Only numbers, +, (, ), and - are allowed."""
                  )
    )
    alpha_regex = RegexValidator(
        r'^[a-zA-Z]*$',
        mark_safe('Please enter a valid name <br> Only letters are allowed.')
    )

    text_regex = RegexValidator(r'^[a-zA-Z0-9\s,.-]*$',
                                mark_safe(f""" Please enter a valid message
                                          <br> Only alphanumeric, spaces, and 
                                          commas,periods, and dashes are
                                           allowed.""")
                                )

    # Email Validation Regex
    # https://emailregex.com/

    # ^[\w+\-.]+: Matches one or more word characters (\w is equivalent to
    # [a-zA-Z0-9_]) as well as the characters +, -, and . in the local part
    # of the email before the @ symbol.

    # @[a-zA-Z\d\-]+: Matches the @ symbol followed by one or more alphabetic
    # characters, digits, or hyphens in the domain's first-level section.

    # (\.[a-zA-Z\d\-]+)*: Matches zero or more occurrences of a period (.)
    # followed by one or more alphabetic characters, digits, or hyphens in
    # subsequent subdomains.

    # \.[a-zA-Z]+$: Matches the top-level domain (TLD) of the email,
    # ensuring it consists of one or more alphabetic characters.

    email_regex = RegexValidator(
        r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        mark_safe(f"""Invalid email address!
                    <br> Enter a valid email formatted as 'name@domain.com"""
                  )
        ),

    first_name = forms.CharField(
        label='first name',
        max_length=50,
        min_length=2,
        validators=[alpha_regex],
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Name',
        }),
    )

    last_name = forms.CharField(
        label='last name',
        max_length=50,
        min_length=2,
        validators=[alpha_regex],
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Last Name',
        }),
    )

    email = forms.EmailField(
        label='email',
        max_length=100,
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
        }),
    )

    phone_number = forms.CharField(
        label='phone number',
        max_length=20,
        min_length=6,
        validators=[alphanumeric_regex],
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Phone Number',
        }),
    )

    message = forms.CharField(
        label='message',
        max_length=1000,
        min_length=10,
        validators=[text_regex],
        required=True,
        widget=forms.Textarea(attrs={
            'placeholder': 'Message',
            'rows': 5,
            'cols': 20,
        }),
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        # append * to each placeholder if the field is required
        for field in self.fields:
            placeholder = self.fields[field].widget.attrs['placeholder']
            if self.fields[field].required:
                placeholder += ' *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
