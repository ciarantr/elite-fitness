from datetime import datetime
from decimal import Decimal

from django.test import TestCase

from apps.ecommerce.products.models import Product
from ..models import Order, OrderLineItem


class OrderModelTest(TestCase):
    """
    Test Order model
    1.Set up a user and Order/Product instance with default values
    2.Test Order model order number is generated & returns a string
    3.Test Order line item model total is calculated correctly
    3.Test Order line item model returns a string with order number & sku
    4.Test Order quantity is updated correctly with order total, delivery cost
    and grand total
    """
    @classmethod
    def setUpTestData(cls):

        Order.objects.create(
            full_name="Test User",
            email="test@example.com",
            phone_number="1234567890",
            country="IE",
            town_or_city="Test City",
            street_address1="Test Street 1",
            street_address2="Test Street 2",
            county="Test County",
        )
        order = Order.objects.get(id=1)

        Product.objects.create(
            name="Test Product",
            description="Test description",
            price=50.50,
            stock=10,
            sku="TESTSKU",
        )
        product = Product.objects.get(id=1)
        OrderLineItem.objects.create(
            order=order,
            product=product,
            quantity=3,
        )

    def test_order_creation(self):
        order = Order.objects.get(id=1)
        self.assertEqual(order.full_name, "Test User")
        self.assertEqual(order.email, "test@example.com")
        self.assertTrue(isinstance(order.date, datetime))
        self.assertEqual(order.status, "PENDING")

    def test_order_repr(self):
        order = Order.objects.get(id=1)
        self.assertEqual(order.__str__(), order.order_number)

    def test_order_update_total(self):
        # Add more items to test update_total method
        order = Order.objects.get(id=1)
        product = Product.objects.get(id=1)

        OrderLineItem.objects.create(
            order=order,
            product=product,
            quantity=2,
        )

        order.update_total()

        # order_total must be price of product * total quantity
        self.assertEqual(round(order.order_total, 2), Decimal(50.50 * 5))

        # as the order total is more than the
        # delivery threshold, delivery cost must be 0
        self.assertEqual(order.delivery_cost, 0)

        # grand_total must be order_total + delivery cost
        self.assertEqual(round(order.grand_total, 2), Decimal(50.50 * 5))

    def test_order_line_item_creation(self):
        line_item = OrderLineItem.objects.get(id=1)
        self.assertEqual(line_item.quantity, 3)
        # round to 2 decimal places to account for floating point errors
        self.assertEqual(round(line_item.lineitem_total, 2),
                         Decimal(50.50 * 3))

    def test_order_line_item_repr(self):
        line_item = OrderLineItem.objects.get(id=1)
        self.assertEqual(line_item.__str__(),
                         f'Order #{line_item.order.order_number}'
                         f' - SKU {line_item.product.sku}')

