# Anonimizador Web

Web local para anonimizar texto basada en la tarea https://github.com/PlanTL-GOB-ES/SPACCC_MEDDOCAN


El modelo se encuentra en https://huggingface.co/Dnidof/NER-MEDDOCAN

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

