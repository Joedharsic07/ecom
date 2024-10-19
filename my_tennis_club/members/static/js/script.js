
document.querySelector(".profile-icon").addEventListener("click", function () {
    var dropdown = document.querySelector(".dropdown-content");
    dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
});
window.addEventListener("click", function(event) {
    var dropdown = document.querySelector(".dropdown-content");
    if (!event.target.closest(".profile-dropdown")) {
        dropdown.style.display = "none";
    }
});
