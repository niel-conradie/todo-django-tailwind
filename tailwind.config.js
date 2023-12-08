// https://github.com/tailwindlabs/tailwindcss/blob/master/stubs/config.full.js

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./assets/js/**/*.js"],
  darkMode: "class",

  // || Overriding styles
  theme: {
    // | Breakpoints
    screens: {
      sm: "640px",
      md: "768px",
      lg: "1024px",
      xl: "1280px",
    },

    // || Additional styles
    extend: {
      // | Typography
      fontFamily: {
        primary: ["Poppins", "sans-serif"],
      },

      // | Background Images
      backgroundImage: {
        light: "url('/static/images/background-light.jpg')",
        dark: "url('/static/images/background-dark.jpg')",
      },

      // | Color Pallette
      colors: {
        text: {
          light: "hsl(213, 13%, 14%)",
          dark: "hsl(210, 67%, 96%)",
        },
        background: {
          primary: {
            light: "hsl(0, 0%, 100%)",
            dark: "hsl(216, 28%, 7%)",
          },
          secondary: {
            light: "hsl(210, 29%, 97%)",
            dark: "hsl(215, 21%, 11%)",
          },
        },
        primary: {
          light: "hsl(217, 91%, 60%)",
          dark: "hsl(217, 91%, 60%)",
        },
        success: {
          light: "hsl(142, 71%, 45%)",
          dark: "hsl(142, 71%, 45%)",
        },
        error: {
          light: "hsl(356, 71%, 48%)",
          dark: "hsl(3, 93%, 63%)",
        },
        danger: {
          light: "hsl(356, 71%, 48%)",
          dark: "hsl(3, 93%, 63%)",
        },
        warning: {
          light: "hsl(45, 93%, 47%)",
          dark: "hsl(45, 93%, 47%)",
        },
        info: {
          light: "hsl(142, 71%, 45%)",
          dark: "hsl(142, 71%, 45%)",
        },
        border: {
          light: "hsl(216, 12%, 84%)",
          dark: "hsl(215, 28%, 17%)",
        },
        shadow: {
          light: "hsl(216, 12%, 84%)",
        },
      },
    },
  },

  plugins: [],
};
