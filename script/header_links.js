document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".headerlink").forEach(anchor => {
    anchor.addEventListener("click", event => {
      event.preventDefault();

      const url = new URL(window.location.href);
      url.hash = anchor.getAttribute("href");

      navigator.clipboard.writeText(url.toString());
    });
  });
});