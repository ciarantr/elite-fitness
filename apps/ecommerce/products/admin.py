from django.contrib import admin
from django.utils.html import format_html

from .models import (Attribute, Benefit, Brand, Category, Image, KeyBenefit,
                     Product, Variant)


class ImageInline(admin.StackedInline):
    model = Image
    max_num = 1
    fields = ['image', 'display_current_image']
    readonly_fields = ['display_current_image']

    def display_current_image(self, obj):
        if obj.image:  # assuming `image` is your ImageField
            return format_html('<img src="{}" width="150" height="150" />',
                               obj.image.url)
        return "No Image"

    display_current_image.short_description = 'Current Image'


class BenefitInline(admin.StackedInline):
    model = Benefit
    max_num = 3
    extra = 1
    classes = ['collapse']
    verbose_name_plural = 'Product Benefit'


class KeyBenefitInline(admin.StackedInline):
    model = KeyBenefit
    max_num = 6
    extra = 1
    classes = ['collapse']
    verbose_name_plural = 'Product Key Benefit'


# Register your models here.
