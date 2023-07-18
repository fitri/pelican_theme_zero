/** @type {import('tailwindcss').Config} */

module.exports = {
  content: ["./themes/zero/templates/*.html"],
  theme: {
    extend: {}
  },
  plugins: [
    require('@tailwindcss/typography')
  ]
};
