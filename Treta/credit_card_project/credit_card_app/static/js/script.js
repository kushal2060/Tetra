function submitForm() {
    console.log('Submit button clicked');

    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var creditCard = document.getElementById('creditCard').value;

    console.log('Username:', username);
    console.log('Email:', email);
    console.log('Credit Card:', creditCard);

    if (!validateEmail(email)) {
        alert('Invalid email address');
        return;
    }

    var data = new FormData();
    data.append('username', username);
    data.append('email', email);
    data.append('encrypted_credit_card', creditCard);

    console.log('Data:', data);

    fetch('/credit_card/store_credit_card/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')  // Include CSRF token in the header
        },
        body: data
    })
    .then(response => response.json())
    .then(data => {
        console.log('Response:', data);
        // You can perform additional actions based on the server response
    })
    .catch(error => {
        console.error('Error:', error);
    });

    document.getElementById('userForm').reset();
}



function validateEmail(email) {
    // Simple email validation using a regular expression
    var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

function toggleCreditCardVisibility() {
    var creditCardInput = document.getElementById('creditCard');
    var eyeIcon = document.querySelector('.eye-icon');

    if (creditCardInput.type === 'password') {
        creditCardInput.type = 'text';
        eyeIcon.textContent = '👀';
    } else {
        creditCardInput.type = 'password';
        eyeIcon.textContent = '👁️';
    }
}

function openCreditCardRetrievalForm() {
    var modal = document.getElementById('creditCardRetrievalModal');
    modal.style.display = 'flex';
    console.log('Opening Credit Card Retrieval Form');
}

function closeCreditCardRetrievalForm() {
    var modal = document.getElementById('creditCardRetrievalModal');
    modal.style.display = 'none';
}
// Function to handle the response and update the UI




document.getElementById('retrieveBtn').addEventListener('click', function (event) {
    console.log('Button clicked!');// Call the retrieveCreditCard function when the button is clicked
    retrieveCreditCard(event);
});


function retrieveCreditCard(event) {
    // Prevent the default form submission
    event.preventDefault();
    var retrievalEmail = document.getElementById('retrievalEmail').value;
    console.log('Retrieved Email:', retrievalEmail);

    // Fetch data from the server
    fetch('/credit_card/retrieve_credit_card/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({email: document.getElementById('retrievalEmail').value }),
        
        
    })
    
    .then(response => {
        if (!response.ok) {
            throw new Error(`Error retrieving credit card information: ${response.statusText}`);
        }
        return response.json();
    })
    .then(data => {
        console.log('Received Data:', data);
        const decryptedCreditCardContainer = document.getElementById('decryptedCreditCardContainer');
        if (data.error) {
            alert(`Error retrieving credit card information: ${data.error}`);
        } else {
            // Display the decrypted credit card information on the frontend
            const creditCardData = data.credit_card;
            decryptedCreditCardContainer.innerHTML = `Decrypted Credit Card: ${creditCardData}`;
        }
    })
    
    
    console.log('Retrieved Email:', retrievalEmail);
    console.log('Sent retrieval request to the server');
}










// Update the retrieveCreditCard function to handle the response



// Function to get the CSRF token from the cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var retrieveBtn = document.getElementById('retrieveBtn');
if (retrieveBtn) {
    retrieveBtn.addEventListener('click', function (event) {
        retrieveCreditCard(event);
    });
}