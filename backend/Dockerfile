# Usamos Python 3.10 slim como base
FROM python:3.10-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos los archivos del backend al contenedor
COPY . /app

# Instalamos las dependencias necesarias
RUN pip install flask mysql-connector-python

# Exponemos el puerto 5000
EXPOSE 5000

# Comando para ejecutar la app Flask
CMD ["python", "app.py"]
