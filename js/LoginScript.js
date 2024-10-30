function validateForm(event) {
    event.preventDefault();
    
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const emailError = document.getElementById('emailError');
    const passwordError = document.getElementById('passwordError');
    
    emailError.textContent = '';
    passwordError.textContent = '';
    
    let isValid = true;
    
    if (!email) {
        emailError.textContent = 'L\'email è richiesta';
        isValid = false;
    } else if (!/\S+@\S+\.\S+/.test(email)) {
        emailError.textContent = 'Inserisci un indirizzo email valido';
        isValid = false;
    }
    
    if (!password) {
        passwordError.textContent = 'La password è richiesta';
        isValid = false;
    } else if (password.length < 6) {
        passwordError.textContent = 'La password deve contenere almeno 6 caratteri';
        isValid = false;
    }
    
    if (isValid) {
        console.log('Form submitted:', { email, password });
        alert('Login effettuato con successo!');
    }
    
    return isValid;
}
