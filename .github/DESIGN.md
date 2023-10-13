# UX / UI 🎨

[Navigate back to README Documentation](./README.md)

The design process for the Elite Fitness e-commerce website commenced with the utilisation of the Figma design tool. I developed designs for various screen sizes, encompassing mobile, iPad, and desktop, with the aim of ensuring a seamless user experience across all devices.

To actualise our design process, I conducted extensive research to meticulously select the ideal colours and images for the application. I examined the utilisation of colour and imagery in other successful restaurant applications and delved into the cultural significance of colors in Japanese cuisine.

In order to complement the visual representation of the available dishes, I judiciously curated a color palette that would harmonize with the visual elements, thereby creating a cohesive and inviting experience for users. By dedicating time to thorough research and meticulous selection of design elements, we achieved the creation of an application that not only boasts aesthetic appeal but also enhances the overall user experience.

## Colour Scheme

I utilized Figma design tools to generate the color palette.

![Colour Palette](../docs/design/colour-palette.png)

I have employed CSS :root variables to customize the appearance of Django alert messages. The following CSS variables are used to style the alert messages:

```css
:root {
    --alert-success: hsl(143, 45%, 24%);
    --alert-error: hsl(5, 50%, 36%);
    --alert-warning: hsl(49, 60%, 44%);
    --alert-info: hsl(204, 58%, 32%);
}
```


## Typography

I used Google Fonts Open Sans web font for the entire website with Arial as the fallback font in case for any reason the font isn't being imported into the site correctly. Open Sans is a clean and easy to read font & is used widely across the web. I converted the font TTF file to WOFF2 using to improve performance.

## Icons

I've used the [icons.js](https://icones.js.org/collection/all) library to find suitable icons for my project. I simply searched for the icon I wanted and copied into Figma and then into my project. All fonts uses are located in the static/icons folder.

## Images

I have sources my images from three different sources based on the product range.

