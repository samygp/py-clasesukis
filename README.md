# Programación básica con Python

## Intro
Curso con intención de dar las bases de programación para completos debutantes, y cualquier humano que tenga intenciones de aprender a programar.

## Herramientas y prerrequisitos
Para ejecutar localmente este contenido, se debe instalar en la computadora lo siguiente:

1. Python 3 (recomendado a la fecha de hoy, 3.7)
2. pip

### Para instalar los paquetes y requerimientos
Ejecutar lo siguiente después de haber descargado el repositorio y navegar en la terminal hasta la carpeta raíz del repositorio.
```
python3 -m venv pyenv
source pyenv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate
```
Esto es para que los paquetes y dependencias instalados como parte de este repositorio estén contenidos solamente en este directorio, y no se instalen globalmente para toda la computadora, y evitar, por ejemplo, conflictos entre versiones distintas de un mismo paquete, o si algún otro proyecto usa otra versión de Python.

### Para activar y desactivar el ambiente virtual (con Jupyter notebooks)
Antes de comenzar a trabajar (una vez instalados lo anterior) hay que activar el ambiente virtual creado, y también inicializar Jupyter.
```
source pyenv/bin/activate
jupyter notebook
```

Para terminar (detener) Jupyter, y desactivar el ambiente virtual, se puede cerrar la terminal en la que se ejecutó.
Opcionalmente, si no se quiere cerrar la terminal, hay que presionar la combinación de teclas `<Ctrl+C>` en la terminal para cerrar Jupyter notebooks, y para desactivar el ambiente virtual, después de terminar Jupyter, ejecutar el comando:
```
deactivate
```