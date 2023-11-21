// https://github.com/tailwindlabs/tailwindcss/blob/master/stubs/config.full.js

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html"],

  // || Overriding styles
  theme: {
    screens: {
      sm: "640px",
      md: "768px",
      lg: "1024px",
      xl: "1280px",
    },

    // || Additional styles
    extend: {
      fontFamily: {
        primary: ["Poppins", "sans-serif"],
      },
      colors: {
        text: {
          light: "hsl(213, 13%, 14%)",
          dark: "hsl(210, 67%, 96%)",
        },
        background: {
          "primary-light": "hsl(0, 0%, 100%)",
          "secondary-light": "hsl(210, 29%, 97%)",
          "primary-dark": "hsl(216, 28%, 7%)",
          "secondary-dark": "hsl(215, 21%, 11%)",
        },
        primary: {
          400: "hsl(213, 94%, 68%)",
          500: "hsl(217, 91%, 60%)",
          600: "hsl(221, 83%, 53%)",
        },
        danger: {
          light: "hsl(356, 71%, 48%)",
          dark: "hsl(3, 93%, 63%)",
        },
        success: {
          light: "#22c55e",
          dark: "#22c55e",
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

  plugins: [
    require("@tailwindcss/aspect-ratio"),
    require("@tailwindcss/container-queries"),
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
  ],
};
