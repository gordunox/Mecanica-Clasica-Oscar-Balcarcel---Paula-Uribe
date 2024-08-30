# -*- coding: utf-8 -*-
"""Pendulo acomplados.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iqyJispMjEyAyLsEFppySqwK1_soajAh

**Solucion sistema base (Cualquier angulo)**
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def sistema(y, t):

    a = 1
    l = 1.0
    k = 1
    m = 1
    g = 9.81
    theta1, theta2, w1, w2 = y


    dtheta1dt = w1
    dtheta2dt = w2
    dw1dt = (-(k*l*l*np.sin(theta1-theta2))+(k*a*l*np.cos(theta1))+((k*a*((l*l*np.sin(theta1-theta2))-(a*l*np.cos(theta1))))/(np.sqrt((a*a)+(2*l*l)-(2*l*l*np.cos(theta1-theta2)+(2*a*l*(np.sin(theta2)-np.sin(theta1)))))))-(m*g*l*np.sin(theta1)))/(m*l*l)  # Ejemplo: ecuación para r1 (cambiar con f_1)
    dw2dt = ((k*l*l*np.sin(theta1-theta2))-(k*a*l*np.cos(theta2))+((k*a*((-l*l*np.sin(theta1-theta2))+(a*l*np.cos(theta2))))/(np.sqrt((a*a)+(2*l*l)-(2*l*l*np.cos(theta1-theta2)+(2*a*l*(np.sin(theta2)-np.sin(theta1)))))))-(m*g*l*np.sin(theta2)))/(m*l*l)  # Ejemplo: ecuación para theta1 (cambiar con f_2)

    return [dtheta1dt, dtheta2dt, dw1dt, dw2dt]


theta1_0 = 0.00174533
theta2_0 = 0
w1_0 = 0
w2_0 = 0

y0 = [theta1_0, theta2_0, w1_0, w2_0]


t = np.linspace(0,50, 10000)


sol = odeint(sistema, y0, t)


theta1_sol = sol[:, 0]
theta2_sol = sol[:, 1]


# Crear subplots
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# Graficar theta1(t)
axs[0].plot(t, theta1_sol, label='theta1(t)', color='b')
axs[0].set_xlabel('Tiempo')
axs[0].set_ylabel('theta1')
axs[0].legend()

# Graficar theta2(t)
axs[1].plot(t, theta2_sol, label='theta2(t)', color='r')
axs[1].set_xlabel('Tiempo')
axs[1].set_ylabel('theta2')
axs[1].legend()

# Mostrar gráfico
plt.tight_layout()
plt.show()

"""**Solucion sistema resorte por mitad (Cualquier angulo)**

---


"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def sistema(y, t):

    a = 1
    l = 1.0
    k = 1
    m = 1
    g = 9.81
    theta1, theta2, w1, w2 = y


    dtheta1dt = w1
    dtheta2dt = w2
    dw1dt = (-(1/4)*k*l*l*np.sin(theta1-theta2))+((1/2)*k*a*l*np.cos(theta1))+((k*a*(((1/2)*l*l*np.sin(theta1-theta2))-(a*l*np.cos(theta1))))/(2*np.sqrt((a*a)+((1/2)*l*l)-((1/2)*l*l*np.cos(theta1-theta2)+(a*l*(np.sin(theta2)-np.sin(theta1)))))))-(m*g*l*np.sin(theta1))/(m*l*l)  # Ejemplo: ecuación para r1 (cambiar con f_1)
    dw2dt = ((1/4)*k*l*l*np.sin(theta1-theta2))-((1/2)*k*a*l*np.cos(theta2))+((k*a*((-(1/2)*l*l*np.sin(theta1-theta2))+(a*l*np.cos(theta2))))/(2*np.sqrt((a*a)+((1/2)*l*l)-((1/2)*l*l*np.cos(theta1-theta2)+(a*l*(np.sin(theta2)-np.sin(theta1)))))))-(m*g*l*np.sin(theta2))/(m*l*l)  # Ejemplo: ecuación para theta1 (cambiar con f_2)

    return [dtheta1dt, dtheta2dt, dw1dt, dw2dt]


theta1_0 = (np.pi/4)
theta2_0 = np.pi/6
w1_0 = 0
w2_0 = 0

