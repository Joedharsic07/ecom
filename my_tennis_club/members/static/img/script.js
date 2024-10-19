
// login password eye button
function togglePasswordVisibility() {
    const passwordField = document.getElementById('pwd');
    const toggleIcon = document.getElementById('toggleIcon');
    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        toggleIcon.classList.remove('bi-eye');
        toggleIcon.classList.add('bi-eye-slash');
    } else {
        passwordField.type = 'password';
        toggleIcon.classList.remove('bi-eye-slash');
        toggleIcon.classList.add('bi-eye');
    }
}
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const usernameInput = document.getElementById('username');
    const emailInput = document.getElementById('E-mail');
    const passwordInput = document.getElementById('password');
    const confirmPasswordInput = document.getElementById('confirmPassword');
    
    const usernameError = document.getElementById('usernameError');
    const emailError = document.getElementById('emailError');
    const passwordError = document.getElementById('passwordError');
    const confirmPasswordError = document.getElementById('confirmPasswordError');

    form.addEventListener('submit', function(event) {
        let isValid = true;

        // Clear previous error messages
        usernameError.textContent = '';
        emailError.textContent = '';
        passwordError.textContent = '';
        confirmPasswordError.textContent = '';

        // Username validation (at least 3 characters)
        if (usernameInput.value.trim().length < 3) {
            usernameError.textContent = 'Username must be at least 3 characters long.';
            isValid = false;
        }

        // Email validation
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(emailInput.value)) {
            emailError.textContent = 'Please enter a valid email address.';
            isValid = false;
        }

        // Password validation (at least 8 characters)
        if (passwordInput.value.length < 8) {
            passwordError.textContent = 'Password must be at least 8 characters long.';
            isValid = false;
        }

        // Confirm password validation
        if (confirmPasswordInput.value !== passwordInput.value) {
            confirmPasswordError.textContent = 'Passwords do not match.';
            isValid = false;
        }

        // Prevent form submission if validation fails
        if (!isValid) {
            event.preventDefault();
        }
    });
});




// confirm password eye button
function toggleConfirmPasswordVisibility(){
    const passwordField = document.getElementById('confirmPassword');
    const toggleIcon = document.getElementById('toggleIcon1');
    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        toggleIcon.classList.remove('bi-eye');
        toggleIcon.classList.add('bi-eye-slash');
    } else {
        passwordField.type = 'password';
        toggleIcon.classList.remove('bi-eye-slash');
        toggleIcon.classList.add('bi-eye');
    }
}
// regpassword eye button
function togglePassword() {
    const passwordField = document.getElementById('password');
    const toggleIcon1 = document.getElementById('toggleIcon');

    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        toggleIcon1.classList.remove('bi-eye');
        toggleIcon1.classList.add('bi-eye-slash');
    } else {
        passwordField.type = 'password';
        toggleIcon1.classList.remove('bi-eye-slash');
        toggleIcon1.classList.add('bi-eye');
    }
}


// /save reg data in local storage
// Function to handle user registration



function togglePasswordVisibility() {
    const passwordField = document.getElementById('pwd');
    const toggleIcon = document.getElementById('toggleIcon');
    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        toggleIcon.classList.remove('bi-eye');
        toggleIcon.classList.add('bi-eye-slash');
    } else {
        passwordField.type = 'password';
        toggleIcon.classList.remove('bi-eye-slash');
        toggleIcon.classList.add('bi-eye');
    }
}


