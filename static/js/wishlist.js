// Js Hint options added for assessor convenience

// Allows the JShint validator to recognise modern ES6 methods, such as
// `let`, `const`, `template literals`, `arrow functions (=>)`,
/* jshint esversion: 11 */

// Suppress warnings missing semicolons
/* jshint asi: true */

const openDialogButtons = document.querySelectorAll('[data-open-dialog]')
const closeDialogButtons = document.querySelectorAll('[data-close-dialog]')
const wishListForms = document.querySelectorAll('[data-wishlist-form]')
let initialWishlistName = ''
let initialWishlistDescription = ''
const paragraphElement = document.createElement('p')

// Disable the submit button if name input is empty or hasn't been changed
// Enable if the text area has been changed
const manageSubmitButtonState = (e) => {
  const { form } = e.target
  const input = form.querySelector('input[name="name"]')
  const textAreaElement = form.querySelector('textarea[name="description"]')
  const submitButton = form.querySelector('button[type="submit"]')

  const isTextAreaValid = isValueValid(
    textAreaElement.value,
    initialWishlistDescription,
  )
  const isInputValid = isValueValid(input.value, initialWishlistName)

  submitButton.disabled = !(isTextAreaValid || isInputValid)
}
// Disable the submitted button if name input is empty
wishListForms.forEach((form) => {
  const nameInput = form.querySelectorAll('input[name="name"]')
  nameInput.forEach((input) => {
    input.addEventListener('input', manageSubmitButtonState)
  })
})

// Add wishlist description to edit wishlist form
const handleEditList = async (button) => {
  const listId = button.getAttribute('data-list-id')
  const listName = button.parentElement.previousElementSibling.textContent
  const listForm = document.querySelector('#edit-list form')
  const descriptionInput = listForm.querySelector(
    'textarea[name="description"]',
  )
  const listInput = listForm.querySelector('input[name="name"]')
  listInput.value = listName
  listForm.setAttribute('action', `/wishlist/edit/${listId}/`)


  try {
    const response = await fetch(`/wishlist/details/${listId}/`)
    if (!response.ok) throw new Error('Network response was not ok')
    const data = await response.json()
    if (data.description) descriptionInput.value = data.description
    initialWishlistDescription = data.description
  } catch (error) {
    console.error('There has been a problem with your fetch operation:', error)
  }
}

const handleDeleteList = (button) => {
  const listId = button.getAttribute('data-list-id')
  const listName = button.parentElement.previousElementSibling.textContent
  const listForm = document.querySelector('#delete-list form')
  let confirmMessage = `Are you sure you want to delete ${listName}? <br>  This action cannot be undone. All items in this list will be deleted.`
  listForm.setAttribute('action', `/wishlist/delete/${listId}/`)
  paragraphElement.innerHTML = confirmMessage
  // append listForm as first child of paragraphElement
  listForm.prepend(paragraphElement)
}

// Open dialog & add list details to edit/delete form
openDialogButtons.forEach((button) => {
  button.addEventListener('click', async () => {
    initialWishlistName =
      button.parentElement.previousElementSibling.textContent
    const dialogId = button.getAttribute('data-wishlist-type')
    const dialog = document.querySelector(`dialog#${dialogId}-list`)
    dialog.showModal()

    // focus on the first input element if it exists
    dialog.querySelector('input[type=text]')?.focus()

    const form = dialog.querySelector('form')
    form.addEventListener('input', manageSubmitButtonState)

    if (dialogId === 'edit') {
      await handleEditList(button)
    }

    if (dialogId === 'delete') {
      handleDeleteList(button)
    }
  })
})
// Close dialog
closeDialogButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const dialog = button.closest('dialog')
    dialog.close()
  })
})

// Check if the value is not empty and not the same as the initial value
function isValueValid(value, initialValue) {
  return value !== '' && value !== initialValue
}
