import uuid

from django.conf import settings
from django.db import models
from django.db.models import Sum
from django_countries.fields import CountryField

from apps.accounts.models import CustomerProfile
from apps.ecommerce.products.models import Product


def generate_order_number():
    """
    Generate a random, unique order number using UUID
    """
    return uuid.uuid4().hex


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    order_number = models.CharField(max_length=32, unique=True)
    user_profile = models.ForeignKey(CustomerProfile, null=True, blank=True,
                                     on_delete=models.SET_NULL,
                                     related_name='orders')
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country *')
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40)
    street_address1 = models.CharField(max_length=80)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, blank=True, default='')
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES,
                              default='PENDING')

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.line_items.aggregate(Sum('lineitem_total'))[
                               'lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = settings.STANDARD_DELIVERY_COST
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name='line_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='line_items')
    quantity = models.IntegerField(default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the line item total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Order #{self.order.order_number} - SKU {self.product.sku}'
