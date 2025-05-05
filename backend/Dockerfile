# Usamos Python 3.10 slim como base
FROM python:3.10-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos el archivo de dependencias primero para aprovechar la cache de Docker
COPY requirements.txt /app/requirements.txt

# Instalamos las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de los archivos del backend al contenedor
COPY . /app

# Exponemos el puerto 5000
EXPOSE 5000

# Comando para ejecutar la app Flask
CMD ["python", "app.py"]
