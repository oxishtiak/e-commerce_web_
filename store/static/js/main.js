// Add any custom JavaScript here
console.log("E-Commerce Store loaded successfully!");

// Example: Confirm before removing items from cart
document.addEventListener("DOMContentLoaded", function () {
   // Add smooth scroll behavior
   document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
      anchor.addEventListener("click", function (e) {
         e.preventDefault();
         const target = document.querySelector(this.getAttribute("href"));
         if (target) {
            target.scrollIntoView({
               behavior: "smooth",
            });
         }
      });
   });
});
