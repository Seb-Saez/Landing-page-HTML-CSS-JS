document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector(".login-formulario");

    form.addEventListener('submit', async function (event) {
        event.preventDefault();

        const username = document.querySelector(".usuario").value;
        const password = document.querySelector(".clave").value;

        try {
            const response = await fetch('http://localhost:5000/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password }),
            });

            const result = await response.json();

            if (response.ok) {
                alert('Bienvenido: ' + result.user.username);
            } else {
                alert('Error: ' + result.message);
            }
        } catch (error) {
            alert('Hubo un problema con la solicitud: ' + error.message);
        }
    });
});
