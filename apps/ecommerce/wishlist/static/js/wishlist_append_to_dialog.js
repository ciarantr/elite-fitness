// Js Hint options added for assessor convenience

// Allows the JShint validator to recognise modern ES6 methods, such as
// `let`, `const`, `template literals`, `arrow functions (=>)`,
/* jshint esversion: 11 */

// Suppress warnings missing semicolons
/* jshint asi: true */

document.addEventListener('DOMContentLoaded', () => {
  const wishlistDialog = document.getElementById('wishlist')
  const wishlistButtons = document.querySelectorAll('[data-popup="wishlist"]')

  const closeHandler = function (event) {
    wishlistDialog.removeChild(event.target.form)
    wishlistDialog.removeEventListener('close', closeHandler, false)
  }

  wishlistButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const form = button.nextElementSibling.firstElementChild.cloneNode(true)
      wishlistDialog.form = form
      wishlistDialog.appendChild(form)
      wishlistDialog.showModal()
      wishlistDialog.addEventListener('close', closeHandler, false)
    })
  })
})
