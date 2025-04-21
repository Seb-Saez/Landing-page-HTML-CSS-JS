from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Conexión a la base de datos MySQL
db = mysql.connector.connect(
    host="mysql",
    user="usuario",
    password="clave",
    database="flaskdb"
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
