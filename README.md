
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


Tarea 3: Comparación de Señales Senoidales

**Descripción:**  
Genera una señal senoidal de referencia (A=1, f=1Hz, ϕ=0) y una señal modificada según los parámetros de amplitud, frecuencia y fase. Muestra gráficas de:

- Comparación de señales continuas
- Señal discreta de referencia
- Señal discreta modificada

Uso / Ejecución:**
```bash
python main.py Tarea_3 <A> <f> <phi>


Tarea 4: Análisis de Resolución de un DAC

**Descripción:**  
Calcula los niveles de salida de un DAC según el número de bits, determina el tamaño de paso y la resolución porcentual, y grafica la señal resultante.

**Uso / Ejecución:**
```bash
python main.py Tarea_4 <bits>

 
 
 
 Exam_01: Señal Modulada AM y FFT

**Objetivos:**  
- Generar una señal modulada AM con portadora (`fc`) y moduladora (`fm`).  
- Calcular la FFT de la señal y obtener la magnitud normalizada.  
- Identificar los picos significativos en el espectro.  
- Mostrar gráficamente el espectro de la señal y la resolución en frecuencia (Δf).  

**Uso / Ejecución:**
```bash
python main.py Exam_01

 Exam_02: Señal Discreta y Análisis con DFT

**Objetivos:**  
- Generar una señal discreta suma de dos senoidales con frecuencias conocidas (`f1`, `f2`).  
- Calcular la DFT de la señal y mostrar el espectro limpio.  
- Agregar una señal de ruido de frecuencia específica y analizar el efecto en el espectro.  
- Identificar picos significativos en presencia de ruido y estimar la resolución en frecuencia (Δf = fs / N).  

**Uso / Ejecución:**
```bash
python main.py Exam_02
