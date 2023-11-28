// Js Hint options added for assessor convenience

// Allows the JShint validator to recognise modern ES6 methods, such as
// `let`, `const`, `template literals`, `arrow functions (=>)`,
/* jshint esversion: 11 */

// Suppress warnings missing semicolons
/* jshint asi: true */

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './templates/**/*.html',
      './apps/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
