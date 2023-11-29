from django.test import Client, TestCase

from apps.ecommerce.products.models import Brand, Category, Product


class AllProductsViewTest(TestCase):
    """
    Test the AllProductsView
    1. Test that the view url exists at the desired location
    and returns a 200 response code & uses the correct template
    2. Test that the view returns the correct queryset & context data
    3. Test that the view returns the correct template, context data &
    status code when filtering by brand
    4. Test that the view returns the correct template, context data &
    status code when filtering by category
    """

    def setUp(self):
        self.client = Client()
        self.brand = Brand.objects.create(name="Test Brand")
        self.category = Category.objects.create(name="Test Category")
        self.product = Product.objects.create(
            name="Test Product",
            brand=self.brand,
            price=10.00,
            stock=10,
        )
        self.product.category.add(self.category)

    def test_get_context_data(self):
        # Test that the view url exists at the desired location
        # and returns a 200 response code & uses the correct template
        response = self.client.get('/products/')

        # Ensure status code 200 i.e., OK
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')

    def test_get_queryset(self):
        # Test that the view returns the correct queryset by filtering
        response = self.client.get('/products/?q=test')
        products = response.context_data['products']

        #  check that the product is in the queryset
        self.assertIn(self.product, products)

    def test_get_queryset_sort_by_brand(self):
        # Test that the view returns the correct queryset by filtering brand
        response = self.client.get(f'/products/?brand={self.brand.slug}')
        products = response.context_data['products']

        #  check that the product is in the queryset
        self.assertIn(self.product, products)

    def test_get_queryset_sort_by_category(self):
        # Test that the view returns the correct queryset by filtering category
        response = self.client.get(f'/products/?category={self.category.slug}')
        products = response.context_data['products']

        #  check that the product is in the queryset
        self.assertIn(self.product, products)

    def test_get_queryset_sort_by_brand_fail(self):
        # Test that the view does not return the product when
        # filtering by the wrong brand & returns a 404
        response = self.client.get('/products/?test&brand=wrong-brand')
        self.assertEqual(response.status_code, 404)

    def test_get_queryset_sort_by_category_fail(self):
        # Test that the view does not return the product when
        # filtering by the wrong category & returns a 404
        response = self.client.get('/products/?test&category=wrong-category')
        self.assertEqual(response.status_code, 404)


class ProductDetailViewTest(TestCase):
    """
    Test the ProductDetailView
    1. Test that the view url exists at the desired location
    and returns a 200 response code & uses the correct template
    2. Test that the view returns the correct context data
    """

    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(
            name="Test Product",
            price=10.00,
            stock=10,
        )

    def test_get_context_data(self):
        response = self.client.get('/products/{self.product.slug}/')

        # Ensure status code 200 i.e., OK
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_detail.html')
        self.assertIn('product', response.context_data)
        self.assertEqual(response.context_data['product'], self.product)

    def test_get_context_data_fail(self):
        response = self.client.get('/products/wrong-slug/')

        # Ensure status code 404 i.e., NOT FOUND
        self.assertEqual(response.status_code, 404)
