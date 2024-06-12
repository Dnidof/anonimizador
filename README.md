# Anonimizador Web

Web local para anonimizar texto basada en la tarea https://github.com/PlanTL-GOB-ES/SPACCC_MEDDOCAN


### Instrucciones

#### Windows

1. **Instalar Python 3.10**:
   - Descarga Python 3.10 desde [python.org](https://www.python.org/downloads/).
   - Durante la instalación, selecciona la opción "Add Python to PATH".

2. **Abrir el Símbolo del Sistema**:
   - Presiona `Win + R`, escribe `cmd` y presiona Enter.

3. **Crear y Activar un Entorno Virtual**:
   - Navega a la carpeta donde quieres crear el entorno virtual usando `cd ruta/a/tu/carpeta`.
   - Crea el entorno virtual ejecutando:
     ```sh
     python -m venv nombre_del_entorno
     ```
   - Activa el entorno virtual:
     ```sh
     nombre_del_entorno\Scripts\activate
     ```

4. **Actualizar pip y Configurar pip para Python 3.10**:
   - Actualiza pip:
     ```sh
     python -m pip install --upgrade pip
     ```

5. **Instalar las Librerías**:
   - Instala las librerías necesarias:
     ```sh
     pip install flask flask-cors transformers PyPDF2
     ```
   - Instala PyTorch. La instalación varía dependiendo de tu hardware (CPU o GPU). Consulta la [página de instalación de PyTorch](https://pytorch.org/get-started/locally/) para el comando específico. Para una instalación con CPU, usa:
     ```sh
     pip install torch torchvision torchaudio
     ```

6. **Verificar la Instalación**:
   - Puedes listar las librerías instaladas para verificar:
     ```sh
     pip list
     ```

#### Linux

1. **Instalar Python 3.10**:
   - En la mayoría de las distribuciones Linux, puedes instalar Python 3.10 con los siguientes comandos:
     ```sh
     sudo apt-get update
     sudo apt-get install python3.10 python3.10-venv python3.10-dev python3-pip
     ```

2. **Abrir la Terminal**:
   - Abre la terminal presionando `Ctrl + Alt + T`.

3. **Crear y Activar un Entorno Virtual**:
   - Navega a la carpeta donde quieres crear el entorno virtual usando `cd /ruta/a/tu/carpeta`.
   - Crea el entorno virtual ejecutando:
     ```sh
     python3.10 -m venv nombre_del_entorno
     ```
   - Activa el entorno virtual:
     ```sh
     source nombre_del_entorno/bin/activate
     ```

4. **Actualizar pip**:
   - Actualiza pip:
     ```sh
     python -m pip install --upgrade pip
     ```

5. **Instalar las Librerías**:
   - Instala las librerías necesarias:
     ```sh
     pip install flask flask-cors transformers PyPDF2
     ```
   - Instala PyTorch. Consulta la [página de instalación de PyTorch](https://pytorch.org/get-started/locally/) para el comando específico. Para una instalación con CPU, usa:
     ```sh
     pip install torch torchvision torchaudio
     ```

6. **Verificar la Instalación**:
   - Puedes listar las librerías instaladas para verificar:
     ```sh
     pip list
     ```

### Notas Adicionales

- **Desactivar el Entorno Virtual**:
  - Para desactivar el entorno virtual, simplemente ejecuta `deactivate` en ambos sistemas operativos.
  
- **Reactivar el Entorno Virtual**:
  - En Windows:
    ```sh
    nombre_del_entorno\Scripts\activate
    ```
  - En Linux:
    ```sh
    source nombre_del_entorno/bin/activate
    ```

### Construcción y Ejecución del Contenedor

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

