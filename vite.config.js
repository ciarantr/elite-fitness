// Js Hint options added for assessor convenience
// Suppress warnings missing semicolons and set es versions number

/* jshint esversion: 11, asi: true */

import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
  root: resolve('./static/'),
  base: '/static/',

  build: {
    manifest: true,
    emptyOutDir: true,
    outDir: resolve('./static/dist'),
    assetsDir: '',
    rollupOptions: {
      input: {
        css: resolve('./static/js/css-import.js'),
        main: resolve('./static/js/main.js'),
        stripe: resolve('./static/js/stripe.js'),
        wishlist: resolve('./static/js/wishlist.js'),
      },
    },
  },
  css: {
    postcss: resolve('./config/postcss.config.js'),
  },
})
