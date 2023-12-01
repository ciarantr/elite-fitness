# Testing 🧪

**Readme navigation links: 🧭**
- [📕 View Readme documentation](./README.md)
- [🎨 View Design documentation](./DESIGN.md#ux--ui-)
- [🚀 View Deployment documentation (Local & Production)](./DEPLOYMENT.md#deployment-)
- [✨ View Features documentation](./FEATURES.md#features-)
- [🔓 View Security documentation](./SECURITY.md#security-)
---

The testing documentation offers a thorough walkthrough of the website's testing procedures and functionality.
It includes screenshots from various testing stages for visual guidance.
This essential resource assists individuals looking to delve deeper into the testing aspects of the website.
It's arranged into multiple sections, each emphasising a specific testing procedure or function.
The sections included are:


- [Code Validation](#code-validation)
  - [HTML](#html)
  - [CSS](#css)
  - [JavaScript](#javascript)
  - [Python](#python)
- [Browser Compatibility](#browser-compatibility)
- [Responsiveness](#responsiveness)
- [Lighthouse Audit](#lighthouse-audit)
- [Defensive Programming](#defensive-programming)
- [User Story Testing](#user-story-testing)
- [Automated Testing](#automated-testing)
  - [Python (Unit Testing)](#python-unit-testing)
    - [Unit Test Issues](#unit-test-issues)
- [Bugs](#bugs)
  - [GitHub **Issues**](#github-issues)
- [Unfixed Bugs](#unfixed-bugs)

## Code Validation

For Code Validation, I have used the following tools: 🛠️

- [W3C HTML Validator](https://validator.w3.org) Validates HTML code
- [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) Validates CSS code
- [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) Validates Python code
- [JShint JavaScript Validator](https://jshint.com) Validates JavaScript code
- [Eslint](https://eslint.org) for JavaScript linting
- [Ruff python linter](https://pypi.org/project/ruff/) for Python linting & formatting
- [Pycharm Code Inspections](https://www.pylint.org) for Python linting (use pep8 style guide)

### HTML

I have employed the W3C Markup Validation Service, which is the recommended tool for validating all of my HTML files.
The validation process ensures accuracy and adherence to industry standards. To access the validator,
please visit the following URL: [W3C Markup Validation Service](https://validator.w3.org).

> [!IMPORTANT]
>
> **HTML validation info messages**
>
> I utilised the prettier formatter to properly format the HTML, which leads to the inclusion of trailing slashes at the
> conclusion of tags. It is important to note that while this may prompt an informational message in HTML validation
> reports, it does not constitute an error.

| Page                                 | W3C URL                                                                                                                                 | Screenshot                                                                           | Notes                                                           |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| About us                             | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Felite-fitness-f6b7c0ead930.herokuapp.com%2Fsupport%2Fabout%2F)                     | ![screenshot](../docs/testing/validation/html/about-us-page.png)                     | No warnings                                                     |
| Contact Us                           | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Felite-fitness-f6b7c0ead930.herokuapp.com%2Fsupport%2Fcontact%2F)                   | ![screenshot](../docs/testing/validation/html/contact-us-page.png)                   | No warnings                                                     |
| FAQS                                 | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Felite-fitness-f6b7c0ead930.herokuapp.com%2Fsupport%2Ffaqs%2F)                      | ![screenshot](../docs/testing/validation/html/faqs-page.png)                         | No warnings                                                     |
| Privacy Policy                       | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Felite-fitness-f6b7c0ead930.herokuapp.com%2Fsupport%2Fprivacy-policy%2F)            | ![screenshot](../docs/testing/validation/html/privacy-policy-page.png)               | No warnings                                                     |
| Products                             | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Felite-fitness-f6b7c0ead930.herokuapp.com%2Fproducts%2F)                            | ![screenshot](../docs/testing/validation/html/products-page.png)                     | No warnings                                                     |
| Product Detail                       | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Felite-fitness-f6b7c0ead930.herokuapp.com%2Fproducts%2Fdaily-essentials-for-men%2F) | ![screenshot](../docs/testing/validation/html/product-detail-page.png)               | No warnings                                                     |
| Profile Account                      | Validated by input                                                                                                                      | ![screenshot](../docs/testing/validation/html/profile-page.png)                      | No warnings                                                     |
| Profile Account Delivery Information | Validated by input                                                                                                                      | ![screenshot](../docs/testing/validation/html/profile-delivery-information-page.png) | Error fixed on commit: b7a681d334ea03bb01ecee84cb5f1b5faa403d9c |
| Profile Account Orders               | Validated by input                                                                                                                      | ![screenshot](../docs/testing/validation/html/profile-orders-page.png)               | No warnings                                                     |

### CSS

I have employed the CSS Jigsaw Validator, which is the recommended tool for validating all of my CSS files.
The validation process ensures accuracy and adherence to industry standards. To access the validator,
please visit the following URL: [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator).

> [!IMPORTANT]
>
> **CSS validation errors**:
>
> This project uses [Tailwind CSS](https://tailwindcss.com), which is a utility-first CSS framework. As such,
> the css is compiled & minified into one css file with [Vite](https://vitejs.dev).
> CSS validation has returned 56 CSS parsing errors. This issue is a result of the final ccs build using Tailwindcss.
> The maintainer of TailwindCSS has discussed this issue and provided a solution;
> however, the recommended fix cannot be used as it is causing issues with the styles used within the application.
> [Remove --tw- variables from universal selector #7317](https://github.com/tailwindlabs/tailwindcss/discussions/7317)

| File                                                 | Jigsaw URL                           | Screenshot                                                                  | Notes                                                                                          |
|------------------------------------------------------|--------------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| main.css  [Navigate to file](../static/css/main.css) | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Felite-fitness-f6b7c0ead930.herokuapp.com&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![Screenshot](../docs/testing/validation/css/W3C-CSS-Validator-results.png) | Fail: (61) Errors. These errors are due to the --tw- variables from universal mentioned above. |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files
along with [ESLint](https://eslint.org) for JavaScript linting.

If using modern JavaScript (ES6) methods, then make sure to include the following
line at the very top of every single JavaScript file (this should remain in your files for submission):

> [!note]
> 
> **ESLint Configuration**
> 
> ```/* jshint esversion: 11 */``` & ```/* jshint asi: true */``` have been added to the top of each JS file for assessment purposes. This allows the JShint validator to recognize modern ES6 methods, such as:
`let`, `const`, `template literals`, `arrow functions (=>)`, etc.

| File                                                                                                                | Screenshot                                                                                                        | Notes           |
|---------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-----------------|
| main.js [Navigate to file](../static/js/main.js)                                                                    | ![screenshot](../docs/testing/validation/js/JSHint-JavaScript-Code-Quality-Tool-main.js.png)                      | Pass: No Errors |
| stripe.js [Navigate to file](../static/js/stripe.js)                                                                | ![screenshot](../docs/testing/validation/js/JSHint-JavaScript-Code-Quality-Tool-stripe.js.png)                    | Pass: No Errors |
| wishlist.js  [Navigate to file](../static/js/wishlist.js)                                                           | ![screenshot](../docs/testing/validation/js/JSHint-JavaScript-Code-Quality-Tool-main.js.png)                      | Pass: No Errors |
| wishlist_append_to_dialog.js  [Navigate to file](../apps/ecommerce/wishlist/static/js/wishlist_append_to_dialog.js) | ![screenshot](../docs/testing/validation/js/JSHint-JavaScript-Code-Quality-Tool-wishlist_append_to_dialog.js.png) | Pass: No Errors |
| Build file main.js Located in ~/static/dist/ directory                                                              | ![screenshot](../docs/testing/validation/js/JSHint-JavaScript-Code-Quality-Tool-build-main.js.png)                | Pass: No Errors |
| Build file stripe.js Located in ~/static/dist/ directory                                                            | ![screenshot](../docs/testing/validation/js/JSHint-JavaScript-Code-Quality-Tool-build-stripe.js.png)              | Pass: No Errors |
| Build file wishlist.js Located in ~/static/dist/ directory                                                          | ![screenshot](../docs/testing/validation/js/JSHint-JavaScript-Code-Quality-Tool-build-wishlist.js.png)            | Pass: No Errors |

### Python

I have utilised the [Ruff Python linter](https://astral.sh/ruff)
to validate and format all of my Python files according to the PEP8 standards.
This was done in conjunction with the [PyCharm IDE](https://www.jetbrains.com/pycharm/).
Additionally,
I employed the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com)
to validate all files excluding diregtories in the **tests** & **migrations** folders, as well as `__init__.py` files.

>[!important]
> 
> **Testing Python Code**
> 
> Folders excluded from testing include: **tests** & **migrations**.
> Files excluded from testing include: `__init__.py` files.

| Status | Filename                                      | Result Text                |
|--------|-----------------------------------------------|----------------------------|
| Pass   | ./apps/home/apps.py                           | All clear, no errors found |
| Pass   | ./apps/home/urls.py                           | All clear, no errors found |
| Pass   | ./apps/home/views.py                          | All clear, no errors found |
| Pass   | ./apps/ecommerce/products/models.py           | All clear, no errors found |
| Pass   | ./apps/ecommerce/products/apps.py             | All clear, no errors found |
| Pass   | ./apps/ecommerce/products/admin.py            | All clear, no errors found |
| Pass   | ./apps/ecommerce/products/utils.py            | All clear, no errors found |
| Pass   | ./apps/ecommerce/products/urls.py             | All clear, no errors found |
| Pass   | ./apps/ecommerce/products/views.py            | All clear, no errors found |
| Pass   | ./apps/ecommerce/checkout/signals.py          | All clear, no errors found |
| Pass   | ./apps/ecommerce/checkout/apps.py             | All clear, no errors found |
| Pass   | ./apps/ecommerce/checkout/webhook_handler.py  | All clear, no errors found |
| Pass   | ./apps/ecommerce/checkout/webhooks.py         | All clear, no errors found |
| Pass   | ./apps/ecommerce/checkout/urls.py             | All clear, no errors found |
| Pass   | ./apps/ecommerce/checkout/views.py            | All clear, no errors found |
| Pass   | ./apps/ecommerce/cart/apps.py                 | All clear, no errors found |
| Pass   | ./apps/ecommerce/cart/context_processors.py   | All clear, no errors found |
| Pass   | ./apps/ecommerce/cart/urls.py                 | All clear, no errors found |
| Pass   | ./apps/ecommerce/cart/views.py                | All clear, no errors found |
| Pass   | ./apps/ecommerce/orders/models.py             | All clear, no errors found |
| Pass   | ./apps/ecommerce/orders/apps.py               | All clear, no errors found |
| Pass   | ./apps/ecommerce/orders/forms.py              | All clear, no errors found |
| Pass   | ./apps/ecommerce/orders/admin.py              | All clear, no errors found |
| Pass   | ./apps/ecommerce/orders/tests.py              | All clear, no errors found |
| Pass   | ./apps/ecommerce/orders/urls.py               | All clear, no errors found |
| Pass   | ./apps/ecommerce/orders/views.py              | All clear, no errors found |
| Pass   | ./apps/ecommerce/wishlist/models.py           | All clear, no errors found |
| Pass   | ./apps/ecommerce/wishlist/apps.py             | All clear, no errors found |
| Pass   | ./apps/ecommerce/wishlist/forms.py            | All clear, no errors found |
| Pass   | ./apps/ecommerce/wishlist/urls.py             | All clear, no errors found |
| Pass   | ./apps/ecommerce/wishlist/views.py            | All clear, no errors found |
| Pass   | ./apps/customer_support/apps.py               | All clear, no errors found |
| Pass   | ./apps/customer_support/forms.py              | All clear, no errors found |
| Pass   | ./apps/customer_support/context_processors.py | All clear, no errors found |
| Pass   | ./apps/customer_support/urls.py               | All clear, no errors found |
| Pass   | ./apps/customer_support/views.py              | All clear, no errors found |
| Pass   | ./apps/subscriptions/models.py                | All clear, no errors found |
| Pass   | ./apps/subscriptions/apps.py                  | All clear, no errors found |
| Pass   | ./apps/subscriptions/forms.py                 | All clear, no errors found |
| Pass   | ./apps/subscriptions/admin.py                 | All clear, no errors found |
| Pass   | ./apps/subscriptions/urls.py                  | All clear, no errors found |
| Pass   | ./apps/subscriptions/views.py                 | All clear, no errors found |
| Pass   | ./apps/accounts/signals.py                    | All clear, no errors found |
| Pass   | ./apps/accounts/models.py                     | All clear, no errors found |
| Pass   | ./apps/accounts/apps.py                       | All clear, no errors found |
| Pass   | ./apps/accounts/forms.py                      | All clear, no errors found |
| Pass   | ./apps/accounts/admin.py                      | All clear, no errors found |
| Pass   | ./apps/accounts/urls.py                       | All clear, no errors found |
| Pass   | ./apps/accounts/views.py                      | All clear, no errors found |
| Pass   | ./apps/marketing/models.py                    | All clear, no errors found |
| Pass   | ./apps/marketing/apps.py                      | All clear, no errors found |
| Pass   | ./apps/marketing/admin.py                     | All clear, no errors found |

> [!NOTE]
> 
> **Extend Python Validation screenshots and links**
> 
<details>
  <summary>
    <strong>View detailed testing with screenshots with CI Python Linter links</strong>
  </summary>

| Status | Filename                                      | Screenshot                                                                                    | Result                     | CI URL                                                                                                                                          |
|--------|-----------------------------------------------|-----------------------------------------------------------------------------------------------|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Pass   | ./apps/home/apps.py                           | ![screenshot](../docs/testing/ci-pep8-linter/apps-home-apps.py.png)                           | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/home/apps.py)                           |
| Pass   | ./apps/home/urls.py                           | ![screenshot](../docs/testing/ci-pep8-linter/apps-home-urls.py.png)                           | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/home/urls.py)                           |
| Pass   | ./apps/home/views.py                          | ![screenshot](../docs/testing/ci-pep8-linter/apps-home-views.py.png)                          | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/home/views.py)                          |
| Pass   | ./apps/ecommerce/products/models.py           | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-products-models.py.png)           | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/products/models.py)           |
| Pass   | ./apps/ecommerce/products/apps.py             | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-products-apps.py.png)             | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/products/apps.py)             |
| Pass   | ./apps/ecommerce/products/admin.py            | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-products-admin.py.png)            | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/products/admin.py)            |
| Pass   | ./apps/ecommerce/products/utils.py            | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-products-utils.py.png)            | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/products/utils.py)            |
| Pass   | ./apps/ecommerce/products/urls.py             | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-products-urls.py.png)             | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/products/urls.py)             |
| Pass   | ./apps/ecommerce/products/views.py            | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-products-views.py.png)            | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/products/views.py)            |
| Pass   | ./apps/ecommerce/checkout/signals.py          | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-checkout-signals.py.png)          | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/checkout/signals.py)          |
| Pass   | ./apps/ecommerce/checkout/apps.py             | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-checkout-apps.py.png)             | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/checkout/apps.py)             |
| Pass   | ./apps/ecommerce/checkout/webhook_handler.py  | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-checkout-webhook_handler.py.png)  | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/checkout/webhook_handler.py)  |
| Pass   | ./apps/ecommerce/checkout/webhooks.py         | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-checkout-webhooks.py.png)         | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/checkout/webhooks.py)         |
| Pass   | ./apps/ecommerce/checkout/urls.py             | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-checkout-urls.py.png)             | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/checkout/urls.py)             |
| Pass   | ./apps/ecommerce/checkout/views.py            | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-checkout-views.py.png)            | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/checkout/views.py)            |
| Pass   | ./apps/ecommerce/cart/apps.py                 | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-cart-apps.py.png)                 | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/cart/apps.py)                 |
| Pass   | ./apps/ecommerce/cart/context_processors.py   | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-cart-context_processors.py.png)   | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/cart/context_processors.py)   |
| Pass   | ./apps/ecommerce/cart/urls.py                 | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-cart-urls.py.png)                 | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/cart/urls.py)                 |
| Pass   | ./apps/ecommerce/cart/views.py                | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-cart-views.py.png)                | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/cart/views.py)                |
| Pass   | ./apps/ecommerce/orders/models.py             | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-orders-models.py.png)             | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/orders/models.py)             |
| Pass   | ./apps/ecommerce/orders/apps.py               | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-orders-apps.py.png)               | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/orders/apps.py)               |
| Pass   | ./apps/ecommerce/orders/forms.py              | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-orders-forms.py.png)              | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/orders/forms.py)              |
| Pass   | ./apps/ecommerce/orders/admin.py              | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-orders-admin.py.png)              | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/orders/admin.py)              |
| Pass   | ./apps/ecommerce/orders/tests.py              | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-orders-tests.py.png)              | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/orders/tests.py)              |
| Pass   | ./apps/ecommerce/orders/urls.py               | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-orders-urls.py.png)               | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/orders/urls.py)               |
| Pass   | ./apps/ecommerce/orders/views.py              | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-orders-views.py.png)              | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/orders/views.py)              |
| Pass   | ./apps/ecommerce/wishlist/models.py           | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-wishlist-models.py.png)           | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/wishlist/models.py)           |
| Pass   | ./apps/ecommerce/wishlist/apps.py             | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-wishlist-apps.py.png)             | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/wishlist/apps.py)             |
| Pass   | ./apps/ecommerce/wishlist/forms.py            | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-wishlist-forms.py.png)            | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/wishlist/forms.py)            |
| Pass   | ./apps/ecommerce/wishlist/urls.py             | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-wishlist-urls.py.png)             | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/wishlist/urls.py)             |
| Pass   | ./apps/ecommerce/wishlist/views.py            | ![screenshot](../docs/testing/ci-pep8-linter/apps-ecommerce-wishlist-views.py.png)            | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/ecommerce/wishlist/views.py)            |
| Pass   | ./apps/customer_support/apps.py               | ![screenshot](../docs/testing/ci-pep8-linter/apps-customer_support-apps.py.png)               | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/customer_support/apps.py)               |
| Pass   | ./apps/customer_support/forms.py              | ![screenshot](../docs/testing/ci-pep8-linter/apps-customer_support-forms.py.png)              | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/customer_support/forms.py)              |
| Pass   | ./apps/customer_support/context_processors.py | ![screenshot](../docs/testing/ci-pep8-linter/apps-customer_support-context_processors.py.png) | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/customer_support/context_processors.py) |
| Pass   | ./apps/customer_support/urls.py               | ![screenshot](../docs/testing/ci-pep8-linter/apps-customer_support-urls.py.png)               | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/customer_support/urls.py)               |
| Pass   | ./apps/customer_support/views.py              | ![screenshot](../docs/testing/ci-pep8-linter/apps-customer_support-views.py.png)              | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/customer_support/views.py)              |
| Pass   | ./apps/subscriptions/models.py                | ![screenshot](../docs/testing/ci-pep8-linter/apps-subscriptions-models.py.png)                | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/subscriptions/models.py)                |
| Pass   | ./apps/subscriptions/apps.py                  | ![screenshot](../docs/testing/ci-pep8-linter/apps-subscriptions-apps.py.png)                  | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/subscriptions/apps.py)                  |
| Pass   | ./apps/subscriptions/forms.py                 | ![screenshot](../docs/testing/ci-pep8-linter/apps-subscriptions-forms.py.png)                 | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/subscriptions/forms.py)                 |
| Pass   | ./apps/subscriptions/admin.py                 | ![screenshot](../docs/testing/ci-pep8-linter/apps-subscriptions-admin.py.png)                 | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/subscriptions/admin.py)                 |
| Pass   | ./apps/subscriptions/urls.py                  | ![screenshot](../docs/testing/ci-pep8-linter/apps-subscriptions-urls.py.png)                  | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/subscriptions/urls.py)                  |
| Pass   | ./apps/subscriptions/views.py                 | ![screenshot](../docs/testing/ci-pep8-linter/apps-subscriptions-views.py.png)                 | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/subscriptions/views.py)                 |
| Pass   | ./apps/accounts/signals.py                    | ![screenshot](../docs/testing/ci-pep8-linter/apps-accounts-signals.py.png)                    | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/accounts/signals.py)                    |
| Pass   | ./apps/accounts/models.py                     | ![screenshot](../docs/testing/ci-pep8-linter/apps-accounts-models.py.png)                     | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/accounts/models.py)                     |
| Pass   | ./apps/accounts/apps.py                       | ![screenshot](../docs/testing/ci-pep8-linter/apps-accounts-apps.py.png)                       | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/accounts/apps.py)                       |
| Pass   | ./apps/accounts/forms.py                      | ![screenshot](../docs/testing/ci-pep8-linter/apps-accounts-forms.py.png)                      | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/accounts/forms.py)                      |
| Pass   | ./apps/accounts/admin.py                      | ![screenshot](../docs/testing/ci-pep8-linter/apps-accounts-admin.py.png)                      | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/accounts/admin.py)                      |
| Pass   | ./apps/accounts/urls.py                       | ![screenshot](../docs/testing/ci-pep8-linter/apps-accounts-urls.py.png)                       | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/accounts/urls.py)                       |
| Pass   | ./apps/accounts/views.py                      | ![screenshot](../docs/testing/ci-pep8-linter/apps-accounts-views.py.png)                      | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/accounts/views.py)                      |
| Pass   | ./apps/marketing/models.py                    | ![screenshot](../docs/testing/ci-pep8-linter/apps-marketing-models.py.png)                    | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/marketing/models.py)                    |
| Pass   | ./apps/marketing/apps.py                      | ![screenshot](../docs/testing/ci-pep8-linter/apps-marketing-apps.py.png)                      | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/marketing/apps.py)                      |
| Pass   | ./apps/marketing/admin.py                     | ![screenshot](../docs/testing/ci-pep8-linter/apps-marketing-admin.py.png)                     | All clear, no errors found | [Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ciaran-io/elite-fitness/main/apps/marketing/admin.py)                     |

