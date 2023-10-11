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
