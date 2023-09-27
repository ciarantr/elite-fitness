from django.db import models

from apps.accounts.models import User
from apps.ecommerce.products.models import Product


class List(models.Model):
    """
    Wish list model
    """
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='wishlist')
    name = models.CharField(max_length=100,
                            unique=True,
                            verbose_name='List name')
    description = models.TextField(max_length=150,
                                   null=True,
                                   blank=True,
                                   verbose_name='List description')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Created on',
                                   editable=False)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'

    def get_all_products(self):
        return self.products.all()