y0 = [theta1_0, theta2_0, w1_0, w2_0]


t = np.linspace(0,50, 10000)


sol = odeint(sistema, y0, t)


theta1_sol = sol[:, 0]
theta2_sol = sol[:, 1]
# Crear subplots
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# Graficar theta1(t)
axs[0].plot(t, theta1_sol, label='theta1(t)', color='b')
axs[0].set_xlabel('Tiempo')
axs[0].set_ylabel('theta1')
axs[0].legend()

# Graficar theta2(t)
axs[1].plot(t, theta2_sol, label='theta2(t)', color='r')
axs[1].set_xlabel('Tiempo')
axs[1].set_ylabel('theta2')
axs[1].legend()

# Mostrar gráfico
plt.tight_layout()
plt.show()

"""**Solucion sistema masas distintas (cualquier angulo)**"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def sistema(y, t):

    a = 1
    l = 1.0
    k = 1
    m1 =1
    m2=1
    g = 9.81
    theta1, theta2, w1, w2 = y


    dtheta1dt = w1
    dtheta2dt = w2
    dw1dt = (-(k*l*l*np.sin(theta1-theta2))+(k*a*l*np.cos(theta1))+((k*a*((l*l*np.sin(theta1-theta2))-(a*l*np.cos(theta1))))/(np.sqrt((a*a)+(2*l*l)-(2*l*l*np.cos(theta1-theta2)+(2*a*l*(np.sin(theta2)-np.sin(theta1)))))))-(m1*g*l*np.sin(theta1)))/(m1*l*l)  # Ejemplo: ecuación para r1 (cambiar con f_1)
    dw2dt = ((k*l*l*np.sin(theta1-theta2))-(k*a*l*np.cos(theta2))+((k*a*((-l*l*np.sin(theta1-theta2))+(a*l*np.cos(theta2))))/(np.sqrt((a*a)+(2*l*l)-(2*l*l*np.cos(theta1-theta2)+(2*a*l*(np.sin(theta2)-np.sin(theta1)))))))-(m2*g*l*np.sin(theta2)))/(m2*l*l)  # Ejemplo: ecuación para theta1 (cambiar con f_2)

    return [dtheta1dt, dtheta2dt, dw1dt, dw2dt]


theta1_0 = (np.pi/4)
theta2_0 = np.pi/6
w1_0 = 0
w2_0 = 0

y0 = [theta1_0, theta2_0, w1_0, w2_0]


t = np.linspace(0,50, 10000)


sol = odeint(sistema, y0, t)


theta1_sol = sol[:, 0]
theta2_sol = sol[:, 1]


# Crear subplots
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# Graficar theta1(t)
axs[0].plot(t, theta1_sol, label='theta1(t)', color='b')
axs[0].set_xlabel('Tiempo')
axs[0].set_ylabel('theta1')
axs[0].legend()

# Graficar theta2(t)
axs[1].plot(t, theta2_sol, label='theta2(t)', color='r')
axs[1].set_xlabel('Tiempo')
axs[1].set_ylabel('theta2')
axs[1].legend()

# Mostrar gráfico
plt.tight_layout()
plt.show()

"""**Solucion sistemas largos distintos (Caulquier angulo)**"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def sistema(y, t):

    a = 1
    l1 = 15
    l2= 20
    k = 1
    m = 1
    g = 9.81
    theta1, theta2, w1, w2 = y

    term1=-k*l1*l2*np.sin(theta1-theta2)+a*k*l1*np.cos(theta1)-m*l1*g*np.sin(theta1)
    term2=(l1*l2*np.sin(theta1-theta2)-a*l1*np.cos(theta1))/(np.sqrt((a*a)+(l1*l1)+(l2*l2)-2*l1*l2*np.cos(theta1-theta2)+2*a*l2*(np.sin(theta2))-2*a*l1*np.sin(theta1)))
    c=(k*np.sqrt((a*a)+((l1-l2)*(l1-l2))))

    term3=k*l1*l2*np.sin(theta1-theta2)-a*k*l2*np.cos(theta2)-m*l2*g*np.sin(theta2)
    term4=(-l1*l2*np.sin(theta1-theta2)+a*l2*np.cos(theta2))/(np.sqrt((a*a)+(l1*l1)+(l2*l2)-2*l1*l2*np.cos(theta1-theta2)+2*a*l2*(np.sin(theta2))-2*a*l1*np.sin(theta1)))

    dtheta1dt = w1
    dtheta2dt = w2
    dw1dt = (term1+c*term2)/(m*l1*l1)
    dw2dt = (term3+c*term4)/(m*l2*l2)

    return [dtheta1dt, dtheta2dt, dw1dt, dw2dt]