document.addEventListener('DOMContentLoaded', function() {
    function saveData(event) {
        event.preventDefault();
        
        // Get input values
        const fname = document.getElementById('fname').value.trim();
        const lname = document.getElementById('lname').value.trim();
        const username = document.getElementById('username').value.trim();
        const password = document.getElementById('password').value.trim();
        const confirmPassword = document.getElementById('confirmPassword').value.trim();
        const email = document.getElementById('E-mail').value.trim();
    
        // Clear previous error messages
        document.getElementById('usernameError').textContent = '';
        document.getElementById('emailError').textContent = '';
        document.getElementById('passwordError').textContent = '';
        document.getElementById('confirmPasswordError').textContent = '';
    
        let hasError = false;
    
        // Validate username
        const usernamePattern = /^[a-zA-Z0-9_]+$/;
        if (username === '') {
            document.getElementById('usernameError').textContent = 'Username is required.';
            hasError = true;
        } else if (!usernamePattern.test(username)) {
            document.getElementById('usernameError').textContent = 'Username should only contain letters, numbers, and underscores.';
            hasError = true;
        }
    
        // Validate email
        if (email === '') {
            document.getElementById('emailError').textContent = 'Email is required.';
            hasError = true;
        } else if (!validateEmail(email)) {
            document.getElementById('emailError').textContent = 'Please enter a valid email address.';
            hasError = true;
        }
    
        // Validate password
        const passwordPattern = /^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
        if (password === '') {
            document.getElementById('passwordError').textContent = 'Password is required.';
            hasError = true;
        } else if (!passwordPattern.test(password)) {
            document.getElementById('passwordError').textContent = 'Password must contain at least 8 characters, including uppercase, number, and special character.';
            hasError = true;
        }
    
        // Validate confirm password
        if (confirmPassword === '') {
            document.getElementById('confirmPasswordError').textContent = 'Confirm Password is required.';
            hasError = true;
        } else if (confirmPassword !== password) {
            document.getElementById('confirmPasswordError').textContent = 'Passwords do not match.';
            hasError = true;
        }
    
        if (hasError) {
            return; // Exit the function if there are validation errors
        }
    
        // Retrieve existing data or initialize an empty array
        let reg;
        try {
            reg = JSON.parse(localStorage.getItem('Data')) || [];
        } catch (e) {
            console.error('Error retrieving data from localStorage:', e);
            reg = [];
        }
        console.log('Retrieved data:', reg);
    
        // Check if the email already exists
        if (reg.some(user => user.email === email)) {
            document.getElementById('emailError').textContent = 'E-mail already exists';
        } else {
            // Add the new registration data to the array
            reg.push({
                "firstName": fname,
                "lastName": lname,
                "username": username,
                "password": password, // Consider hashing the password before storing
                "email": email
            });
    
            // Save the updated array back to local storage
            localStorage.setItem('Data', JSON.stringify(reg));
            alert('Registration successful');
        }
    }    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', saveData);
    }
});



// Function to validate email format
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

// Function to handle user login and validation
function loginData(event) {
    event.preventDefault();
    const username = document.getElementById('name').value;
    const password = document.getElementById('pwd').value;

    console.log("Entered Username: ", username);
    console.log("Entered Password: ", password);

    // Basic validation for username and password
    const usernameError = document.getElementById('usernameError');
    const passwordError = document.getElementById('passwordError');

    // Clear previous error messages
    usernameError.textContent = '';
    passwordError.textContent = '';

    const passwordPattern = /^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    const usernamePattern = /^[a-zA-Z0-9_]+$/; // Username should only contain alphanumeric characters and underscores

    let hasError = false;

    // Check if the username is not empty
    if (username.trim() === '') {
        usernameError.textContent = 'Username is required.';
        hasError = true;
    } else if (!usernamePattern.test(username)) {
        usernameError.textContent = 'Username should only contain letters, numbers, and underscores.';
        hasError = true;
    }

    // Check if the password is not empty
    if (password.trim() === '') {
        passwordError.textContent = 'Password is required.';
        hasError = true;
    } else if (!passwordPattern.test(password)) {
        passwordError.textContent = 'Wrong Password.';
        hasError = true;
    }

    if (hasError) {
        return; // Stop processing if there are validation errors
    }

    // Retrieve the stored data from local storage
    let reg = JSON.parse(localStorage.getItem('Data')) || [];
    console.log("Stored Data: ", reg);

    // Check if the username and password match any stored user
    const currentUser = reg.find((user) => user.username === username && user.password === password);
    console.log("Matched User: ", currentUser);

    if (currentUser) {
        alert("Login successful");
        localStorage.setItem("currentUser", JSON.stringify(currentUser));
        window.location.href = "./home.html";
    } else {
        alert("Invalid username or password");
    }
}

// Function to display the logged-in user's name in the dropdown
function displayLoggedInUser() {
    const currentUser = JSON.parse(localStorage.getItem("currentUser"));
    if (currentUser) {
        document.getElementById("profile-username").textContent = currentUser.username;
    } else {
        console.error('No logged-in user found in local storage.');
    }
}

// Toggle dropdown visibility on profile icon click
document.querySelector(".profile-icon").addEventListener("click", function () {
    var dropdown = document.querySelector(".dropdown-content");
    dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
});

// Close dropdown if clicked outside
window.addEventListener("click", function(event) {
    var dropdown = document.querySelector(".dropdown-content");
    if (!event.target.closest(".profile-dropdown")) {
        dropdown.style.display = "none";
    }
});
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('logout-btn').addEventListener('click', function() {
      // Clear user data from local storage
      localStorage.removeItem('currentUser'); // Adjust the key if necessary

      // Redirect to the login page
      window.location.href = 'login.html'; // Change to your actual login page URL
    });
  });
// Call the function to display the username when the page loads
window.onload = displayLoggedInUser;

// Add event listener for the login form
document.getElementById('login-form').addEventListener('submit', loginData);







