from django.db import models

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
