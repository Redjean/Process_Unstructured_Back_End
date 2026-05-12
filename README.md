# Process_Unstructured_Back_End
Back End para realizar el flujo de procesamiento de datos no estructurados. 

## Configuración del entorno virtual

Antes de ejecutar el proyecto, es recomendable crear un entorno virtual de Python para aislar las dependencias y evitar conflictos con otras instalaciones del sistema.

### 1. Verificar la instalación de Python

Compruebe que Python esté instalado correctamente:

```bash
python --version
```

O, en algunos sistemas:

```bash
python3 --version
```

Se recomienda utilizar Python 3.10 o superior.

---

### 2. Crear el entorno virtual

Ubíquese en la carpeta raíz del proyecto y ejecute:

```bash
python -m venv env
```

Este comando creará un directorio llamado `env`, el cual contendrá una instalación aislada de Python y sus paquetes.

---

### 3. Activar el entorno virtual

#### Windows (PowerShell)

```powershell
env\Scripts\Activate.ps1
```

#### Windows (Símbolo del sistema)

```cmd
venv\Scripts\activate.bat
```

#### Linux y macOS

```bash
source venv/bin/activate
```

Una vez activado, el nombre del entorno (`env`) aparecerá al inicio de la línea de comandos.

---

### 4. Instalar las dependencias del proyecto

Con el entorno virtual activado, instale las bibliotecas requeridas:

```bash
pip install -r requirements.txt
```

---

### 5. Verificar la instalación

Para confirmar que las dependencias se instalaron correctamente, ejecute:

```bash
pip list
```

Deberían aparecer, entre otras, las librerías `fastapi`, `uvicorn` y `pydantic`.

---

### 6. Ejecutar la aplicación

Inicie el servidor de desarrollo con:

```bash
uvicorn app.main:app --reload
```

---

### 7. Desactivar el entorno virtual

Cuando termine de trabajar en el proyecto, puede salir del entorno virtual con:

```bash
deactivate
```

---

## Resumen rápido

```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual (Windows PowerShell)
venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
uvicorn app.main:app --reload

# Desactivar el entorno virtual
deactivate
```