# Anonimizador Web

Web local para anonimizar texto basada en la tarea https://github.com/PlanTL-GOB-ES/SPACCC_MEDDOCAN

![image](https://github.com/Dnidof/anonimizador/assets/88423658/be8542aa-b181-4870-bc4d-a784576e6c4b)

El modelo se encuentra en https://huggingface.co/Dnidof/NER-MEDDOCAN

![image](https://github.com/Dnidof/anonimizador/assets/88423658/68825ed1-0005-4f84-aa02-d8d5c98d31a9)


### Instrucciones

#### Construcción y Ejecución del Contenedor

Para construir y ejecutar el contenedor, sigue estos pasos:

1. **Construir la imagen Docker**:
   En el mismo directorio donde está el Dockerfile, ejecuta:
   ```sh
   docker build -t anonimizador_hitz2024 .
   ```

2. **Ejecutar el contenedor**:
   ```sh
   docker run -p 127.0.0.1:4444:4444 anonimizador_hitz2024
   ```

