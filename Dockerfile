# Usa una imagen base de Python 3.10
FROM python:3.10

# Establece el directorio de trabajo en /app
WORKDIR /app

# Actualiza pip
RUN pip install --upgrade pip

# Instala las dependencias directamente
# Cache con las dependencias: https://jpetazzo.github.io/2013/12/01/docker-python-pip-requirements/
RUN pip install flask
RUN pip install flask-cors
RUN pip install transformers
RUN pip install PyPDF2
RUN pip install torch
RUN pip install torchvision
RUN pip install torchaudio

# Copia el contenido de la carpeta actual en el sistema anfitrión al directorio de trabajo en el contenedor
COPY . .

# Establece la variable de entorno para que Flask escuche solo en localhost
ENV FLASK_RUN_HOST=127.0.0.1

# Exponer el puerto 5000 para Flask (opcional, solo para documentación)
EXPOSE 5000

# Comando por defecto para ejecutar la aplicación Flask
CMD ["flask", "run"]
