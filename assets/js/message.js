// remove success message from html
function removeMessage() {
  const message = document.getElementById("message");
  if (message) {
    message.remove();
  }
}

try {
  window.addEventListener("load", () => {
    // wait before removing the message
    setTimeout(removeMessage, 2500);
  });
} catch (error) {
  // console.error(error); // pass silently
}