</details>

> [!IMPORTANT]
> 
> **Django settings.py**
> 
> The Django settings.py file comes with 4 lines that are quite long, and will throw the `E501 line too long` error.
This is default behavior, but can be fixed by adding `# noqa` to the end of those lines.

```python
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa
    },
]
```

## Browser Compatibility

> [!note]
> 
> **Browser Screenshots**
> 
> Screenshots of the deployed project on various browsers can be found in the [docs/testing/browser-testing](../docs/testing/browser-testing) directory.
> Due to the large number of screenshots,
> the browsers have been categorized based on their types
> and can be accessed in the dropdown menu below `view detailed screenshots`.
> Nearly all pages have been tested on mobile & desktop in Chrome, Firefox & Safari.

I have tested my deployed project on multiple browsers to check for compatibility issues. The browsers tested were:

- [Chrome](https://www.google.com/chrome) Version 121.0.6115.2 (Official Build) dev (arm64)

<details>
  <summary>
    <strong>View detailed screenshots for Chrome</strong>
  </summary>

| Page                                 | Device (mobile)                                                                                    | Device (desktop)                                                                                    | Notes             |
|--------------------------------------|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-------------------|
| About                                | ![screenshot](../docs/testing/browser-testing/chrome/about-mobile.png)                             | ![screenshot](../docs/testing/browser-testing/chrome/about-desktop.png)                             | Works as expected |
| Account New User Verify              | ![screenshot](../docs/testing/browser-testing/chrome/account-new-user-mobile.png)                  | ![screenshot](../docs/testing/browser-testing/chrome/account-new-user-desktop.png)                  | Works as expected |
| Account Profile                      | ![screenshot](../docs/testing/browser-testing/chrome/account-profile-mobile.png)                   | ![screenshot](../docs/testing/browser-testing/chrome/account-profile-desktop.png)                   | Works as expected |
| Account Profile Delivery Information | ![screenshot](../docs/testing/browser-testing/chrome/account-profile-order-information-mobile.png) | ![screenshot](../docs/testing/browser-testing/chrome/account-profile-order-information-desktop.png) | Works as expected |
| Account Profile Orders No Auth       | ![screenshot](../docs/testing/browser-testing/chrome/account-order-no-auth-mobile.png)             | ![screenshot](../docs/testing/browser-testing/chrome/account-order-no-auth-desktop.png)             | Works as expected |
| Cart Preview                         | NA                                                                                                 | ![screenshot](../docs/testing/browser-testing/chrome/cart-preview.png)                              | Works as expected |
| Checkout                             | ![screenshot](../docs/testing/browser-testing/chrome/checkout-mobile.png)                          | ![screenshot](../docs/testing/browser-testing/chrome/checkout-desktop.png)                          | Works as expected |
| Contact                              | ![screenshot](../docs/testing/browser-testing/chrome/contact-mobile.png)                           | ![screenshot](../docs/testing/browser-testing/chrome/contact-desktop.png)                           | Works as expected |
| FAQS                                 | ![screenshot](../docs/testing/browser-testing/chrome/faqs-mobile.png)                              | ![screenshot](../docs/testing/browser-testing/chrome/faqs-desktop.png)                              | Works as expected |
| Home                                 | ![screenshot](../docs/testing/browser-testing/chrome/home-mobile.png)                              | ![screenshot](../docs/testing/browser-testing/chrome/home-desktop.png)                              | Works as expected |
| Home Menu Open                       | ![screenshot](../docs/testing/browser-testing/chrome/home-menu-open-mobile.png)                    | ![screenshot](../docs/testing/browser-testing/chrome/home-menu-open-desktop.png)                    | Works as expected |
| Order Confirmation                   | ![screenshot](../docs/testing/browser-testing/chrome/order-complete-mobile.png)                    | ![screenshot](../docs/testing/browser-testing/chrome/order-complete-desktop.png)                    | Works as expected |
| Privacy                              | ![screenshot](../docs/testing/browser-testing/chrome/privacy-mobile.png)                           | ![screenshot](../docs/testing/browser-testing/chrome/privacy-desktop.png)                           | Works as expected |
| Product To Wishlist                  | ![screenshot](../docs/testing/browser-testing/chrome/product-detail-wishlist-mobile.png)           | ![screenshot](../docs/testing/browser-testing/chrome/product-detail-wishlist-desktop.png)           | Works as expected |
| Products                             | ![screenshot](../docs/testing/browser-testing/chrome/products-mobile.png)                          | ![screenshot](../docs/testing/browser-testing/chrome/products-desktop.png)                          | Works as expected |
| Products Detailed                    | ![screenshot](../docs/testing/browser-testing/chrome/product-detail-mobile.png)                    | ![screenshot](../docs/testing/browser-testing/chrome/product-detail-desktop.png)                    | Works as expected |
| Register                             | ![screenshot](../docs/testing/browser-testing/chrome/register-mobile.png)                          | ![screenshot](../docs/testing/browser-testing/chrome/register-desktop.png)                          | Works as expected |
| Register Confirmation Email          | ![screenshot](../docs/testing/browser-testing/chrome/register-confirmation-email.png)              | NA                                                                                                  | Works as expected |
| Shipping & Information               | ![screenshot](../docs/testing/browser-testing/chrome/shipping-and-information-mobile.png)          | ![screenshot](../docs/testing/browser-testing/chrome/shipping-and-information-desktop.png)          | Works as expected |
| Shopping Cart                        | ![screenshot](../docs/testing/browser-testing/chrome/shopping-cart-mobile.png)                     | ![screenshot](../docs/testing/browser-testing/chrome/shopping-cart-desktop.png)                     | Works as expected |
| Subscription Email                   | ![screenshot](../docs/testing/browser-testing/firefox/subscription-email.png)                      | NA                                                                                                  | Works as expected |
| Subscription Complete                | ![screenshot](../docs/testing/browser-testing/chrome/subscription-confirm-mobile.png)              | ![screenshot](../docs/testing/browser-testing/chrome/subscription-confirm-desktop.png)              | Works as expected |
| Terms & Conditions                   | ![screenshot](../docs/testing/browser-testing/chrome/terms-and-conditions-mobile.png)              | ![screenshot](../docs/testing/browser-testing/chrome/terms-and-conditions-desktop.png)              | Works as expected |
| wishlist                             | ![screenshot](../docs/testing/browser-testing/chrome/wishlist-mobile.png)                          | ![screenshot](../docs/testing/browser-testing/chrome/wishlist-desktop.png)                          | Works as expected |
| wishlist Create                      | ![screenshot](../docs/testing/browser-testing/chrome/wishlist-create-mobile.png)                   | ![screenshot](../docs/testing/browser-testing/chrome/wishlist-create-desktop.png)                   | Works as expected |
| wishlist   Delete                    | ![screenshot](../docs/testing/browser-testing/chrome/wishlist-delete-mobile.png)                   | ![screenshot](../docs/testing/browser-testing/chrome/wishlist-delete-desktop.png)                   | Works as expected |
| wishlist   Edit                      | ![screenshot](../docs/testing/browser-testing/chrome/wishlist-edit-mobile.png)                     | ![screenshot](../docs/testing/browser-testing/chrome/wishlist-edit-desktop.png)                     | Works as expected |
| 404 Not Found                        | ![screenshot](../docs/testing/browser-testing/chrome/404-mobile.png)                               | ![screenshot](../docs/testing/browser-testing/chrome/404-desktop.png)                               | Works as expected |

</details>


- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer) Version 121.056 (64-bit)

