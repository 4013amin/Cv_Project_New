/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './cvAll/app/static/**/*.html',  // مسیر صحیح به فایل‌های HTML
    './cvAll/app/static/**/*.js',
    './cvAll/app/static/**/*.css',    // مسیر صحیح به فایل‌های JS
  ],
  theme: {
    extend: {},
  },
  plugins: [   
     require('tailwindcss-rtl'),    // Ensure RTL support is correctly configured
  ],
}
