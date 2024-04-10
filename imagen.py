import pandas as pd
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

def grafica_linealidad():
    url = 'https://docs.google.com/spreadsheets/d/1iS_XVTNLZ-BSYV3EmOBN1Vo6mmGxjd1-PvZHGyYdg_c/export?format=csv'     #cambiar por el link posta lo q esta entre d/ y /export
    datos_respuesta_voltaje= pd.read_csv(url)

    #Ve: voltaje emitido  Vr: voltaje recibido
    voltaje_emitido = datos_respuesta_voltaje['Voltaje emitido (Vpp)'].to_numpy()
    error_Ve = datos_respuesta_voltaje['Error del voltaje emitido'].to_numpy()
    voltaje_recibido = datos_respuesta_voltaje['Voltaje recibido (Vpp)'].to_numpy()
    error_Vr = datos_respuesta_voltaje['Error del voltaje recibido'].to_numpy()


    m,b,r,*otros = sc.stats.linregress(voltaje_emitido,voltaje_recibido)  #regresión lineal m: pendiente b:ordenadaal origen, r: coef. r de pearson
    print(r**2)
    voltaje_esperado = [] #el voltaje que dice el ajuste para los mismos puntos de voltaje medido

    for x in(voltaje_emitido):
    voltaje_esperado.append(m*x+b)

    plt.xlabel('Voltaje aplicado al emisor (V)')
    plt.ylabel('Voltaje medido en el receptor (V)')

    plt.plot(voltaje_emitido, voltaje_esperado)
    plt.errorbar(voltaje_emitido, voltaje_recibido, xerr=error_Ve, yerr=error_Vr, fmt='none', ecolor='r')
    plt.show()

def grafico_curva_de_respuesta():
    url = 'https://docs.google.com/spreadsheets/d/12bLRg_DhFVkXwLZXoDPi7wt14ozUOb3cNRsMHDaxZ04/export?format=csv'     #cambiar por el link posta lo q esta entre d/ y /export
    datos_respuesta_voltaje= pd.read_csv(url)

    #Ve: voltaje emitido  Vr: voltaje recibido
    frecuencia = datos_respuesta_voltaje['frec'].to_numpy()
    voltaje_recibido = datos_respuesta_voltaje['volt'].to_numpy()
    error_Vr = datos_respuesta_voltaje['err volt'].to_numpy()

    plt.xlabel('Frecuencia (kHz)')
    plt.ylabel('Voltaje medido (V)')

    #plt.plot(voltaje_emitido, voltaje_esperado)        #acá habría que usar algún modelo. Supongo que el del osc forzado
    plt.errorbar(frecuencia, voltaje_recibido, yerr=error_Vr, fmt='none', ecolor='r')
    plt.show()

def devuelve_fourier(url):

  datos = pd.read_csv(url,header=None)

  #t: tiempo; volt: voltaje.  Dejo el tiempo comentado xq no es necesario, solo hace falta el dt de muestreo
  #t = datos[3].to_numpy()
  volt = datos[4].to_numpy()

  #N: cantidad de puntos    dt: diferencia temporal entre puntos
  N = len(volt)
  dt = float(datos[1][1])

  yf = sc.fft.fft(volt)
  xf = sc.fft.fftfreq(N,d=dt)[35:48]   #pongo del 35 al 48 xq es donde se ve bien la campana. cambiar por [:N//2] para todo el espectro

  return(2.0/N * np.abs(yf[35:48]) , xf) #Ni idea xq el 2pi/N

num = ['00','01','02','03','04','05','06','07','08','09','10','11']

yPromedio = np.zeros(13)

for i in range(len(num)):#12
  y,x=devuelve_fourier('/content/Labo_2/Datos onda cuadrada v1/ALL00'+num[i]+'/F00'+num[i]+'CH1.CSV')
  yPromedio += y

plt.xlabel('Frecuencia (kHz)')
plt.ylabel('???')

plt.scatter(x, yPromedio/12)
plt.show()