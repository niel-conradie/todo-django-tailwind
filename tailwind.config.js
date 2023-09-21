/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./pages/templates/**/*.html"],

  // || Overriding styles
  theme: {
    // screens: {
    //   sm: "640px",
    //   md: "768px",
    //   lg: "1024px",
    //   xl: "1280px",
    // },

    // || Additional styles
    extend: {
      // fontFamily: {
      //   primary: ["Roboto", "sans-serif"],
      //   secondary: ["Merriweather", "serif"],
      // },
      // colors: {
      //   spotify: {
      //     50: "",
      //     100: "",
      //     200: "",
      //     300: "",
      //     400: "",
      //     500: "",
      //     600: "",
      //     700: "",
      //     800: "",
      //     900: "",
      //     950: "",
      //   },
      // },
    },
  },

  plugins: [
    require("@tailwindcss/aspect-ratio"),
    require("@tailwindcss/container-queries"),
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
  ],
};