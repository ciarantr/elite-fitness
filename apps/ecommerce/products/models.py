from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.ecommerce.products.utils import create_sku, create_slug


class AttributeType(models.TextChoices):  # enum class
    """Attribute type model"""
    COLOR = 'color', 'Color'
    SIZE = 'size', 'Size'
    WEIGHT = 'weight', 'Weight'
    COUNT = 'count', 'Count'


class Attribute(models.Model):
    class Meta:
        verbose_name_plural = 'Product attributes'

    type = models.CharField(max_length=50,
                            verbose_name='Attribute type',
                            choices=AttributeType.choices)

    name = models.CharField(max_length=50,
                            unique=True,
                            verbose_name='Attribute name',
                            help_text='Required. 50 characters or fewer.')

    def __str__(self):
        return f'{self.type} - {self.name}'


# Create your models here.
class Brand(models.Model):
    """Brand model"""

    class Meta:
        verbose_name_plural = 'Brands'
        ordering = ['name']

    name = models.CharField(max_length=50,
                            unique=True,
                            blank=True,
                            verbose_name='Brand name',
                            help_text='Required. 50 characters or fewer.')

    slug = models.SlugField(max_length=100,
                            help_text='Generated automatically on save.',
                            blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Generate slug if it doesn't exist
        if not self.slug:
            self.slug = create_slug(self.name)
        super().save(*args, **kwargs)


class Benefit(models.Model):
    """Product benefit model"""
    product = models.ForeignKey('Product',
                                related_name='benefits',
                                null=True,
                                blank=True,
                                on_delete=models.CASCADE)

    title = models.CharField(max_length=100,
                             null=True,
                             # blank=True,
                             )
    description = models.TextField(max_length=1000,
                                   null=True,
                                   blank=True)

    def __str__(self):
        return self.title


class KeyBenefit(models.Model):
    """Product benefit model"""
    product = models.ForeignKey('Product',
                                related_name='key_benefits',
                                null=True,
                                blank=True,
                                on_delete=models.CASCADE)

    title = models.CharField(max_length=250,
                             null=True,
                             blank=True,
                             )

    def __str__(self):
        return self.title


class Category(models.Model):
    """Category model"""

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    name = models.CharField(max_length=100,
                            unique=True,
                            verbose_name='Category name',
                            help_text='Required. 100 characters or fewer.')

    slug = models.SlugField(
        max_length=150,
        blank=True,
        help_text='Generated automatically on save.',
        unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Generate slug if it doesn't exist
        if not self.slug:
            self.slug = create_slug(self.name)
        super().save(*args, **kwargs)


class BaseProduct(models.Model):
    class Meta:
        abstract = True
        verbose_name_plural = 'Products'
        ordering = ['name']

    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Created on',
                                   editable=False)

    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='Last updated')

    sku = models.CharField(max_length=15,
                           blank=True,
                           help_text='Generated automatically on save.',
                           unique=True)
    slug = models.SlugField(max_length=200,
                            blank=True,
                            help_text='Generated automatically on save.',
                            unique=True)

    description = models.TextField(
        max_length=1000, null=True, blank=True
    )
    name = models.CharField(max_length=150, verbose_name='Product name',
                            unique=True,
                            help_text='Required. 150 characters or fewer.')
    is_active = models.BooleanField(default=True, verbose_name='Active')
    is_reviewed = models.BooleanField(default=False, verbose_name='Reviewed')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def save(self, *args, **kwargs):
        # Generate slug if it doesn't exist
        if not self.slug:
            self.slug = create_slug(self.name)
            self.sku = create_sku(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

