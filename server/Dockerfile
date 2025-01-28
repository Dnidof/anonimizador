# Usa una imagen base de Python 3.10
FROM python:3.10

# Establece el directorio de trabajo en /app/
WORKDIR /app/

# Actualiza pip
RUN pip install --upgrade pip

# Instala las dependencias directamente
# Cache con las dependencias: https://jpetazzo.github.io/2013/12/01/docker-python-pip-requirements/
RUN pip install Flask==3.0.3
RUN pip install Flask-Cors==4.0.1
RUN pip install transformers==4.41.2
RUN pip install PyPDF2==3.0.1
RUN pip install torch==2.3.1
RUN pip install torchaudio==2.3.1
RUN pip install torchvision==0.18.1

COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia el contenido de la carpeta actual en el sistema anfitrión al directorio de trabajo en el contenedor
COPY .. .

# Exponer el puerto 4444 para Flask (opcional, solo para documentación)
EXPOSE 4444

# Comando por defecto para ejecutar la aplicación Flask
CMD ["python", "app.py"]
