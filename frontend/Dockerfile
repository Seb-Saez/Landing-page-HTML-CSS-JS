# frontend/Dockerfile

FROM nginx:latest

# Copiar configuración personalizada de nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copiar todo el contenido del frontend al directorio por defecto de nginx
COPY . /usr/share/nginx/html

# Exponer el puerto 80 (opcional, ya que Nginx usa ese puerto por defecto)
EXPOSE 80
