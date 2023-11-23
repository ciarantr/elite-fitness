// Js Hint options added for assessor convenience

// Allows the JShint validator to recognise modern ES6 methods, such as
// `let`, `const`, `template literals`, `arrow functions (=>)`,
/* jshint esversion: 11 */

// Suppress warnings missing semicolons
/* jshint asi: true */

const stripePublicKeyEl = document.querySelector('#stripe_public_key')
const clientSecretEl = document.querySelector('#client_secret')
const cardEl = document.querySelector('#card-element')
const form = document.querySelector('#payment-form')
const dialog = document.getElementById('process-order')

// Extract values without surrounding quotes
const stripePublicKey = stripePublicKeyEl.textContent.trim().slice(1, -1)
const clientSecret = clientSecretEl.textContent.trim().slice(1, -1)

// Initialize Stripe and Elements
const stripe = Stripe(stripePublicKey)
const elements = stripe.elements()
const style = {
  base: {
    color: '#32325d',
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '16px',
    '::placeholder': {
      color: '#201d1d',
    },
  },
  invalid: {
    color: '#fa755a',
    iconColor: '#fa755a',
  },
}
const card = elements.create('card', { style: style })
card.mount(cardEl)

// Card change event
card.addEventListener('change', (event) => {
  let errorDiv = document.getElementById('card-errors')
  if (event.error) {
    let html = `<span>${event.error.message}</span>`
    errorDiv.innerHTML = html
  } else {
    errorDiv.textContent = ''
  }
})

// Handle form submit

form.addEventListener('submit', async function (event) {
  event.preventDefault()
  card.update({ disabled: true })
  dialog.showModal()
  const saveInfo = Boolean(
    document.querySelector('#id-save-info')?.checked ?? false,
  )
  const csrfToken = document.querySelector('[name="csrfmiddlewaretoken"]').value
  const postData = {
    csrfmiddlewaretoken: csrfToken,
    client_secret: clientSecret,
    save_info: saveInfo,
  }

  const url = '/checkout/cache-checkout-data/'

  const billingDetails = {
    name: form.full_name.value.trim(),
    phone: form.phone_number.value.trim(),
    email: form.email.value.trim(),
    address: {
      line1: form.street_address1.value.trim(),
      line2: form.street_address2.value.trim(),
      city: form.town_or_city.value.trim(),
      country: form.country.value.trim(),
      state: form.county.value.trim(),
    },
  }

  const shippingDetails = {
    name: form.full_name.value.trim(),
    phone: form.phone_number.value.trim(),
    address: {
      line1: form.street_address1.value.trim(),
      line2: form.street_address2.value.trim(),
      city: form.town_or_city.value.trim(),
      country: form.country.value.trim(),
      postal_code: form.postcode.value.trim(),
      state: form.county.value.trim(),
    },
  }

  try {
    await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
      },
      body: JSON.stringify(postData),
    }).then((response) => {
      if (response.ok) {
        stripe
          .confirmCardPayment(clientSecret, {
            payment_method: {
              card: card,
              billing_details: billingDetails,
            },
            shipping: shippingDetails,
          })
          .then((result) => {
            if (result.error) {
              const displayError = document.getElementById('card-errors')
              displayError.textContent = result.error.message
              card.update({ disabled: false })
              document.querySelector('#submit-button').disabled = false
              dialog.close()
            } else {
              if (result.paymentIntent.status === 'succeeded') {
                document.querySelector('#submit-button').disabled = false
                // close dialog & submit form
                dialog.close()
                form.submit()
              }
            }
          })
      } else {
        location.reload()
      }
    })
  } catch (error) {
    console.log(error)
  }
})