theta1_0 = (np.pi/4)
theta2_0 = np.pi/6
w1_0 = 0
w2_0 = 0

y0 = [theta1_0, theta2_0, w1_0, w2_0]


t = np.linspace(0,50, 10000)


sol = odeint(sistema, y0, t)


theta1_sol = sol[:, 0]
theta2_sol = sol[:, 1]


# Crear subplots
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# Graficar theta1(t)
axs[0].plot(t, theta1_sol, label='theta1(t)', color='b')
axs[0].set_xlabel('Tiempo')
axs[0].set_ylabel('theta1')
axs[0].legend()

# Graficar theta2(t)
axs[1].plot(t, theta2_sol, label='theta2(t)', color='r')
axs[1].set_xlabel('Tiempo')
axs[1].set_ylabel('theta2')
axs[1].legend()

# Mostrar gráfico
plt.tight_layout()
plt.show()

"""**Analisis de caos (cualquier angulo)**"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def sistema(y, t):
    a = 1
    l = 1.0
    k = 1
    m = 1
    g = 9.81
    theta1, theta2, w1, w2 = y

    dtheta1dt = w1
    dtheta2dt = w2
    dw1dt = (-(k*l*l*np.sin(theta1-theta2))+(k*a*l*np.cos(theta1)) +
             (k*a*((l*l*np.sin(theta1-theta2)) - (a*l*np.cos(theta1)))) /
             (np.sqrt((a*a) + (2*l*l) - (2*l*l*np.cos(theta1-theta2)) +
             (2*a*l*(np.sin(theta2) - np.sin(theta1))))) -
             (m*g*l*np.sin(theta1))) / (m*l*l)
    dw2dt = ((k*l*l*np.sin(theta1-theta2)) - (k*a*l*np.cos(theta2)) +
             (k*a*((-l*l*np.sin(theta1-theta2)) + (a*l*np.cos(theta2)))) /
             (np.sqrt((a*a) + (2*l*l) - (2*l*l*np.cos(theta1-theta2)) +
             (2*a*l*(np.sin(theta2) - np.sin(theta1))))) -
             (m*g*l*np.sin(theta2))) / (m*l*l)

    return [dtheta1dt, dtheta2dt, dw1dt, dw2dt]

# Primer conjunto de condiciones iniciales
theta1_0_1 = np.pi / 4 +0.01
theta2_0_1 = np.pi / 6
w1_0_1 = 0
w2_0_1 = 0
y0_1 = [theta1_0_1, theta2_0_1, w1_0_1, w2_0_1]

# Segundo conjunto de condiciones iniciales
theta1_0_2 = (np.pi /4)
theta2_0_2 = np.pi / 6
w1_0_2 = 0
w2_0_2 = 0
y0_2 = [theta1_0_2, theta2_0_2, w1_0_2, w2_0_2]

t = np.linspace(0, 200, 10000)

# Resolver el sistema para ambos conjuntos de condiciones iniciales
sol_1 = odeint(sistema, y0_1, t)
sol_2 = odeint(sistema, y0_2, t)

# Obtener las soluciones
theta1_sol_1 = sol_1[:, 0]
theta2_sol_1 = sol_1[:, 1]
theta1_sol_2 = sol_2[:, 0]
theta2_sol_2 = sol_2[:, 1]

# Calcular la resta de las soluciones
theta1_diff = theta1_sol_1 - theta1_sol_2
theta2_diff = theta2_sol_1 - theta2_sol_2

# Crear subplots
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# Graficar la resta de theta1(t)
axs[0].plot(t, theta1_diff, label='Resta de theta1(t)', color='b')
axs[0].set_xlabel('Tiempo')
axs[0].set_ylabel('Resta de theta1')
axs[0].legend()

# Graficar la resta de theta2(t)
axs[1].plot(t, theta2_diff, label='Resta de theta2(t)', color='r')
axs[1].set_xlabel('Tiempo')
axs[1].set_ylabel('Resta de theta2')
axs[1].legend()

# Mostrar gráfico
plt.tight_layout()
plt.show()

"""**Espectograma (cualquier angulo)**"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

