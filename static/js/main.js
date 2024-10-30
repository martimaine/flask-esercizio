document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('registrationForm');
  form.addEventListener('submit', function(event) {
      event.preventDefault();

      const nome = document.getElementById('nome').value;
      const cognome = document.getElementById('cognome').value;
      const email = document.getElementById('email').value;


      const data = { nome, cognome, email };
      fetch('/partecipanti', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data)
      })
      .then(response => response.json())
      .then(data => {
          if (data.error) {
              document.getElementById('responseMessage').innerHTML = `<p class="text-danger">${data.error}</p>`;
          } else {
              document.getElementById('responseMessage').innerHTML = `<p class="text-success">Registration successful! Your ID is ${data.id}</p>`;
              form.reset();  
          }
      })
      .catch(error => console.error('Error:', error));
  });
});
