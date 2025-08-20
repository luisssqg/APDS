import numpy as np
import matplotlib.pyplot as plt

def exam_p1():
    """
        Genera una señal modulada (AM) con portadora {fc} Hz y moduladora {fm} Hz,
        calcula su FFT, identifica los picos significativos y muestra su espectro
        con resolución Δf = {delta_f} Hz.
    """
    fs = 100          # frecuencia de muestreo
    fm = 0.5          # frecuencia moduladora
    fc = 8            # frecuencia portadora
    m  = 0.5          # índice de modulación
    N  = 100          # número de muestras

    t  = np.linspace(0, 2, 1000)  

    x_t = (1 + m * np.cos(2*np.pi*fm*t)) * np.sin(2*np.pi*fc*t)

    X = np.fft.fft(x_t)
    X_mag = np.abs(X)/N           
    f = np.fft.fftfreq(N, 1/fs)   

    X_mag = X_mag[:N//2]
    f = f[:N//2]

    thd = 0.1
    pico_indices = np.where(X_mag > thd)[0]
    p_f = f[pico_indices]
    p_a = X_mag[pico_indices]
    delta_f = fs / N
    
    print(f"Resolución en frecuencia Δf = {delta_f} Hz")
    print("Frecuencias de los picos:", p_f)
    print("Amplitudes relativas:", p_a)

    plt.figure(1)
    plt.subplots_adjust(hspace = 0.5)

    plt.stem(p_f, p_a)
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Relative Amplitude")
    plt.title("Signal Spectrum")
    plt.grid()
    plt.show()
