# Proyecto de Señales - Tareas 1 y 2

Este proyecto permite graficar y analizar diferentes tipos de señales continuas y discretas, incluyendo señales sinusoidales, exponenciales, triangulares y cuadradas. Está organizado en dos tareas principales que pueden ser ejecutadas desde el archivo `main.py`.

## Estructura del Proyecto
    ├── main.py
    ├── README.md
    ├── requirements.txt
    └── src/
    ├── Tarea_1.py
    ├── Tarea_2.py
    └── utils/
    └── grapher.py

Tarea 1: Graficar señales continuas y discretas
python main.py Tarea_1 [tipo_de_senal]

Donde [tipo_de_senal] puede ser uno de:
    seno
    exponencial
    triangular
    cuadrada
Ejemplo:
    python main.py Tarea_1 seno

Tarea 2: Graficar señal sinusoidal continua con frecuencia personalizada
Ejemplo:
    python main.py Tarea_2 2.5

Notas
Asegúrate de ejecutar el script desde la raíz del proyecto para que las rutas de importación funcionen correctamente.

El proyecto usa funciones de matplotlib para mostrar las gráficas, por lo que debe tener una interfaz gráfica disponible.

Si usas un entorno virtual, activa el entorno antes de instalar los paquetes y ejecutar el script.