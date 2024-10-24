// Open dropdown
document.querySelector(".profile-icon").addEventListener("click", function () {
    var dropdown = document.querySelector(".dropdown-menu");
    if (dropdown) {
        dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
    } else {
        console.error(".dropdown-menu not found.");
    }
});

// Close dropdown on outside click
window.addEventListener("click", function (event) {
    var dropdown = document.querySelector(".dropdown-menu");
    if (dropdown && !event.target.closest(".profile-dropdown")) {
        dropdown.style.display = "none";
    }
});

// Wait for the DOM to load
document.addEventListener('DOMContentLoaded', function () {
    // Get the modal and the link to open it
    var modal = new bootstrap.Modal(document.getElementById('changePasswordModal'), {
        keyboard: false // prevents closing with ESC
    });
    var openModalLink = document.getElementById('changePasswordLink');
    var closeButton = document.querySelector('.btn-close');

    // Check if modal and openModalLink exist before adding event listeners
    if (modal && openModalLink) {
        // Open the modal
        openModalLink.addEventListener('click', function (event) {
            event.preventDefault();
            modal.show(); // Use Bootstrap's method to show the modal
        });
    } else {
        console.error("Modal or changePasswordLink not found.");
    }

    // Check if closeButton exists before adding event listener
    if (closeButton) {
        closeButton.addEventListener('click', function () {
            modal.hide(); // Use Bootstrap's method to hide the modal
        });
    } else {
        console.error("Close button not found.");
    }

    // Close modal when clicking outside
    window.addEventListener('click', function (event) {
        if (event.target.classList.contains('modal')) {
            modal.hide(); // Use Bootstrap's method to hide the modal
        }
    });

    // Toggle password visibility 
    document.getElementById('toggleCurrentPassword').onclick = function () {
        let input = document.getElementById('currentPassword');
        togglePassword(input, this);
    };

    document.getElementById('toggleNewPassword').onclick = function () {
        let input = document.getElementById('newPassword');
        togglePassword(input, this);
    };

    document.getElementById('toggleConfirmPassword').onclick = function () {
        let input = document.getElementById('confirmPassword');
        togglePassword(input, this);
    };

    function togglePassword(input, toggleButton) {
        if (input.type === 'password') {
            input.type = 'text';
            toggleButton.innerHTML = '<i class="fa fa-eye"></i>';
        } else {
            input.type = 'password';
            toggleButton.innerHTML = '<i class="fa fa-eye-slash"></i>';
        }
    }

    // Handle Change Password Form Submission via Fetch API
    var changePasswordForm = document.getElementById('changePasswordForm');
    if (changePasswordForm) {
        changePasswordForm.onsubmit = function (event) {
            event.preventDefault();

            const oldPassword = document.getElementById('currentPassword').value;
            const newPassword1 = document.getElementById('newPassword').value;
            const newPassword2 = document.getElementById('confirmPassword').value;
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            const formData = new FormData();
            formData.append('old_password', oldPassword);
            formData.append('new_password1', newPassword1);
            formData.append('new_password2', newPassword2);

            fetch('{% url "change_password" %}', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken
                },
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                document.querySelectorAll('.text-danger').forEach(el => el.textContent = '');

                if (data.success) {
                    alert(data.message);
                    modal.hide(); // Use Bootstrap's method to hide the modal
                    location.reload();
                } else {
                    if (data.errors.old_password) {
                        document.getElementById('oldPasswordError').textContent = data.errors.old_password;
                    }
                    if (data.errors.new_password) {
                        document.getElementById('newPasswordError').textContent = data.errors.new_password;
                    }
                    if (data.errors.new_password_length) {
                        document.getElementById('newPasswordLengthError').textContent = data.errors.new_password_length;
                    }
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        };
    } else {
        console.error("Change password form not found.");
    }
});
