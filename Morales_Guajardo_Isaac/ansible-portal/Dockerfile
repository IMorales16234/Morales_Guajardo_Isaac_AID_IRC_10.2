FROM python:3.9

# Instalar Flask y otras dependencias
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

# Copiar los archivos del portal web
COPY . /app
WORKDIR /app

# Exponer el puerto 5000
EXPOSE 5000

# Ejecutar la aplicación Flask
CMD ["python", "app.py"]
