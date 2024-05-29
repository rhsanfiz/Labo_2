import pandas as pd
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt




def devuelve_fourier(url):

  datos = pd.read_csv(url,header=None)

  #t: tiempo; volt: voltaje.  Dejo el tiempo comentado xq no es necesario, solo hace falta el dt de muestreo
  #t = datos[3].to_numpy()
  volt = datos[4].to_numpy()

  #N: cantidad de puntos    dt: diferencia temporal entre puntos
  N = len(volt)
  dt = float(datos[1][1])

  yf = sc.fft.fft(volt)
  xf = sc.fft.fftfreq(N,d=dt)[:N//2]   #pongo del 35 al 48 xq es donde se ve bien la campana. cambiar por [:N//2] para todo el espectro

  return(2.0/N * np.abs(yf[:N//2]) , xf)

 num_arch = ['00','01','02','03','04','05','06','07','08','09','10','11']

# yPromedio = np.zeros(13)

# for i in range(len(num)):#12
#   y,x=devuelve_fourier('Labo_2/Datos onda cuadrada v2/ALL00'+num[i]+'/F00'+num[i]+'CH1.CSV')
#   yPromedio += y

def fouPosta(num,rango):
    y,x=devuelve_fourier('./Datos onda cuadrada v2/ALL00'+num+'/F00'+num+'CH1.CSV')

    plt.xlabel('Frecuencia (kHz)')
    plt.ylabel('???')

    plt.scatter(x[rango[0]:rango[1]], y[rango[0]:rango[1]])
    plt.show()

def fouxd(num,rango):
    y,x=devuelve_fourier('./Datos onda cuadrada v2/ALL00'+num+'/F00'+num+'CH1.CSV')

    plt.xlabel('Frecuencia (kHz)')
    plt.ylabel('???')

    plt.plot(y[rango[0]:rango[1]])
    plt.show()



