import numpy as np
import matplotlib.pyplot as plt
from src.utils.functions import mi_DFT

def exam_p2():
    """
        Este código es para
    """
    fs = 256
    T = 6
    N = 1536
    n = np.arange(N)
    
    f1, f2 = 8, 20

    X_n = np.sin(2*np.pi*f1*n/fs) + 0.5*np.sin(2*np.pi*f2*n/fs)
    Xm1 = mi_DFT(X_n)

    tol = 1e-14
    Xm1.real[abs(Xm1.real) < tol] = 0
    Xm1.imag[abs(Xm1.imag) < tol] = 0

    m = np.arange(N)
    fan = m * fs / N

    plt.figure(1)
    plt.subplots_adjust(hspace = 0.5)

    plt.subplot(2,1,1)
    plt.plot(n/fs, X_n)
    plt.title("Señal discreta limpia en el tiempo")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")  
    plt.grid()

    plt.subplot(2,1,2)
    plt.stem(fan[:N//2], np.abs(Xm1[:N//2]))
    plt.title("Espectro (DFT) de la señal limpia")
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("|X(f)|")
    plt.grid()

    signal_noise = 2*np.cos(np.pi*8*n/fs)
    Signal_final = X_n + signal_noise
    Xm2 = mi_DFT(Signal_final)

    Xm2.real[abs(Xm2.real) < tol] = 0
    Xm2.imag[abs(Xm2.imag) < tol] = 0

    plt.figure(2)
    plt.subplots_adjust(hspace = 0.5)

    plt.subplot(2,1,1)
    plt.plot(n/fs, Signal_final)
    plt.title("Señal discreta con signal_noise en el tiempo")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid()

    plt.subplot(2,1,2)
    plt.stem(fan[:N//2], np.abs(Xm2[:N//2]))
    plt.title("Espectro (DFT) de la señal con signal_noise")
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("|X(f)|")
    plt.grid()

    plt.show()