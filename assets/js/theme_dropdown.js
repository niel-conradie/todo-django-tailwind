const themeDropdownIcon = document.getElementById("themeDropdownIcon");

try {
  themeDropdownIcon.addEventListener("click", () => {
    // dropdown menu toggle
    const themeDropdownMenu = document.getElementById("themeDropdownMenu");
    themeDropdownMenu.classList.toggle("hidden");

    // light theme icon toggle
    const lightThemeDropdownIconPath1 = document.getElementById(
      "lightThemeDropdownIconPath1",
    );
    lightThemeDropdownIconPath1.classList.toggle("stroke-text-light");
    lightThemeDropdownIconPath1.classList.toggle("dark:stroke-text-dark");
    lightThemeDropdownIconPath1.classList.toggle("stroke-primary-light");
    lightThemeDropdownIconPath1.classList.toggle("dark:stroke-primary-dark");

    const lightThemeDropdownIconPath2 = document.getElementById(
      "lightThemeDropdownIconPath2",
    );
    lightThemeDropdownIconPath2.classList.toggle("stroke-text-light");
    lightThemeDropdownIconPath2.classList.toggle("dark:stroke-text-dark");
    lightThemeDropdownIconPath2.classList.toggle("stroke-primary-light");
    lightThemeDropdownIconPath2.classList.toggle("dark:stroke-primary-dark");

    // dark theme icon toggle
    const darkThemeDropdownIconPath1 = document.getElementById(
      "darkThemeDropdownIconPath1",
    );
    darkThemeDropdownIconPath1.classList.toggle("fill-text-light");
    darkThemeDropdownIconPath1.classList.toggle("dark:fill-text-dark");
    darkThemeDropdownIconPath1.classList.toggle("fill-primary-light");
    darkThemeDropdownIconPath1.classList.toggle("dark:fill-primary-dark");

    const darkThemeDropdownIconPath2 = document.getElementById(
      "darkThemeDropdownIconPath2",
    );
    darkThemeDropdownIconPath2.classList.toggle("fill-text-light");
    darkThemeDropdownIconPath2.classList.toggle("dark:fill-text-dark");
    darkThemeDropdownIconPath2.classList.toggle("fill-primary-light");
    darkThemeDropdownIconPath2.classList.toggle("dark:fill-primary-dark");

    // system theme icon toggle
    const systemThemeDropdownIconPath1 = document.getElementById(
      "systemThemeDropdownIconPath1",
    );
    systemThemeDropdownIconPath1.classList.toggle("stroke-text-light");
    systemThemeDropdownIconPath1.classList.toggle("dark:stroke-text-dark");
    systemThemeDropdownIconPath1.classList.toggle("stroke-primary-light");
    systemThemeDropdownIconPath1.classList.toggle("dark:stroke-primary-dark");

    const systemThemeDropdownIconPath2 = document.getElementById(
      "systemThemeDropdownIconPath2",
    );
    systemThemeDropdownIconPath2.classList.toggle("stroke-text-light");
    systemThemeDropdownIconPath2.classList.toggle("dark:stroke-text-dark");
    systemThemeDropdownIconPath2.classList.toggle("stroke-primary-light");
    systemThemeDropdownIconPath2.classList.toggle("dark:stroke-primary-dark");
  });
} catch (error) {
  // console.error(error); // pass silently
}
