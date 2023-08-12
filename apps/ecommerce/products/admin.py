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


product_fieldset = (
    ('Product Details', {
        'fields': (
            'is_active',
            'is_reviewed',
            'name',
            'description',
            'price',
            'stock',
            'attributes',

        )
    }),
    ('Meta Data',
     {
         'fields': (
             'sku',
             'slug',
             'created',
             'updated',
         ),
         'classes': ('collapse',),
     }),

)


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    """Variant admin"""

    # get product brand
    def product_brand(self, obj):
        return obj.product.brand if obj.product.brand else "None"

    def display_product_categories(self, obj):
        return ", ".join(
            [category.name for category in obj.product.category.all()])

    display_product_categories.short_description = 'Product Categories'

    inlines = (ImageInline,)
    filter_horizontal = ['attributes']

    readonly_fields = [
        'slug',
        'sku',
        'product_brand',
        'created',
        'updated',
        'display_product_categories'
    ]

    list_display = [
        'name',
        'product',
        'product_brand',
        'price',
        'stock',
        'is_active',
    ]

    list_filter = [
        'is_active',
        'is_reviewed',
        'product__brand__name',
        'product__category__name',
        'created', 'updated'
    ]

    search_fields = [
        'name',
        'sku',
        'slug',
        'product__name',
        'product__sku',
        'product__slug',
        'product__brand__name',
        'product__category__name'
    ]

    # add product field to fieldsets tuple
    product_fieldset = product_fieldset + (('Related Product', {
        'fields': (
            'product',
            'product_brand',
            'display_product_categories'
        )
    }),)

    fieldsets = product_fieldset


