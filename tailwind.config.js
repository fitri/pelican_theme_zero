/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./themes/zero/templates/*.html"],
  theme: {
    extend: {
      fontFamily: {
        custom: ['Montserrat', 'sans-serif']
      },
      fontWeight: {
        regular: 400,
        medium: 500,
        semibold: 600,
        extrabold:800,
        black:900
        },
      typography: (theme) => ({
        DEFAULT: {
          css: {
            'h1': {
              '@apply mr-5': {},
            }
          }
        }
      })
    }
  },
  plugins: []
};
