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