# Definir el sistema de ecuaciones
def sistema(y, t):
    a = 1
    l = 1.0
    k = 1
    m = 1
    g = 9.81
    theta1, theta2, w1, w2 = y

    dtheta1dt = w1
    dtheta2dt = w2
    dw1dt = (-(k*l*l*np.sin(theta1-theta2))+(k*a*l*np.cos(theta1))+
            ((k*a*((l*l*np.sin(theta1-theta2))-(a*l*np.cos(theta1))))/
            (np.sqrt((a*a)+(2*l*l)-(2*l*l*np.cos(theta1-theta2)+(2*a*l*(np.sin(theta2)-np.sin(theta1)))))))-
            (m*g*l*np.sin(theta1)))/(m*l*l)
    dw2dt = ((k*l*l*np.sin(theta1-theta2))-(k*a*l*np.cos(theta2))+
            ((k*a*((-l*l*np.sin(theta1-theta2))+(a*l*np.cos(theta2))))/
            (np.sqrt((a*a)+(2*l*l)-(2*l*l*np.cos(theta1-theta2)+(2*a*l*(np.sin(theta2)-np.sin(theta1)))))))-
            (m*g*l*np.sin(theta2)))/(m*l*l)

    return [dtheta1dt, dtheta2dt, dw1dt, dw2dt]

# Condiciones iniciales
theta1_0 = np.pi/4
theta2_0 = np.pi/6
w1_0 = 0
w2_0 = 0
y0 = [theta1_0, theta2_0, w1_0, w2_0]

# Tiempo
t = np.linspace(0, 100, 10000)

# Resolver el sistema
sol = odeint(sistema, y0, t)
theta1_sol = sol[:, 0]

# Generar el espectrograma
frequencies, times, Sxx = spectrogram(theta1_sol, fs=1/(t[1]-t[0]), nperseg=256)

# Graficar el espectrograma
plt.pcolormesh(times, frequencies, np.log(Sxx), shading='gouraud')
plt.ylabel('Frecuencia [Hz]')
plt.xlabel('Tiempo [s]')
plt.title('Espectrograma de theta1(t)')
plt.colorbar(label='Intensidad [dB]')
plt.show()

