# Server Dockerfile
FROM python:3.10

WORKDIR /app/

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

COPY . .

CMD waitress-serve --call --port=$BACKEND_PORT app:create_app
