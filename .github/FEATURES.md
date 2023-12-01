# Features ✨

**Readme navigation links: 🧭**
- [📕 View Readme documentation](./README.md)
- [🎨 View Design documentation](./DESIGN.md#ux--ui-)
- [🚀 View Deployment documentation (Local & Production)](./DEPLOYMENT.md#deployment-)
- [🔓 View Security documentation](./SECURITY.md#security-)
- [🧪 View Testing documentation](./TESTING.md#testing-)
---

The feature documentation provides a comprehensive and detailed explanation of the website's features and functionality.
It incorporates screenshots of the website for visual reference.
This documentation serves as a valuable resource for individuals seeking to deepen their understanding of the website. It is organised into sections, each focusing on a distinct aspect of the website.
The following sections are included:

[Navigate back to README Documentation](./README.md)

- **Existing Features**
  - Key Features
  - Supporting Features
- [**Future Features**](#future-features)

## Existing features:

### 🔑 Key features:

- [Users can register for an account.](#account-registration)
- [Users can log in to view their account.](#account-login)
- [Users can change reset their password.](#account-password-reset)
- [Users can view store products with detailed information.](#store-products)
- [Users can sort products by category, brand, price & the newest product.](#store-products)
- [Users can search for products by name or description.](#store-products)
- [Users can add products to their cart.](#shopping-cart)
- [Users can update the quantity of products in their cart.](#shopping-cart)
- [Users can view an order summary before placing an order.](#checkout)
- [Users can easily navigate to the cart page from the checkout page.](#checkout)
- [Users can subscribe to the newsletter.](#newsletter)
- [Users can easily navigate to the store page from the mobile flout menu, the desktop dropdown menu or the footer.](#navigation)


- [Admins can add/update/delete products to the store via the admin panel.](#admin-panel)
- [Admins can add product categories/brands/colours/sizes to the store via the admin panel.](#admin-panel)
- [Admins can view & update all orders placed by users via the admin panel.](#admin-panel)
- [Admins can view subscribers via the admin panel.](#admin-panel)
- [Admins can add/update/delete users delivery information via the admin panel.](#admin-panel)

### 🫶 Supporting features:

- [Users can view their order history.](#account-profile)
- [Users can update their account information & delivery information details.](#account-profile)
- [Users can choose which wishlist to add products to.](#wishlist)
- [Users can create wishlists & add products to their wishlist.](#wishlist)
- [Users can view their wishlist & add products to their cart from their wishlist.](#wishlist)
- [Users can make changes to their wishlist name & description & delete their wishlist.](#wishlist)
- [Registered Users can update their default shipping address details at checkout.](#checkout)
- [Users can view helpful information such as delivery information, returns & refunds, terms & conditions & privacy policy via the footer.](#additional-features)
- [Users can view the store's social media links via the footer.](#additional-features)
- [User can send a message to the store via the contact form.](#additional-features)
- [User will receive a confirmation message once they have sent a message to the store.](#additional-features)

#### Account registration

- Users can register for an account by clicking the register link in the navbar. or by clicking the register link on the login page. For mobile, the account link is conveniently placed in a sticky footer. Users will be sent a confirmation email to verify their account. Once the account is verified, users will be able to log in to their account. Users will also see the name of their account in the navbar once they are logged in & a sign message will be displayed in the navbar.

<details>

  <summary>📸 Preview</summary>

  ![account register mobile ](../docs/features/sign-in-mobile.png)
  ![account register mobile ](../docs/features/sign-in-desktop.png)
  ![account registration](../docs/features/account-register.png)
  ![account registration email](../docs/features/register-email-confirmation.png)

</details>

#### Account login

- Users can log in to their account by clicking the login link in the navbar. or by clicking the login link on the register page. For mobile, the account link is conveniently placed in a sticky footer. Users will also see the name of their account in the navbar once they are logged in & a sign message will be displayed in the navbar.

<details>

  <summary>📸 Preview</summary>

  ![account login mobile ](../docs/features/sign-in-mobile.png)
  ![account login desktop ](../docs/features/sign-in-desktop.png)
  ![account login](../docs/features/account-login.png)

</details>

#### Account password reset

- Users can reset their password by clicking the forgot password link on the login page. Users will be redirected to a confirmation page and will shortly after receive an email with a link to reset their password. Once the password is reset, users will be redirected to the login page.

<details>

  <summary>📸 Preview</summary>

  ![account password reset](../docs/features/password-reset-message.png)
  ![account password reset email](../docs/features/password-reset-email.png)

</details>

#### Account profile

- Users can update their details, shipping details & view their order history. Users will receive a confirmation message once they have updated their details.

<details>

  <summary>📸 Preview</summary>

  ![account profile](../docs/features/profile-account-information.png)
  ![account profile](../docs/features/profile-delivery-information.png)
  ![account profile](../docs/features/profile-order-history.png)
  ![account profile](../docs/features/profile-update-message.png)
  ![account profile](../docs/features/profile-delivery-information-update-message.png)

</details>

#### Store products

- On the product page, users have the ability to view all available store products. Users can also view the product details to find out more information on the product which includes a product description and key benefits. Users can also conveniently sort products by category, brand, price, and the latest additions. Additionally, users can easily search for products by name or description. To add items to their cart, users simply need to click the "Add to Cart" button.
- Pagination is also implemented on the product page to improve the user experience. Users can navigate through the pages to view more products.

<details>

  <summary>📸 Preview</summary>

  ![account profile](../docs/features/all-products.png)
  ![account profile](../docs/features/product-sorting.png)
  ![account profile](../docs/features/product-detail.png)
  ![account profile](../docs/features/product-search.png)
  ![account profile](../docs/features/search-results.png)

</details>

#### Shopping cart

- Users can access the cart page by clicking on the cart icon located in the header for desktop or the sticky footer for mobile users. Users can also view the cart by hovering over the cart icon which will display a preview of the products in the cart. Users can also remove products from their cart by clicking the remove button. Users can also update the quantity of products in their cart by clicking x button icon. Users can also conveniently navigate back to the store by clicking the "Continue Shopping" button. Users can also conveniently navigate to the checkout page by clicking the "Checkout" button.

- Users will also receive a confirmation message once they have updated their cart.

<details>

  <summary>📸 Preview</summary>

  ![account profile](../docs/features/cart-navbar.png)
  ![account profile](../docs/features/sign-in-mobile.png)
  ![account profile](../docs/features/cart-preview.png)
  ![account profile](../docs/features/cart-update-preview.png)
  ![account profile](../docs/features/cart-removed-update.png)

</details>

#### Wishlist

- Users have the ability to create wishlists and add products to them. Additionally, they can view their wishlists and add products from their wishlists to their shopping carts. Users also have the option to modify the name and description of their wishlists, as well as delete them. Furthermore, users can select which wishlist they want to add products to.
Upon updating their wishlist, users will receive a confirmation message to acknowledge the changes. To access the wishlist page, users can click on the wishlist icon located in the header for desktop users or the sticky footer for mobile users. To remove products from the wishlist, users can simply click the remove button.

<details>

  <summary>📸 Preview</summary>

  ![account profile](../docs/features/account-login-name.png)
  ![account profile](../docs/features/cart-navbar.png)
  ![account profile](../docs/features/add-to-wishlist-button.png)
  ![account profile](../docs/features/shopping-cart-wishlist-option.png)
  ![account profile](../docs/features/add-remove-product-wishlist.png)
  ![account profile](../docs/features/wishlist-page.png)
  ![account profile](../docs/features/wishlist-create.png)
  ![account profile](../docs/features/wishlist-edit.png)
  ![account profile](../docs/features/wishlist-confirm-delete.png)
  ![account profile](../docs/features/wishlist-updated-msg.png)
  ![account profile](../docs/features/wishlist-created-msg.png)
  ![account profile](../docs/features/wishlist-deleted-msg.png)

</details>

#### Checkout

- Registered Users can also update their address details at checkout using the checkbox located at the end of the deleivery information form in checkout. Users can view a preview of their order before placing an order. Users can also navigate back to the cart page by clicking the "Back to cart" button or link.
- Users will also receive a confirmation message once they have placed their order. & an order confirmation email will be sent to the user.
- Users will be redirected to a order confirmation page once they have placed their order. Users will also receive an confirmation message.

<details>

  <summary>📸 Preview</summary>

  ![account profile](../docs/features/checkout.png)
  ![account profile](../docs/features/order-confirmation.png)
  ![account profile](../docs/features/order-confirmation-email.png)

</details>

#### Newsletter

- Users can subscribe to the newsletter by entering their email address in the newsletter form located in the footer. Users will receive a confirmation message once they have subscribed to the newsletter.

<details>

  <summary>📸 Preview</summary>

  ![account profile](../docs/features/newsletter-form.png)
  ![account profile](../docs/features/newsletter-msg.png)
  ![account profile](../docs/features/newsletter-confirmation-email.png)
  ![account profile](../docs/features/newsletter-confirmation.png)

</details>

#### Navigation**

- Users can easily navigate to the store page from the mobile flout menu, the desktop dropdown menu or the footer.

<details>

  <summary>📸 Preview</summary>

  ![mobile flyout menu](../docs/features/mobile-menu.png)
  ![mobile sticky footer](../docs/features/sign-in-mobile.png)
  ![desktop dropdown menu](../docs/features/desktop-menu.png)
  ![footer menu](../docs/features/footer-menu.png)

</details>

#### Admin panel

- Admins can add/update/delete products to the store via the admin panel. Admins can also add product categories/brands & product attributes to the store via the admin panel.
- Admins can view & update all orders placed by users via the admin panel. Admins can view subscribers via the admin panel. Admins can add/update/delete users delivery information via the admin panel.
- Admins can view & edit subscription details via the admin panel.

<details>

  <summary>📸 Preview</summary>

  ![admin panel](../docs/features/admin-products-overview.png)
  ![admin panel](../docs/features/admin-product-update.png)
  ![admin panel](../docs/features/admin-delivery-details-overview.png)
  ![admin panel](../docs/features/admin-delivery-details-update.png) 
  ![admin panel](../docs/features/admin-subscription-overview.png) ![admin panel](../docs/features/admin-subscription-update.png)

</details>

#### ➕Additional features:

- Users can view helpful information such as delivery information, returns & refunds, terms & conditions & privacy policy via the footer.
- Users can view the store's social media links via the footer.
- User can send a message to the store via the contact form.
- User will receive a confirmation message once they have sent a message to the store.

<details>

  <summary>📸 Preview</summary>

  ![account profile](../docs/features/contact-us.png)
  ![account profile](../docs/features/contact-support-email.png)
  ![account profile](../docs/features/shipping-information.png)
  ![account profile](../docs/features/terms-and-conditions.png)
  ![account profile](../docs/features/privacy-policy.png)

</details>

## 🔮Future features:

- Upgrade user profile page to SPA. (Single Page Application using React JS)
- Display products in search results below the search bar.
- Add a product rating system.
- Add a product review system.
- Load new products on page without refreshing the page.
- Integrate a social media login system.

🔝 [Back to Top](#features-)