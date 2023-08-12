import random
import re
import string

from django.utils.text import slugify


def create_slug(original_string):
    # Remove non-Unicode characters
    clean_string = re.sub(r'[^\x00-\x7F]+', '', original_string)
    # Use Django's slugify function to create URL-friendly string
    return slugify(clean_string)


def create_sku(name):
    """Generate SKU"""
    alphabetic_chars = ''.join(filter(str.isalpha, name))[:3].upper()
    random_numbers = ''.join(random.choices(string.digits, k=6))
    return f"{alphabetic_chars}-{random_numbers}"
