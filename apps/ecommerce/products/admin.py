from django.contrib import admin
from django.utils.html import format_html

from .models import (Attribute, Benefit, Brand, Category, Image, KeyBenefit,
                     Product, )


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


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Product admin"""

    # get all variants for a product and create a link for each variant
    def product_variants(self, obj):
        variants = obj.variants.all()
        return format_html(
            '<br>'.join(
                ['<a href="/admin/products/variant/{}/change/">{}</a>'.format(
                    variant.id, variant.name) for variant in variants]))

    inlines = (ImageInline, BenefitInline, KeyBenefitInline,)
    readonly_fields = ['slug',
                       'sku',
                       'created',
                       'updated',
                       'product_variants']

    list_display = ['name',
                    'updated',
                    'brand',
                    'price',
                    'stock',
                    'is_active', 'is_reviewed']

    list_filter = ['is_active',
                   'is_reviewed',
                   'brand',
                   'category',
                   'created', 'updated']

    search_fields = ['name',
                     'sku',
                     'slug',
                     'brand__name', 'category__name']

    filter_horizontal = ['attributes', 'category']

    #  insert category and brand in the Product Details fieldset
    product_fieldset = product_fieldset[:1] + (('Category & Brand', {
        'fields': (
            'category',
            'brand',
        ),
        'classes': ('collapse',),
    }),) + product_fieldset[1:]
    # insert product_variants in the Product Details fieldset
    product_fieldset = product_fieldset[:2] + (('Product Variants', {
        'fields': (
            'product_variants',
        ),
        'classes': ('collapse',),
    }),) + product_fieldset[2:]

    fieldsets = product_fieldset


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    """Attribute admin"""
    list_display = ['type', 'name']

    class Meta:
        model = Attribute


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """Brand admin"""

    def product_count(self, obj):
        products = Product.objects.filter(brand=obj)
        return products.count()

    list_display = ['name', 'product_count', 'slug']
    search_fields = ['name']
    readonly_fields = ['slug']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin"""

    # sum the number of products in a category
    def product_count(self, obj):
        products = Product.objects.filter(category=obj)
        return products.count()

    list_display = ['name', 'product_count', 'slug']
    search_fields = ['name']
    readonly_fields = ['slug']
