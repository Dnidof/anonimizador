# Usa una imagen base de Python 3.10
FROM python:3.10

# Actualiza pip
RUN pip install --upgrade pip

# Instala las dependencias directamente
RUN pip install flask flask-cors transformers PyPDF2 torch torchvision torchaudio

# Establece la variable de entorno para que Flask escuche solo en localhost
ENV FLASK_RUN_HOST=127.0.0.1

# Exponer el puerto 4444 para Flask (opcional, solo para documentación)
EXPOSE 4444

# Comando por defecto para ejecutar la aplicación Flask
CMD ["flask", "run"]