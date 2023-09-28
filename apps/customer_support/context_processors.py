# customer support pages
from django.urls import reverse


def support_pages(request):
    """
    Adds customer support pages to the context.
    Reverse() is used to get the URL for each page.
    The Initial url is set in core/urls.py as: support/
    Must have app_name = 'customer_support' in urls.py
    """

    customer_support_pages = [
        {
            "name": "About Us",
            "slug": "about",
        },
        {
            "name": "Contact Us",
            "slug": "contact",
        },
        {
            "name": "FAQs",
            "slug": "faqs",
        },
        {
            "name": "Privacy Policy",
            "slug": "privacy-policy",
        },
        {
            "name": "Shipping & Information",
            "slug": "shipping-and-information",
        },
        {
            "name": "Terms & Conditions",
            "slug": "terms-and-conditions",
        },

    ]

    for page in customer_support_pages:
        page["url"] = reverse(f"customer_support:{page['slug']}")

    context = {
        "customer_support_pages": customer_support_pages,
    }

    return context
