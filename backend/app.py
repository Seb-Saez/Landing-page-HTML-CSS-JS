from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

db_config = {
    'host': 'db',
    'user': 'root',
    'password': 'root',
    'database': 'usuariosdb'
}

# Ruta para login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # Obtener datos JSON enviados desde frontend
    username = data.get('username')
    password = data.get('password')

    # Conectar a la base de datos
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    # Buscar usuario con username y password
    cursor.execute("SELECT * FROM usuarios WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:
        return jsonify({"success": True, "message": f"Bienvenido, {username}!"}), 200

    return jsonify({"success": False, "message": "Usuario o contraseña incorrectos"}), 401

# Ruta para registro
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO usuarios (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"success": True, "message": "Usuario registrado correctamente"}), 201

    except mysql.connector.IntegrityError:
        return jsonify({"success": False, "message": "El nombre de usuario ya existe"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