"""**Transformada de fourier (cualquier angulo)**"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definir el sistema de ecuaciones (mismo que antes)
def sistema(y, t):
    a = 1
    l = 1.0
    k = 1
    m = 1
    g = 9.81
    theta1, theta2, w1, w2 = y

    dtheta1dt = w1
    dtheta2dt = w2
    dw1dt = (-(k*l*l*np.sin(theta1-theta2))+(k*a*l*np.cos(theta1))+
            ((k*a*((l*l*np.sin(theta1-theta2))-(a*l*np.cos(theta1))))/
            (np.sqrt((a*a)+(2*l*l)-(2*l*l*np.cos(theta1-theta2)+(2*a*l*(np.sin(theta2)-np.sin(theta1)))))))-
            (m*g*l*np.sin(theta1)))/(m*l*l)
    dw2dt = ((k*l*l*np.sin(theta1-theta2))-(k*a*l*np.cos(theta2))+
            ((k*a*((-l*l*np.sin(theta1-theta2))+(a*l*np.cos(theta2))))/
            (np.sqrt((a*a)+(2*l*l)-(2*l*l*np.cos(theta1-theta2)+(2*a*l*(np.sin(theta2)-np.sin(theta1)))))))-
            (m*g*l*np.sin(theta2)))/(m*l*l)

    return [dtheta1dt, dtheta2dt, dw1dt, dw2dt]

# Condiciones iniciales
theta1_0 = np.pi / 4
theta2_0 = np.pi / 6
w1_0 = 0
w2_0 = 0
y0 = [theta1_0, theta2_0, w1_0, w2_0]

# Tiempo
t = np.linspace(0, 100, 10000)

# Resolver el sistema
sol = odeint(sistema, y0, t)
theta1_sol = sol[:, 0]
theta2_sol = sol[:, 1]

# Realizar la Transformada de Fourier
N = len(theta1_sol)
dt = t[1] - t[0]  # Intervalo de tiempo
frequencies = np.fft.fftfreq(N, dt)
theta1_fft = np.fft.fft(theta1_sol)
theta2_fft = np.fft.fft(theta2_sol)

# Filtrar solo las frecuencias hasta 2.5 Hz
freq_limit = 1
mask = np.abs(frequencies) <= freq_limit

# Graficar la magnitud de la Transformada de Fourier para theta1 y theta2
plt.figure(figsize=(12, 6))

# Gráfico para theta1
plt.subplot(2, 1, 1)
plt.plot(frequencies[mask], np.abs(theta1_fft)[mask], label='FFT de theta1', color='b')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud de Fourier')
plt.title('Transformada de Fourier de theta1 (0-2.5 Hz)')
plt.legend()

# Gráfico para theta2
plt.subplot(2, 1, 2)
plt.plot(frequencies[mask], np.abs(theta2_fft)[mask], label='FFT de theta2', color='r')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud de Fourier')
plt.title('Transformada de Fourier de theta2 (0-2.5 Hz)')
plt.legend()

plt.tight_layout()
plt.show()

"""**Sistema base(angulos pequeños)**"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def sistema(y, t):

    a = 1
    l = 1.0
    k = 1
    m = 1
    g = 9.81
    theta1, theta2, w1, w2 = y


    dtheta1dt = w1
    dtheta2dt = w2
    dw1dt = (a*l*k-(k*a*a*l)/(np.sqrt(a*a+2*a*l*(theta2-theta1))))/(m*l*l)
    dw2dt = (-a*l*k+(k*a*a*l)/(np.sqrt(a*a+2*a*l*(theta2-theta1))))/(m*l*l)
    return [dtheta1dt, dtheta2dt, dw1dt, dw2dt]


theta1_0 = 0.17
theta2_0 = 0
w1_0 = 0
w2_0 = 0

y0 = [theta1_0, theta2_0, w1_0, w2_0]


t = np.linspace(0,50, 10000)


sol = odeint(sistema, y0, t)


theta1_sol = sol[:, 0]
theta2_sol = sol[:, 1]


# Crear subplots
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# Graficar theta1(t)
axs[0].plot(t, theta1_sol, label='theta1(t)', color='b')
axs[0].set_xlabel('Tiempo')
axs[0].set_ylabel('theta1')
axs[0].legend()

# Graficar theta2(t)
axs[1].plot(t, theta2_sol, label='theta2(t)', color='r')
axs[1].set_xlabel('Tiempo')
axs[1].set_ylabel('theta2')
axs[1].legend()

# Mostrar gráfico
plt.tight_layout()
plt.show()

"""**Sistema resorte en el medio (angulos pequeños)**"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def sistema(y, t):

    a = 1
    l = 1.0
    k = 1
    m = 1
    g = 9.81
    theta1, theta2, w1, w2 = y


    dtheta1dt = w1
    dtheta2dt = w2
    dw1dt = ((a*l*k)/2-(k*a*a*l)/(2*(np.sqrt(a*a+a*l*(theta2-theta1)))))/(m*l*l)
    dw2dt = (-(a*l*k)/2+(k*a*a*l)/(2*(np.sqrt(a*a+a*l*(theta2-theta1)))))/(m*l*l)
    return [dtheta1dt, dtheta2dt, dw1dt, dw2dt]


theta1_0 = 0.17
theta2_0 = 0
w1_0 = 0
w2_0 = 0

y0 = [theta1_0, theta2_0, w1_0, w2_0]


t = np.linspace(0,50, 10000)


sol = odeint(sistema, y0, t)


theta1_sol = sol[:, 0]
theta2_sol = sol[:, 1]


# Crear subplots
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# Graficar theta1(t)
axs[0].plot(t, theta1_sol, label='theta1(t)', color='b')
axs[0].set_xlabel('Tiempo')
axs[0].set_ylabel('theta1')
axs[0].legend()

# Graficar theta2(t)
axs[1].plot(t, theta2_sol, label='theta2(t)', color='r')
axs[1].set_xlabel('Tiempo')
axs[1].set_ylabel('theta2')
axs[1].legend()

# Mostrar gráfico
plt.tight_layout()
plt.show()

"""****Solucion sistema masas distintas (angulos pequeños)**"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def sistema(y, t):

    a = 1
    l = 1.0
    k = 1
    m1 = 12
    m2=36
    g = 9.81
    theta1, theta2, w1, w2 = y


    dtheta1dt = w1
    dtheta2dt = w2
    dw1dt = (a*l*k-(k*a*a*l)/(np.sqrt(a*a+2*a*l*(theta2-theta1))))/(m1*l*l)
    dw2dt = (-a*l*k+(k*a*a*l)/(np.sqrt(a*a+2*a*l*(theta2-theta1))))/(m2*l*l)
    return [dtheta1dt, dtheta2dt, dw1dt, dw2dt]


