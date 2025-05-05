
Activar el cors

** en cmd:
pip install flask-cors


y el app.py

agregar algo as:
from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS  # Importar CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

