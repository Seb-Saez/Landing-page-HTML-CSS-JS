document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('registerForm');
  const message = document.getElementById('message');

  form.addEventListener('submit', async function (e) {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
      const response = await fetch('/api/register', {  // <-- CAMBIO AQUÍ
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
      });

      const data = await response.json();

      if (response.ok) {
        message.innerText = data.message;
        message.style.color = 'green';
      } else {
        message.innerText = data.message;
        message.style.color = 'red';
      }
    } catch (error) {
      message.innerText = 'Error al conectar con el servidor';
      message.style.color = 'red';
      console.error('Error al conectar con el servidor:', error);
    }
  });
});