theta1_0 = 0.17
theta2_0 = 0
w1_0 = 0
w2_0 = 0

y0 = [theta1_0, theta2_0, w1_0, w2_0]


t = np.linspace(0,50, 10000)


sol = odeint(sistema, y0, t)


theta1_sol = sol[:, 0]
theta2_sol = sol[:, 1]


# Crear subplots
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# Graficar theta1(t)
axs[0].plot(t, theta1_sol, label='theta1(t)', color='b')
axs[0].set_xlabel('Tiempo')
axs[0].set_ylabel('theta1')
axs[0].legend()

# Graficar theta2(t)
axs[1].plot(t, theta2_sol, label='theta2(t)', color='r')
axs[1].set_xlabel('Tiempo')
axs[1].set_ylabel('theta2')
axs[1].legend()

# Mostrar gráfico
plt.tight_layout()
plt.show()

"""**Solucion largos distintos (angulos pequeños)**"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def sistema(y, t):

    a = 1
    l1= 1.0
    l2=1
    k = 1
    m=1
    g = 9.81
    theta1, theta2, w1, w2 = y


    dtheta1dt = w1
    dtheta2dt = w2

    numerator1 = (a * l1 * k - ((np.sqrt(a**2 + (l1 - l2)**2) * k * a * l1))/(np.sqrt((l1 - l2)**2 + 2 * a * l2 * theta2 - 2 * a * l1 * theta2 + a**2)))
    numerator2 = (-a * l2 * k + ((np.sqrt(a**2 + (l1 - l2)**2) * k * a * l2))/(np.sqrt((l1 - l2)**2 + 2 * a * l2 * theta2 - 2 * a * l1 * theta2 + a**2)))

    dw2dt = numerator1 / (m * l2**2)
    dw1dt = numerator2 / (m * l1**2)

    return [dtheta1dt, dtheta2dt, dw1dt, dw2dt]


theta1_0 = 0.17
theta2_0 = 0
w1_0 = 0
w2_0 = 0

y0 = [theta1_0, theta2_0, w1_0, w2_0]


t = np.linspace(0,50, 10000)


sol = odeint(sistema, y0, t)


theta1_sol = sol[:, 0]
theta2_sol = sol[:, 1]


# Crear subplots
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# Graficar theta1(t)
axs[0].plot(t, theta1_sol, label='theta1(t)', color='b')
axs[0].set_xlabel('Tiempo')
axs[0].set_ylabel('theta1')
axs[0].legend()

# Graficar theta2(t)
axs[1].plot(t, theta2_sol, label='theta2(t)', color='r')
axs[1].set_xlabel('Tiempo')
axs[1].set_ylabel('theta2')
axs[1].legend()

# Mostrar gráfico
plt.tight_layout()
plt.show()

"""**Caos aproximacion**"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def sistema(y, t):

    a = 1
    l = 1.0
    k = 1
    m = 1
    g = 9.81
    theta1, theta2, w1, w2 = y


    dtheta1dt = w1
    dtheta2dt = w2
    dw1dt = (a*l*k-(k*a*a*l)/(np.sqrt(a*a+2*a*l*(theta2-theta1))))/(m*l*l)
    dw2dt = (-a*l*k+(k*a*a*l)/(np.sqrt(a*a+2*a*l*(theta2-theta1))))/(m*l*l)
    return [dtheta1dt, dtheta2dt, dw1dt, dw2dt]