<details>
  <summary>
    <strong>View detailed screenshots for Firefox</strong>
  </summary>

| Browser                              | Device (mobile)                                                                                     | Device (desktop)                                                                                     | Notes             |
|--------------------------------------|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-------------------|
| About                                | ![screenshot](../docs/testing/browser-testing/firefox/about-mobile.png)                             | ![screenshot](../docs/testing/browser-testing/firefox/about-desktop.png)                             | Works as expected |
| Account Profile                      | ![screenshot](../docs/testing/browser-testing/firefox/account-profile-mobile.png)                   | ![screenshot](../docs/testing/browser-testing/firefox/account-profile-desktop.png)                   | Works as expected |
| Account Profile Delivery Information | ![screenshot](../docs/testing/browser-testing/firefox/account-profile-order-information-mobile.png) | ![screenshot](../docs/testing/browser-testing/firefox/account-profile-order-information-desktop.png) | Works as expected |
| Account Profile  Past Orders         | ![screenshot](../docs/testing/browser-testing/firefox/account-profile-mobile.png)                   | ![screenshot](../docs/testing/browser-testing/firefox/account-profile-desktop.png)                   | Works as expected |
| Cart Preview                         | NA                                                                                                  | ![screenshot](../docs/testing/browser-testing/firefox/cart-preview-desktop.png)                      | Works as expected |
| Checkout                             | ![screenshot](../docs/testing/browser-testing/firefox/checkout-mobile.png)                          | ![screenshot](../docs/testing/browser-testing/firefox/checkout-desktop.png)                          | Works as expected |
| Contact                              | ![screenshot](../docs/testing/browser-testing/firefox/contact-mobile.png)                           | ![screenshot](../docs/testing/browser-testing/firefox/contact-desktop.png)                           | Works as expected |
| FAQS                                 | ![screenshot](../docs/testing/browser-testing/firefox/faqs-mobile.png)                              | ![screenshot](../docs/testing/browser-testing/firefox/faqs-desktop.png)                              | Works as expected |
| Home                                 | ![screenshot](../docs/testing/browser-testing/firefox/home-mobile.png)                              | ![screenshot](../docs/testing/browser-testing/firefox/home-desktop.png)                              | Works as expected |
| Home Menu Open                       | ![screenshot](../docs/testing/browser-testing/firefox/home-mobile-menu-open.png)                    | ![screenshot](../docs/testing/browser-testing/firefox/home-menu-open-desktop.png)                    | Works as expected |
| Login                                | ![screenshot](../docs/testing/browser-testing/firefox/login-mobile.png)                             | ![screenshot](../docs/testing/browser-testing/firefox/login-desktop.png)                             | Works as expected |
| Order Complete                       | ![screenshot](../docs/testing/browser-testing/firefox/order-complete-mobile.png)                    | ![screenshot](../docs/testing/browser-testing/firefox/order-complete-desktop.png)                    | Works as expected |
| Order Summary                        | ![screenshot](../docs/testing/browser-testing/firefox/order-summary-mobile.png)                     | ![screenshot](../docs/testing/browser-testing/firefox/order-summary-desktop.png)                     | Works as expected |
| Privacy                              | ![screenshot](../docs/testing/browser-testing/firefox/privacy-policy-mobile.png)                    | ![screenshot](../docs/testing/browser-testing/firefox/privacy-policy-desktop.png)                    | Works as expected |
| Product Add To Wishlist              | ![screenshot](../docs/testing/browser-testing/firefox/product-detail-wishlist-mobile.png)           | ![screenshot](../docs/testing/browser-testing/firefox/product-detail-wishlist-desktop.png)           | Works as expected |
| Products All                         | ![screenshot](../docs/testing/browser-testing/firefox/products-mobile.png)                          | ![screenshot](../docs/testing/browser-testing/firefox/products-desktop.png)                          | Works as expected |
| Register                             | ![screenshot](../docs/testing/browser-testing/firefox/register-mobile.png)                          | ![screenshot](../docs/testing/browser-testing/firefox/register-desktop.png)                          | Works as expected |
| Shipping Information                 | ![screenshot](../docs/testing/browser-testing/firefox/shipping-information-mobile.png)              | ![screenshot](../docs/testing/browser-testing/firefox/shipping-information-desktop.png)              | Works as expected |
| Shopping Cart                        | ![screenshot](../docs/testing/browser-testing/firefox/shopping-cart-mobile.png)                     | ![screenshot](../docs/testing/browser-testing/firefox/shopping-cart-desktop.png)                     | Works as expected |
| Subscription Complete                | ![screenshot](../docs/testing/browser-testing/firefox/subscription-confirm-mobile.png)              | ![screenshot](../docs/testing/browser-testing/firefox/subscription-confirm-desktop.png)              | Works as expected |
| Terms & Conditions                   | ![screenshot](../docs/testing/browser-testing/firefox/terms-and-conditions-mobile.png)              | ![screenshot](../docs/testing/browser-testing/firefox/terms-and-conditions-desktop.png)              | Works as expected |
| Wishlist                             | ![screenshot](../docs/testing/browser-testing/firefox/wishlist-mobile.png)                          | ![screenshot](../docs/testing/browser-testing/firefox/wishlist-desktop.png)                          | Works as expected |
| Wishlist Edit                        | ![screenshot](../docs/testing/browser-testing/firefox/wishlist-edit-mobile.png)                     | ![screenshot](../docs/testing/browser-testing/firefox/wishlist-edit-desktop.png)                     | Works as expected |
| Wishlist   Create                    | ![screenshot](../docs/testing/browser-testing/firefox/wishlist-create-mobile.png)                   | ![screenshot](../docs/testing/browser-testing/firefox/wishlist-create-desktop.png)                   | Works as expected |
| Wishlist   Delete                    | ![screenshot](../docs/testing/browser-testing/firefox/wishlist-delete-mobile.png)                   | ![screenshot](../docs/testing/browser-testing/firefox/wishlist-delete-desktop.png)                   | Works as expected |
| 404 Not Found                        | ![screenshot](../docs/testing/browser-testing/firefox/404-error-mobile.png)                         | ![screenshot](../docs/testing/browser-testing/firefox/404-error-desktop.png)                         | Works as expected |


