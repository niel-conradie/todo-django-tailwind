const accountDropdownIcon = document.getElementById("accountDropdownIcon");

try {
  accountDropdownIcon.addEventListener("click", () => {
    // dropdown menu toggle
    const accountDropdownMenu = document.getElementById("accountDropdownMenu");
    accountDropdownMenu.classList.toggle("hidden");

    // dropdown icon toggle
    const accountDropdownIconPath1 = document.getElementById(
      "accountDropdownIconPath1",
    );
    accountDropdownIconPath1.classList.toggle("stroke-text-light");
    accountDropdownIconPath1.classList.toggle("dark:stroke-text-dark");
    accountDropdownIconPath1.classList.toggle("stroke-primary-light");
    accountDropdownIconPath1.classList.toggle("dark:stroke-primary-dark");

    const accountDropdownIconPath2 = document.getElementById(
      "accountDropdownIconPath2",
    );
    accountDropdownIconPath2.classList.toggle("stroke-text-light");
    accountDropdownIconPath2.classList.toggle("dark:stroke-text-dark");
    accountDropdownIconPath2.classList.toggle("stroke-primary-light");
    accountDropdownIconPath2.classList.toggle("dark:stroke-primary-dark");
  });
} catch (error) {
  // console.error(error); // pass silently
}
