module.exports = {
  content: [
    'app/static/**/*.html',
    'app/static/**/*.js',
    'app/static/**/*.css',
  ],
  theme: {
    extend: {},
  },
  plugins: [   
     require('tailwindcss-rtl'),    // Ensure RTL support is correctly configured
  ],
}