1. [Wild Nutrition](https://www.wildnutrition.com/) for supplement images and banner images.
2. [Pelaton](https://www.onepeloton.co.uk/) for exercise equipment images.
3. [Juicers.ie](https://www.juicers.ie/) for juicer images.

## Design Mockups with High Fidelity

In adherence to industry standards, meticulous mockups were created for mobile, tablet, and desktop dimensions. Figma, a vector graphics editor and prototyping tool, was employed for the purpose of designing the website mockups. The Figma design file can be accessed in the docs/design/figma/elite-fitness.fig directory.

Navigate to design mockups for the following pages:

- [About Page](#about-page)
- [Contact Page](#contact-page)
- [Checkout Page](#checkout-page)
- [Checkout Success Page](#checkout-success-page)
- [Faq Page](#faq-page)
- [Home Page](#home-page)
- [Login Page](#login-page)
- [Mobile Flyout Menu](#mobile-flyout-menu)
- [Profile Page](#profile-page)
- [Profile Delivery Information Page](#profile-delivery-information-page)
- [Profile Order History Page](#profile-order-history-page)
- [Products Page](#products-page)
- [Product Detail Page](#product-detail-page)
- [Privacy Policy Page](#privacy-policy-page)
- [Register Page](#register-page)
- [Shopping Cart Page](#shopping-cart-page)
- [Shipping And Information Page](#shipping-and-information-page)
- [Wishlist Page With Products](#wishlist-page-with-products)
- [Wishlist Page Without Products](#wishlist-page-without-products)
- [Wishlist Page Edit Wishlist](#wishlist-page-edit-wishlist)
- [Wishlist Page Delete Wishlist](#wishlist-page-delete-wishlist)
- [Wishlist Page Add Product](#wishlist-page-add-product)
- [404 Page](#404-page)
- [Facebook mockup](#facebook-mockup)

### About Page

<details>

  <summary>Mobile</summary>

  ![About Page Mobile](../docs/design/about-sm.png)
</details>

<details>

  <summary>Tablet</summary>

  ![About Page Tablet](../docs/design/about-md.png)
</details>

<details>

  <summary>Desktop</summary>

  ![About Page Desktop](../docs/design/about-lg.png)
</details>

### Contact Page

<details>

  <summary>Mobile</summary>

  ![Contact Page Mobile](../docs/design/contact-sm.png)
</details>

<details>

  <summary>Tablet</summary>

  ![Contact Page Tablet](../docs/design/contact-md.png)
</details>

<details>

  <summary>Desktop</summary>

  ![Contact Page Desktop](../docs/design/contact-lg.png)
</details>

### Checkout Page

<details>

  <summary>Mobile</summary>

![Checkout Page Mobile](../docs/design/checkout-sm.png)
</details>

<details>

  <summary>Tablet</summary>

![Checkout Page Tablet](../docs/design/checkout-md.png)
</details>

<details>

  <summary>Desktop</summary>

![Checkout Page Desktop](../docs/design/checkout-lg.png)
</details>

### Checkout Success Page

<details>

  <summary>Mobile</summary>

![Checkout Success Page Mobile](../docs/design/checkout-success-sm.png)
</details>

<details>

  <summary>Tablet</summary>

![Checkout Success Page Tablet](../docs/design/checkout-success-md.png)
</details>

<details>

  <summary>Desktop</summary>

![Checkout Success Page Desktop](../docs/design/checkout-success-lg.png)
</details>

### Faq Page

<details>

  <summary>Mobile</summary>

  ![Faq Page Mobile](../docs/design/faq-sm.png)
</details>

<details>

  <summary>Tablet</summary>

  ![Faq Page Tablet](../docs/design/faq-md.png)
</details>

<details>

  <summary>Desktop</summary>

  ![Faq Page Desktop](../docs/design/faq-lg.png)

</details>

### Home Page

<details>

  <summary>Mobile</summary>

  ![Home Page Mobile](../docs/design/home-sm.png)
</details>

<details>

  <summary>Tablet</summary>

  ![Home Page Tablet](../docs/design/home-md.png)
</details>

<details>

  <summary>Desktop</summary>

  ![Home Page Desktop](../docs/design/home-lg.png)
</details>

### Login Page

<details>

  <summary>Mobile</summary>

![Login Page Mobile](../docs/design/login-sm.png)
</details>

<details>

  <summary>Tablet</summary>

![Login Page Tablet](../docs/design/login-md.png)
</details>

<details>

  <summary>Desktop</summary>

![Login Page Desktop](../docs/design/login-lg.png)
</details>

### Mobile Flyout Menu

<details>
   <summary>Mobile Menu Open</summary>

![Login Page Tablet](../docs/design/login-menu-open.png)
</details>

### Profile Page

<details>

  <summary>Mobile</summary>

![Profile Page Mobile](../docs/design/profile-sm.png)
</details>

<details>

  <summary>Tablet</summary>

![Profile Page Tablet](../docs/design/profile-md.png)
</details>

<details>

  <summary>Desktop</summary>

![Profile Page Desktop](../docs/design/profile-lg.png)
</details>

### Profile Delivery Information Page

<details>

  <summary>Mobile</summary>

![Profile Delivery Information Page Mobile](../docs/design/profile-delivery-info-sm.png)
</details>

<details>

  <summary>Tablet</summary>

![Profile Delivery Information Page Tablet](../docs/design/profile-delivery-info-md.png)
</details>

<details>

  <summary>Desktop</summary>

![Profile Delivery Information Page Desktop](../docs/design/profile-delivery-info-lg.png)
</details>

### Profile Order History Page
<details>

  <summary>Mobile</summary>

![Profile Order History Page Mobile](../docs/design/profile-order-sm.png)
</details>

<details>

  <summary>Tablet</summary>

![Profile Order History Page Tablet](../docs/design/profile-order-md.png)
</details>

<details>

  <summary>Desktop</summary>

![Profile Order History Page Desktop](../docs/design/profile-order-lg.png)
</details>

### Products Page

<details>

  <summary>Mobile</summary>

![Product List Page Mobile](../docs/design/products-sm.png)
</details>

<details>

  <summary>Tablet</summary>

![Product List Page Tablet](../docs/design/products-md.png)
</details>

<details>

  <summary>Desktop</summary>

![Product List Page Desktop](../docs/design/products-lg.png)
</details>

### Product Detail Page

<details>

  <summary>Mobile</summary>

  ![Product Detail Page Mobile](../docs/design/product-detail-sm.png)
</details>

<details>

  <summary>Tablet</summary>

  ![Product Detail Page Tablet](../docs/design/product-detail-md.png)
</details>

<details>

  <summary>Desktop</summary>

  ![Product Detail Page Desktop](../docs/design/product-detail-lg.png)
</details>

### Privacy Policy Page

<details>

  <summary>Mobile</summary>

  ![Privacy Policy Page Mobile](../docs/design/privacy-policy-sm.png)
</details>

<details>

  <summary>Tablet</summary>

  ![Privacy Policy Page Tablet](../docs/design/privacy-policy-md.png)
</details>

<details>

  <summary>Desktop</summary>

  ![Privacy Policy Page Desktop](../docs/design/privacy-policy-lg.png)
</details>

### Register Page

<details>

  <summary>Mobile</summary>

![Register Page Mobile](../docs/design/register-sm.png)
</details>


<details>

  <summary>Tablet</summary>

![Register Page Tablet](../docs/design/register-md.png)
</details>

<details>

  <summary>Desktop</summary>

![Register Page Desktop](../docs/design/register-lg.png)
</details>

### Shopping Cart Page

<details>

  <summary>Mobile</summary>

  ![Shopping Cart Page Mobile](../docs/design/cart-sm.png)
</details>

<details>

  <summary>Tablet</summary>

  ![Shopping Cart Page Tablet](../docs/design/cart-md.png)
</details>

<details>

  <summary>Desktop</summary>

  ![Shopping Cart Page Desktop](../docs/design/cart-lg.png)
</details>

### Shipping And Information Page

<details>

  <summary>Mobile</summary>

  ![Shipping And Information Page Mobile](../docs/design/shipping-information-sm.png)
</details>

<details>

  <summary>Tablet</summary>

  ![Shipping And Information Page Tablet](../docs/design/shipping-information-md.png)
</details>

<details>

  <summary>Desktop</summary>

  ![Shipping And Information Page Desktop](../docs/design/shipping-information-lg.png)
</details>

### Wishlist Page With Products

<details>

  <summary>Mobile</summary>

  ![Wishlist Page Mobile](../docs/design/wishlist-with-product-sm.png)
</details>

<details>

  <summary>Tablet</summary>

  ![Wishlist Page Tablet](../docs/design/wishlist-with-product-md.png)
</details>

<details>

  <summary>Desktop</summary>

  ![Wishlist Page Desktop](../docs/design/wishlist-with-product-lg.png)
</details>

### Wishlist Page Without Products

<details>

  <summary>Mobile</summary>

  ![Wishlist Page Mobile](../docs/design/wishlist-created-sm.png)
</details>

<details>

  <summary>Tablet</summary>

  ![Wishlist Page Tablet](../docs/design/wishlist-created-md.png)
</details>

<details>

  <summary>Desktop</summary>

  ![Wishlist Page Desktop](../docs/design/wishlist-created-lg.png)
</details>

### Wishlist Page Edit Wishlist

<details>

  <summary>Mobile</summary>

  ![Wishlist Page Mobile](../docs/design/wishlist-edit-sm.png)
</details>

<details>

  <summary>Tablet</summary>

  ![Wishlist Page Tablet](../docs/design/wishlist-edit-md.png)
</details>

<details>

  <summary>Desktop</summary>

  ![Wishlist Page Desktop](../docs/design/wishlist-edit-lg.png)
</details>

### Wishlist Page Delete Wishlist

<details>

  <summary>Mobile</summary>

  ![Wishlist Page Mobile](../docs/design/wishlist-delete-sm.png)
</details>

<details>

  <summary>Tablet</summary>

  ![Wishlist Page Tablet](../docs/design/wishlist-delete-md.png)
</details>

<details>

  <summary>Desktop</summary>

  ![Wishlist Page Desktop](../docs/design/wishlist-delete-lg.png)
</details>

### Wishlist Page Add Product

<details>

  <summary>Mobile</summary>

  ![Wishlist Page Mobile](../docs/design/wishlist-add-product-sm.png)
</details>

<details>

  <summary>Tablet</summary>

  ![Wishlist Page Tablet](../docs/design/wishlist-add-product-md.png)
</details>

<details>

  <summary>Desktop</summary>

  ![Wishlist Page Desktop](../docs/design/wishlist-add-product-lg.png)
</details>

### 404 Page

<details>
   <summary>Mobile</summary>

  ![404 Page Mobile](../docs/design/error-404-sm.png)
</details>

<details>
   <summary>Tablet</summary>

  ![404 Page Tablet](../docs/design/error-404-md.png)
</details>

<details>
   <summary>Desktop</summary>

  ![404 Page Desktop](../docs/design/error-404-lg.png)
</details>

### Facebook mockup

<details>
   <summary>Desktop</summary>

  ![Facebook Mobile](../docs/design/facebook-mockup.png)
</details>

🔝 [Back to top](#ux--ui-)