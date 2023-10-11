const mobileMenuBtn = document.querySelector('#toggle-nav-sidebar')
const mobileMenu = document.querySelector('#navbar-menu')
const closeMobileMenuBtn = mobileMenu.querySelector('button')
const desktopMenu = document.querySelectorAll('.desktop-nav-menu')
const desktopSearchBtn = document.querySelector('#toggle-search-form')
const desktopSearchContainer = document.querySelector('#search-container')
const desktopSearchCloseBtn = desktopSearchContainer.querySelector(
  'button[type="reset"]',
)
const overlay = document.createElement('div')

// Helper methods to control ARIA attributes and class
const setAria = (element, elementTwo, expanded, hidden) => {
  if (!expanded) {
    elementTwo.setAttribute('aria-hidden', hidden)
  } else {
    element.setAttribute('aria-expanded', expanded)
    elementTwo.setAttribute('aria-hidden', hidden)
  }
}

const toggleClass = (element, className, action) => {
  element.classList[action](className)
}

// Control the flyout menu on mobile
mobileMenuBtn.addEventListener('click', () => {
  toggleClass(mobileMenu, 'open', 'toggle')
  setAria(mobileMenuBtn, mobileMenu, 'true', 'false')
  setAria(closeMobileMenuBtn, mobileMenu, 'true', 'false')

  // make sure the menu is closed when the window is resized
  window.addEventListener('resize', () => {
    if (window.innerWidth > 1024) {
      mobileMenu.classList.remove('open')
      mobileMenu.setAttribute('aria-hidden', 'true')
      closeMobileMenuBtn.setAttribute('aria-expanded', 'false')
    }
  })
})

closeMobileMenuBtn.addEventListener('click', () => {
  toggleClass(mobileMenu, 'open', 'toggle')
  setAria(mobileMenuBtn, mobileMenu, 'false', 'true')
  setAria(closeMobileMenuBtn, mobileMenu, 'false', 'true')
})

// Control the dropdown menu on desktop
// Set aria-attributes and toggle class on mouseover and mouseleave
desktopMenu.forEach((menu) => {
  menu.addEventListener('mouseover', () => {
    setAria(menu, menu.nextElementSibling, false, 'false')
    toggleClass(menu.nextElementSibling, 'open', 'add')
  })

  menu.addEventListener('mouseleave', () => {
    setAria(menu, menu.nextElementSibling, false, 'true')
    toggleClass(menu.nextElementSibling, 'open', 'remove')
  })

  menu.nextElementSibling.addEventListener('mouseenter', () => {
    setAria(menu, menu.nextElementSibling, false, 'false')
    toggleClass(menu.nextElementSibling, 'open', 'add')
  })

  menu.nextElementSibling.addEventListener('mouseleave', () => {
    setAria(menu, menu.nextElementSibling, false, 'true')
    toggleClass(menu.nextElementSibling, 'open', 'remove')
  })
})

// Control the search form on desktop
// Set aria-attributes and toggle class on click
desktopSearchBtn.addEventListener('click', () => {
  desktopSearchContainer.classList.toggle('open')

  const desktopSearchBtnAttrsState =
    desktopSearchContainer.getAttribute('aria-hidden')

  desktopSearchContainer.setAttribute(
    'aria-hidden',
    desktopSearchBtnAttrsState === 'true' ? 'false' : 'true',
  )
  // add focus to the search input
  desktopSearchContainer.querySelector('input').focus()
  // add overlay to the page
  document.body.appendChild(overlay)
  disableMenuNav()

  window.addEventListener('scroll', closeSearchOnScroll)
  removeOverlay()
})

function disableMenuNav() {
  // disable all nav submenu popover
  const isOpen = desktopSearchContainer.classList.contains('open')
  desktopMenu.forEach((element) => {
    element.setAttribute('aria-hidden', isOpen ? 'true' : 'false')
    if (isOpen) {
      element.setAttribute('inert', 'true')
    } else {
      element.removeAttribute('inert')
    }
  })

  overlay.classList.toggle('overlay', isOpen)
}

function removeOverlay() {
  document.body.addEventListener('click', (event) => {
    if (event.target === overlay) {
      desktopSearchContainer.classList.toggle('open')
      desktopSearchContainer.setAttribute('aria-hidden', 'true')
      disableMenuNav()
    }
  })

  // listen for the escape key to close the search form
  document.addEventListener('keydown', (event) => {
    if (
      event.key === 'Escape' &&
      desktopSearchContainer.classList.contains('open')
    ) {
      desktopSearchContainer.classList.toggle('open')
      desktopSearchContainer.setAttribute('aria-hidden', 'true')
      disableMenuNav()
    }
  })
}

function closeSearchOnScroll() {
  if (window.scrollY > 150) {
    desktopSearchContainer.classList.remove('open')
    desktopSearchContainer.setAttribute('aria-hidden', 'true')
    disableMenuNav()
  }
}

// close the search form on desktop & set aria-attributes
desktopSearchCloseBtn.addEventListener('click', () => {
  desktopSearchContainer.classList.toggle('open')
  desktopSearchContainer.setAttribute('aria-hidden', 'true')
  disableMenuNav()
})

const cartNavigation = document.querySelector('#cart-navigation')
const cartDropdown = document.querySelector('#cart-popover')

function showCartDropdown() {
  cartDropdown.setAttribute('aria-hidden', 'false')
}
function hideCartDropdown() {
  if (
    cartDropdown.getAttribute('aria-hidden') === 'true' &&
    cartNavigation.getAttribute('aria-expanded') === 'true'
  ) {
    cartNavigation.setAttribute('aria-expanded', 'false')
    cartDropdown.setAttribute('aria-hidden', 'true')
  }
}

// Add event listeners for hover effects
cartNavigation?.addEventListener('mouseover', showCartDropdown)
cartNavigation?.addEventListener('mouseleave', hideCartDropdown)
cartDropdown?.addEventListener('mouseleave', () =>
  cartDropdown.setAttribute('aria-hidden', 'true'),
)

setTimeout(() => {
  const messages = document.querySelectorAll('[data-django-message]')
  // Apply a fade-out animation using CSS transitions
  if (messages) {
    //   loop through all the messages and add the fade-out class
    messages.forEach((element) => {
      // Apply a fade-out animation using CSS transitions
      element.style.transition = 'opacity 0.5s'
      element.style.opacity = '0'

      // Remove the messages element from the DOM after the animation completes
      setTimeout(() => {
        element.parentNode.removeChild(element)
      }, 500)
    })
  }
}, 4000)
