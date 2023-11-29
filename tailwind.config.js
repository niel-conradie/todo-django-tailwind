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
        "background-primary": {
          light: "hsl(0, 0%, 100%)",
          dark: "hsl(216, 28%, 7%)",
        },
        "background-secondary": {
          light: "hsl(210, 29%, 97%)",
          dark: "hsl(215, 21%, 11%)",
        },
        primary: {
          light: "hsl(217, 91%, 60%)",
          dark: "hsl(217, 91%, 60%)",
        },
        danger: {
          light: "hsl(356, 71%, 48%)",
          dark: "hsl(3, 93%, 63%)",
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
