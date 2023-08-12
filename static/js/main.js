const mobileMenuBtn = document.querySelector('#toggle-nav-sidebar')
const mobileMenu = document.querySelector('#menu-content')
const closeMobileMenuBtn = mobileMenu.querySelector('button')
const desktopMenu = document.querySelectorAll('.desktop-nav-menu')
const desktopSearchBtn = document.querySelector('#toggle-search-form')
const desktopSearchContainer = document.querySelector('#search-container')
const desktopSearchCloseBtn = desktopSearchContainer.querySelector(
  'button[type="reset"]',
)

// Helper methods to control ARIA attributes and class
const setAria = (element, elementTwo, expanded, hidden) => {
  element.setAttribute('aria-expanded', expanded)
  elementTwo.setAttribute('aria-hidden', hidden)
}

const toggleClass = (element, className, action) => {
  element.classList[action](className)
}

// Control the flyout menu on mobile
mobileMenuBtn.addEventListener('click', () => {
  toggleClass(mobileMenu, 'open', 'toggle')
  setAria(mobileMenuBtn, mobileMenu, 'true', 'false')
  setAria(closeMobileMenuBtn, mobileMenu, 'true', 'false')
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
    setAria(menu, menu.nextElementSibling, 'true', 'false')
    toggleClass(menu.nextElementSibling, 'open', 'add')
  })

  menu.addEventListener('mouseleave', () => {
    setAria(menu, menu.nextElementSibling, 'false', 'true')
    toggleClass(menu.nextElementSibling, 'open', 'remove')
  })

  menu.nextElementSibling.addEventListener('mouseenter', () => {
    setAria(menu, menu.nextElementSibling, 'true', 'false')
    toggleClass(menu.nextElementSibling, 'open', 'add')
  })

  menu.nextElementSibling.addEventListener('mouseleave', () => {
    setAria(menu, menu.nextElementSibling, 'false', 'true')
    toggleClass(menu.nextElementSibling, 'open', 'remove')
  })
})

// make sure the menu is closed when the window is resized
window.addEventListener('resize', () => {
  if (window.innerWidth > 1024) {
    mobileMenu.classList.remove('open')
    mobileMenu.setAttribute('aria-hidden', 'true')
    closeMobileMenuBtn.setAttribute('aria-expanded', 'false')
  }
})

// Control the search form on desktop
// Set aria-attributes and toggle class on click
desktopSearchBtn.addEventListener('click', () => {
  desktopSearchContainer.classList.toggle('open')
  const searchBtnAttrsState = desktopSearchBtn.getAttribute('aria-expanded')
  const desktopSearchBtnAttrsState =
    desktopSearchContainer.getAttribute('aria-hidden')

  desktopSearchBtn.setAttribute(
    'aria-expanded',
    searchBtnAttrsState === 'true' ? 'false' : 'true',
  )
  desktopSearchContainer.setAttribute(
    'aria-hidden',
    desktopSearchBtnAttrsState === 'true' ? 'false' : 'true',
  )

  // add focus to the search input
  desktopSearchContainer.querySelector('input').focus()
})

// close the search form on desktop & set aria-attributes
desktopSearchCloseBtn.addEventListener('click', () => {
  desktopSearchContainer.classList.toggle('open')
  desktopSearchContainer.setAttribute('aria-hidden', 'true')
  desktopSearchBtn.setAttribute('aria-expanded', 'false')
})
