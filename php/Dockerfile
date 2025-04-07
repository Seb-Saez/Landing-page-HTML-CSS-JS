# Imagen base de Ubuntu
FROM ubuntu:22.04

# Evitar preguntas en instalaciones (modo no interactivo)
#ENV DEBIAN_FRONTEND=noninteractive

# Actualizamos paquetes y instalamos Apache2
RUN apt-get update && apt-get install -y apache2

# Copiamos los archivos del proyecto al directorio web de Apache
#COPY ./codigo/ /var/www/html

# Exponemos el puerto por donde sirve Apache
EXPOSE 80

# Comando para mantener Apache corriendo en primer plano
CMD ["apachectl", "-D", "FOREGROUND"]