</details>

- [Safari](https://support.apple.com/downloads/safari) Version 17.1 (19616.2.9.11.7)

<details>
  <summary>
    <strong>View detailed screenshots for Safari</strong>
  </summary>

| Browser                              | Device (mobile)                                                                                    | Device (desktop)                                                                                    | Notes             |
|--------------------------------------|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-------------------|
| About                                | ![screenshot](../docs/testing/browser-testing/webkit/about-mobile.png)                             | ![screenshot](../docs/testing/browser-testing/webkit/about-desktop.png)                             | Works as expected |
| Account Profile                      | ![screenshot](../docs/testing/browser-testing/webkit/account-profile-mobile.png)                   | ![screenshot](../docs/testing/browser-testing/webkit/account-profile-desktop.png)                   | Works as expected |
| Account Profile Delivery Information | ![screenshot](../docs/testing/browser-testing/webkit/account-profile-order-information-mobile.png) | ![screenshot](../docs/testing/browser-testing/webkit/account-profile-order-information-desktop.png) | Works as expected |
| Account Profile Past Orders          | ![screenshot](../docs/testing/browser-testing/webkit/account-profile-past-orders-mobile.png)       | ![screenshot](../docs/testing/browser-testing/webkit/account-profile-past-orders-desktop.png)       | Works as expected |
| Checkout                             | ![screenshot](../docs/testing/browser-testing/webkit/checkout-mobile.png)                          | ![screenshot](../docs/testing/browser-testing/webkit/checkout-desktop.png)                          | Works as expected |
| Contact                              | ![screenshot](../docs/testing/browser-testing/webkit/contact-mobile.png)                           | ![screenshot](../docs/testing/browser-testing/webkit/contact-desktop.png)                           | Works as expected |
| FAQS                                 | ![screenshot](../docs/testing/browser-testing/webkit/faqs-mobile.png)                              | ![screenshot](../docs/testing/browser-testing/webkit/faqs-desktop.png)                              | Works as expected |
| Home                                 | ![screenshot](../docs/testing/browser-testing/webkit/home-mobile.png)                              | ![screenshot](../docs/testing/browser-testing/webkit/home-desktop.png)                              | Works as expected |
| Home Menu Open                       | ![screenshot](../docs/testing/browser-testing/webkit/home-menu-open-mobile.png)                    | ![screenshot](../docs/testing/browser-testing/webkit/home-menu-open-desktop.png)                    | Works as expected |
| Home Subscription Signup             | ![screenshot](../docs/testing/browser-testing/webkit/home-subscription-signup-mobile.png)          | ![screenshot](../docs/testing/browser-testing/webkit/home-subscription-signup-desktop.png)          | Works as expected |
| Login                                | ![screenshot](../docs/testing/browser-testing/webkit/login-mobile.png)                             | ![screenshot](../docs/testing/browser-testing/webkit/login-desktop.png)                             | Works as expected |
| Order Complete                       | ![screenshot](../docs/testing/browser-testing/webkit/order-complete-mobile.png)                    | ![screenshot](../docs/testing/browser-testing/webkit/order-complete-desktop.png)                    | Works as expected |
| Privacy Policy                       | ![screenshot](../docs/testing/browser-testing/webkit/privacy-policy-mobile.png)                    | ![screenshot](../docs/testing/browser-testing/webkit/privacy-policy-desktop.png)                    | Works as expected |
| Products                             | ![screenshot](../docs/testing/browser-testing/webkit/products-mobile.png)                          | ![screenshot](../docs/testing/browser-testing/webkit/products-desktop.png)                          | Works as expected |
| Product Detail                       | ![screenshot](../docs/testing/browser-testing/webkit/product-detail-mobile.png)                    | ![screenshot](../docs/testing/browser-testing/webkit/product-detail-desktop.png)                    | Works as expected |
| Product Detail Wishlist              | ![screenshot](../docs/testing/browser-testing/webkit/product-detail-wishlist-mobile.png)           | ![screenshot](../docs/testing/browser-testing/webkit/product-detail-wishlist-desktop.png)           | Works as expected |
| Product Search                       | ![screenshot](../docs/testing/browser-testing/webkit/product-search-mobile.png)                    | ![screenshot](../docs/testing/browser-testing/webkit/product-search-desktop.png)                    | Works as expected |
| Register                             | ![screenshot](../docs/testing/browser-testing/webkit/register-mobile.png)                          | ![screenshot](../docs/testing/browser-testing/webkit/register-desktop.png)                          | Works as expected |
| Shipping & Information               | ![screenshot](../docs/testing/browser-testing/webkit/shipping-and-information-mobile.png)          | ![screenshot](../docs/testing/browser-testing/webkit/shipping-and-information-desktop.png)          | Works as expected |
| Shopping Cart                        | ![screenshot](../docs/testing/browser-testing/webkit/shopping-cart-mobile.png)                     | ![screenshot](../docs/testing/browser-testing/webkit/shopping-cart-desktop.png)                     | Works as expected |
| Terms & Conditions                   | ![screenshot](../docs/testing/browser-testing/webkit/terms-and-conditions-mobile.png)              | ![screenshot](../docs/testing/browser-testing/webkit/terms-and-conditions-desktop.png)              | Works as expected |
| Wishlist                             | ![screenshot](../docs/testing/browser-testing/webkit/wishlist-mobile.png)                          | ![screenshot](../docs/testing/browser-testing/webkit/wishlist-desktop.png)                          | Works as expected |
| Wishlist Create                      | ![screenshot](../docs/testing/browser-testing/webkit/wishlist-create-mobile.png)                   | ![screenshot](../docs/testing/browser-testing/webkit/wishlist-create-desktop.png)                   | Works as expected |
| Wishlist   Edit                      | ![screenshot](../docs/testing/browser-testing/webkit/wishlist-edit-mobile.png)                     | ![screenshot](../docs/testing/browser-testing/webkit/wishlist-edit-desktop.png)                     | Works as expected |
| wishlist   Delete                    | ![screenshot](../docs/testing/browser-testing/webkit/wishlist-delete-mobile.png)                   | ![screenshot](../docs/testing/browser-testing/webkit/wishlist-delete-desktop.png)                   | Works as expected |
| 404                                  | ![screenshot](../docs/testing/browser-testing/webkit/404-error-mobile.png)                         | ![screenshot](../docs/testing/browser-testing/webkit/404-desktop.png)                               | Works as expected |

</details>

## Responsiveness

Device testing was conducted using the [Polypane browser app](https://polypane.app), which allows for testing on multiple
devices simultaneously.

The three sizes tested were:

- Mobile (320px)
- Tablet (500px)
- Desktop (12580px)


| Page                 | Screenshots                                               | Notes             |
|----------------------|-----------------------------------------------------------|-------------------|
| About us             | ![screenshot](../docs/testing/polypane/about-us.png)      | Works as expected |
| Cart                 | ![screenshot](../docs/testing/polypane/cart.png)          | Works as expected |
| Checkout             | ![screenshot](../docs/testing/polypane/checkout.png)      | Works as expected |
| Delivery Information | ![screenshot](../docs/testing/polypane/delivery-info.png) | Works as expected |
| Desktop Menu         | ![screenshot](../docs/testing/polypane/desktop-menu.png)  | Works as expected |
| Email Verification   | ![screenshot](../docs/testing/polypane/email-verify.png)  | Works as expected | 
| Home                 | ![screenshot](../docs/testing/polypane/home.png)          | Works as expected |  
| Login                | ![screenshot](../docs/testing/polypane/sign-in.png)       | Works as expected |
| Mobile Menu          | ![screenshot](../docs/testing/polypane/mobile-menu.png)   | Works as expected |
| Products All    | ![screenshot](../docs/testing/polypane/products.png)      | Works as expected |
| Product Detail       | ![screenshot](../docs/testing/polypane/product.png)       | Works as expected |
| Profile              | ![screenshot](../docs/testing/polypane/profile.png)       | Works as expected |
| Profile Orders       | ![screenshot](../docs/testing/polypane/past-order.png)    | Works as expected |
| Register New User    | ![screenshot](../docs/testing/polypane/register.png)      | Works as expected |
| Register New User    | ![screenshot](../docs/testing/polypane/register.png)      | Works as expected |

## Lighthouse Audit

> [!IMPORTANT]
>
> **Lighthouse Audit**
> The primary cause of performance issues can be attributed to the Stripe.js file and the static files obtained from the AWS S3 bucket. The Stripe.js file is essential for enabling Stripe payment functionality, while the static files from AWS are necessary for the proper functioning of CSS, JavaScript, and image files.

![screenshot performance](../docs/testing/lighthouse/PageSpeed-Insights-perf-issues.png)

I have conducted a series of Lighthouse Audits on my application. The Lighthouse Audit is a tool that is built into the Chrome DevTools. It is used to measure the performance, accessibility, best practices and SEO of a website.

The Lighthouse Audit was conducted on the following pages:

- About us
- Cart
- Contact us
- FAQS
- Home
- Products
- Product Detail
- Profile
- Profile Delivery Information
- Profile Orders
- Privacy Policy
- Register
- Sign In
- Terms and Conditions
- Wishlist

| Page     | Device (Mobile)   | Device (Desktop) | Notes              |
|----------|-------------------|-----------------|---------------------|
| About us | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-about-mobile.png) | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-about-desktop.png) | Minor issues|
| Cart | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-cart-mobile.png) | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-cart-desktop.png) | Minor issues|
| Contact us | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-contact-mobile.png) | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-contact-desktop.png) | Minor issues|
| FAQS | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-faqs-mobile.png) | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-faqs-desktop.png) | Minor issues|
| Home | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-home-mobile.png) | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-home-desktop.png) | Minor issues|
| Products | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-products-mobile.png) | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-products-desktop.png) | Minor issues|
| Product Detail | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-product-detail-mobile.png) | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-product-detail-desktop.png) | Minor issues|
| Profile | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-profile-mobile.png) | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-profile-desktop.png) | Minor issues|
| Profile Delivery Information | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-profile-delivery-information-mobile.png) | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-profile-delivery-information-desktop.png) | Minor issues|
| Profile Orders | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-profile-past-orders-mobile.png) | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-profile-past-orders-desktop.png) | Minor issues|
| Privacy Policy | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-privacy-policy-mobile.png) | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-privacy-policy-desktop.png) | Minor issues|
| Register | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-register-mobile.png) | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-register-desktop.png) | Minor issues|
| Sign In | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-login-mobile.png) | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-login-desktop.png) | Minor issues|
| Terms and Conditions | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-terms-and-conditions-mobile.png) | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-terms-and-conditions-desktop.png) | Minor issues|
| Wishlist | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-wishlist-mobile.png) | ![screenshot](../docs/testing/lighthouse/PageSpeed-Insights-wishlist-desktop.png) | Minor issues|


