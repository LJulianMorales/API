/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['api/static/css/style2.css'],
  theme: {
    extend: {},
  },
  plugins: [
    require('tailwindcss'),
    require('autoprefixer'),
  ],
}