# Primer conjunto de condiciones iniciales
theta1_0_1 = 0.17 +0.01
theta2_0_1 = 0
w1_0_1 = 0
w2_0_1 = 0
y0_1 = [theta1_0_1, theta2_0_1, w1_0_1, w2_0_1]

# Segundo conjunto de condiciones iniciales
theta1_0_2 = 0.17
theta2_0_2 = 0
w1_0_2 = 0
w2_0_2 = 0
y0_2 = [theta1_0_2, theta2_0_2, w1_0_2, w2_0_2]

t = np.linspace(0, 200, 10000)

# Resolver el sistema para ambos conjuntos de condiciones iniciales
sol_1 = odeint(sistema, y0_1, t)
sol_2 = odeint(sistema, y0_2, t)

# Obtener las soluciones
theta1_sol_1 = sol_1[:, 0]
theta2_sol_1 = sol_1[:, 1]
theta1_sol_2 = sol_2[:, 0]
theta2_sol_2 = sol_2[:, 1]

# Calcular la resta de las soluciones
theta1_diff = theta1_sol_1 - theta1_sol_2
theta2_diff = theta2_sol_1 - theta2_sol_2

# Crear subplots
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# Graficar la resta de theta1(t)
axs[0].plot(t, theta1_diff, label='Resta de theta1(t)', color='b')
axs[0].set_xlabel('Tiempo')
axs[0].set_ylabel('Resta de theta1')
axs[0].legend()

# Graficar la resta de theta2(t)
axs[1].plot(t, theta2_diff, label='Resta de theta2(t)', color='r')
axs[1].set_xlabel('Tiempo')
axs[1].set_ylabel('Resta de theta2')
axs[1].legend()

# Mostrar gráfico
plt.tight_layout()
plt.show()

"""**Fourier(angulos pequeños)**"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def sistema(y, t):

    a = 1
    l = 1.0
    k = 1
    m = 1
    g = 9.81
    theta1, theta2, w1, w2 = y


    dtheta1dt = w1
    dtheta2dt = w2
    dw1dt = (a*l*k-(k*a*a*l)/(np.sqrt(a*a+2*a*l*(theta2-theta1))))/(m*l*l)
    dw2dt = (-a*l*k+(k*a*a*l)/(np.sqrt(a*a+2*a*l*(theta2-theta1))))/(m*l*l)
    return [dtheta1dt, dtheta2dt, dw1dt, dw2dt]


theta1_0 = 0.17
theta2_0 = 0
w1_0 = 0
w2_0 = 0

y0 = [theta1_0, theta2_0, w1_0, w2_0]


t = np.linspace(0,200, 10000)


sol = odeint(sistema, y0, t)


theta1_sol = sol[:, 0]
theta2_sol = sol[:, 1]


# Realizar la Transformada de Fourier
N = len(theta1_sol)
dt = t[1] - t[0]  # Intervalo de tiempo
frequencies = np.fft.fftfreq(N, dt)
theta1_fft = np.fft.fft(theta1_sol)
theta2_fft = np.fft.fft(theta2_sol)

# Filtrar solo las frecuencias hasta 2.5 Hz
freq_limit = 1
mask = np.abs(frequencies) <= freq_limit

# Graficar la magnitud de la Transformada de Fourier para theta1 y theta2
plt.figure(figsize=(12, 6))

# Gráfico para theta1
plt.subplot(2, 1, 1)
plt.plot(frequencies[mask], np.abs(theta1_fft)[mask], label='FFT de theta1', color='b')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud de Fourier')
plt.title('Transformada de Fourier de theta1 (0-2.5 Hz)')
plt.legend()

# Gráfico para theta2
plt.subplot(2, 1, 2)
plt.plot(frequencies[mask], np.abs(theta2_fft)[mask], label='FFT de theta2', color='r')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud de Fourier')
plt.title('Transformada de Fourier de theta2 (0-2.5 Hz)')
plt.legend()

plt.tight_layout()
plt.show()