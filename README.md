# Anonimizador Web

Herramienta para anonimizar texto basada en la tarea https://github.com/PlanTL-GOB-ES/SPACCC_MEDDOCAN

El modelo se encuentra en https://huggingface.co/Dnidof/NER-MEDDOCAN

### Métricas obtenidas en el conjunto de test
<img width="489" alt="metricas del modelo" src="https://github.com/Dnidof/anonimizador/assets/88423658/68825ed1-0005-4f84-aa02-d8d5c98d31a9" />

### Ejemplo de documento pdf anonimizado
<img width="489" alt="documento anonimizado" src="https://github.com/user-attachments/assets/ed78d3a1-b485-47c8-9f27-532e86f49658" />

### Instrucciones

#### Construcción y Ejecución del Contenedor

Para construir y ejecutar el contenedor, sigue estos pasos:

1. **Construir la imagen Docker**:
   En el mismo directorio donde está el Dockerfile, ejecuta:
   ```sh
   docker build -t anonimizador_hitz2024 .
   ```
2. **Introducir archivos txt o pdf en la carpeta input**
3. **Ejecutar el contenedor (Powershell o bash)**:
   ```sh
   docker run -v ${PWD}:/app/ anonimizador_hitz2024
   ```

