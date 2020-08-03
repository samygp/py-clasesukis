# Programación básica con Python

## Intro
Curso con intención de dar las bases de programación para completos debutantes, y cualquier humano que tenga intenciones de aprender a programar.

## Índice

### Módulo 0

1. [Bienvenida](./mod_0/notebooks/0_bienvenida.ipynb)
2. [Hola mundo: función `print` y tipos de datos](./mod_0/notebooks/1_hola_mundo.ipynb)
    - [Hola mundo: práctica 1](https://repl.it/@elSampai/holamundopractica)
3. [Operadores aritméticos](./mod_0/notebooks/operadores_aritmeticos.ipynb)
    - [Operadores aritméticos:  práctica 1](https://repl.it/@elSampai/operadoresaritmeticospractica)

### Módulo 1

1. [Operadores booleanos y enunciados `if`: Parte 1](./mod_1/control_de_flujo/booleanos_pt1.ipynb)
    - [Booleanos: calentamiento](https://repl.it/@elSampai/booleanoscalentamiento)
    - [Booleanos: Práctica 1](https://repl.it/@elSampai/booleanos1)
2. [Operadores booleanos y enunciados `if`: Parte 2](./mod_1/control_de_flujo/booleanos_pt2.ipynb)
    - [Booleanos: Práctica 2](https://repl.it/@elSampai/booleanos2)
    - [Booleanos: Práctica 3](https://repl.it/@elSampai/booleanos3)
3. [Arreglos: Parte 1](./mod_1/arreglos/notebooks/arreglos_pt1.ipynb)
    - [Arreglos: Práctica 1](https://repl.it/@elSampai/arreglos1)
4. [Arreglos: Parte 2](./mod_1/arreglos/notebooks/arreglos_pt2.ipynb)
    - [Arreglos: Práctica 2](https://repl.it/@elSampai/arreglos2)
5. [Arreglos: Parte 3](./mod_1/arreglos/notebooks/arreglos_pt3.ipynb)
    - [Arreglos: Práctica 3](https://repl.it/@elSampai/arreglos3)
6. [Cadenas](./mod_1/cadenas/notebooks/cadenas_pt1.ipynb)
7. [Ciclos `for`: Parte 1](./mod_1/control_de_flujo/for_pt1.ipynb)
    - [Ciclos `for`: Práctica 1](https://repl.it/@elSampai/for1)
    - [Ciclos `for`: Práctica 2](https://repl.it/@elSampai/for2)
8. [Ciclos `for`: Parte 2](./mod_1/control_de_flujo/for_pt2.ipynb)
    - [Ciclos `for`: Práctica 3](https://repl.it/@elSampai/for3)
    - [Ciclos `for`: Práctica 4](https://repl.it/@elSampai/for4)
9. [Ciclos `while`](./mod_1/control_de_flujo/while.ipynb)
    - [Ciclos `while`: Práctica 1](https://repl.it/@elSampai/while1)
    - [Ciclos `while`: Práctica 2](https://repl.it/@elSampai/while1)
10. [Anidación](./mod_1/control_de_flujo/anidacion.ipynb)
    - [Anidación: Práctica 1](https://repl.it/@elSampai/anidacion1)
    - [Anidación: Práctica 2](https://repl.it/@elSampai/anidacion2)

### Módulo 2

1. [Funciones y subrutinas: Parte 1](./mod_2/funciones/funciones_pt1.ipynb)
1. [Funciones y subrutinas: Parte 2 - scope](./mod_2/funciones/funciones_pt2.ipynb)
    - [Funciones: Práctica 1](https://repl.it/@elSampai/funciones1)
    - [Funciones: Práctica 2](https://repl.it/@elSampai/funciones2)
1. [Recursión](./mod_2/funciones/recursion.ipynb)
    - [Recursión: Práctica 1](https://repl.it/@elSampai/recursion1)
1. [Programación orientada a objetos (POO): Clases, métodos y atributos](./mod_2/poo/poo_pt1.ipynb)
    - [Programación orientada a objetos: Práctica 1](https://repl.it/@elSampai/poo1)
1. [Estructuras de datos: Listas ligadas](./mod_2/estructuras/listas_ligadas.ipynb)
    - [Listas ligadas: Práctica 1](https://repl.it/@elSampai/listasligadas)
1. [Estructuras de datos: Colas](./mod_2/estructuras/colas.ipynb)
    - [Colas: Práctica 1](https://repl.it/@elSampai/colas)
1. [Estructuras de datos: Pilas](./mod_2/estructuras/pilas.ipynb)
    - [Pilas: Práctica 1](https://repl.it/@elSampai/pilas)
1. [Estructuras de datos: Diccionarios](./mod_2/estructuras/diccionarios.ipynb)
    - [Diccionarios: Práctica 1](https://repl.it/@elSampai/diccionarios)
1. [Programación orientada a objetos (POO): Herencia](./mod_2/poo/poo_pt2.ipynb)

## Usar localmente el contenido del repositorio

### Herramientas y prerrequisitos
Para ejecutar localmente este contenido, se debe instalar en la computadora lo siguiente:

1. Python 3 (recomendado a la fecha de hoy, 3.7)
2. pip

#### Para instalar los paquetes y requerimientos
Ejecutar lo siguiente después de haber descargado el repositorio y navegar en la terminal hasta la carpeta raíz del repositorio.
```
python3 -m venv pyenv
source pyenv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate
```
Esto es para que los paquetes y dependencias instalados como parte de este repositorio estén contenidos solamente en este directorio, y no se instalen globalmente para toda la computadora, y evitar, por ejemplo, conflictos entre versiones distintas de un mismo paquete, o si algún otro proyecto usa otra versión de Python.

#### Para activar y desactivar el ambiente virtual (con Jupyter notebooks)
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