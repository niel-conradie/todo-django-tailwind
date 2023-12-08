const lightTheme = document.getElementById("lightTheme");
const darkTheme = document.getElementById("darkTheme");
const systemTheme = document.getElementById("systemTheme");

// set local storage theme to light
function setLightTheme() {
  localStorage.theme = "light";
  document.documentElement.classList.remove("dark");
}

// set local storage theme to dark
function setDarkTheme() {
  localStorage.theme = "dark";
  document.documentElement.classList.add("dark");
}

// remove local storage theme and use system preferences
function setSystemTheme() {
  localStorage.removeItem("theme");
}

// update theme icons based on local storage settings
function updateThemeIcons() {
  try {
    if (localStorage.theme === "light") {
      // add active theme icon
      const lightThemeDropdownIcon = document.getElementById(
        "lightThemeDropdownIcon",
      );
      lightThemeDropdownIcon.classList.remove("hidden");

      // update active theme icon class values
      const lightThemeDropdownMenuIconPath1 = document.getElementById(
        "lightThemeDropdownMenuIconPath1",
      );
      lightThemeDropdownMenuIconPath1.classList.remove("stroke-text-light");
      lightThemeDropdownMenuIconPath1.classList.remove("dark:stroke-text-dark");
      lightThemeDropdownMenuIconPath1.classList.add("stroke-primary-light");
      lightThemeDropdownMenuIconPath1.classList.add("dark:stroke-primary-dark");

      const lightThemeDropdownMenuIconPath2 = document.getElementById(
        "lightThemeDropdownMenuIconPath2",
      );
      lightThemeDropdownMenuIconPath2.classList.remove("stroke-text-light");
      lightThemeDropdownMenuIconPath2.classList.remove("dark:stroke-text-dark");
      lightThemeDropdownMenuIconPath2.classList.add("stroke-primary-light");
      lightThemeDropdownMenuIconPath2.classList.add("dark:stroke-primary-dark");

      // remove inactive theme icons
      darkThemeDropdownIcon.classList.add("hidden");
      systemThemeDropdownIcon.classList.add("hidden");
    } else if (localStorage.theme === "dark") {
      // add active theme icon
      const darkThemeDropdownIcon = document.getElementById(
        "darkThemeDropdownIcon",
      );
      darkThemeDropdownIcon.classList.remove("hidden");

      // update active theme icon class values
      const darkThemeDropdownMenuIconPath1 = document.getElementById(
        "darkThemeDropdownMenuIconPath1",
      );
      darkThemeDropdownMenuIconPath1.classList.remove("fill-text-light");
      darkThemeDropdownMenuIconPath1.classList.remove("dark:fill-text-dark");
      darkThemeDropdownMenuIconPath1.classList.add("fill-primary-light");
      darkThemeDropdownMenuIconPath1.classList.add("dark:fill-primary-dark");

      const darkThemeDropdownMenuIconPath2 = document.getElementById(
        "darkThemeDropdownMenuIconPath2",
      );
      darkThemeDropdownMenuIconPath2.classList.remove("fill-text-light");
      darkThemeDropdownMenuIconPath2.classList.remove("dark:fill-text-dark");
      darkThemeDropdownMenuIconPath2.classList.add("fill-primary-light");
      darkThemeDropdownMenuIconPath2.classList.add("dark:fill-primary-dark");

      // remove inactive theme icons
      lightThemeDropdownIcon.classList.add("hidden");
      systemThemeDropdownIcon.classList.add("hidden");
    } else {
      // add active theme icon
      const systemThemeDropdownIcon = document.getElementById(
        "systemThemeDropdownIcon",
      );
      systemThemeDropdownIcon.classList.remove("hidden");

      // update active theme icon class values
      const systemThemeDropdownMenuIconPath1 = document.getElementById(
        "systemThemeDropdownMenuIconPath1",
      );
      systemThemeDropdownMenuIconPath1.classList.remove("stroke-text-light");
      systemThemeDropdownMenuIconPath1.classList.remove(
        "dark:stroke-text-dark",
      );
      systemThemeDropdownMenuIconPath1.classList.add("stroke-primary-light");
      systemThemeDropdownMenuIconPath1.classList.add(
        "dark:stroke-primary-dark",
      );

      const systemThemeDropdownMenuIconPath2 = document.getElementById(
        "systemThemeDropdownMenuIconPath2",
      );
      systemThemeDropdownMenuIconPath2.classList.remove("stroke-text-light");
      systemThemeDropdownMenuIconPath2.classList.remove(
        "dark:stroke-text-dark",
      );
      systemThemeDropdownMenuIconPath2.classList.add("stroke-primary-light");
      systemThemeDropdownMenuIconPath2.classList.add(
        "dark:stroke-primary-dark",
      );

      // remove inactive theme icons
      lightThemeDropdownIcon.classList.add("hidden");
      darkThemeDropdownIcon.classList.add("hidden");
    }
  } catch (error) {
    // console.error(error); // pass silently
  }
}

// activate the light theme
try {
  lightTheme.addEventListener("click", () => {
    setLightTheme();
    location.reload(); // force reload
  });
} catch (error) {
  // console.error(error); // pass silently
}

// activate the dark theme
try {
  darkTheme.addEventListener("click", () => {
    setDarkTheme();
    location.reload(); // force reload
  });
} catch (error) {
  // console.error(error); // pass silently
}

// activate the system preference theme
try {
  systemTheme.addEventListener("click", () => {
    setSystemTheme();
    location.reload(); // force reload
  });
} catch (error) {
  // console.error(error); // pass silently
}

// on load update theme icons
try {
  window.addEventListener("load", () => {
    updateThemeIcons();
  });
} catch (error) {
  // console.error(error); // pass silently
}
