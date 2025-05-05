from flask import Flask, request, jsonify # type: ignore
import mysql.connector # type: ignore
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app)

# Conexión a la base de datos MySQL
db = mysql.connector.connect(
    host="mysql",  # Nombre del contenedor de MySQL en docker-compose
    user="usuario",  # Usuario definido en docker-compose
    password="clave",  # Contraseña definida en docker-compose
    database="flaskdb"  # Nombre de la base de datos
)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    
    if user:
        return jsonify({"message": "Login exitoso", "user": user})
    else:
        return jsonify({"message": "Credenciales incorrectas"}), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
