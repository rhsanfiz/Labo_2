import pandas as pd
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import os
    

def derivada(modelo,x,dx=None,umbral=0.05):
    if dx:
        pass
    else:
        m = 0
        dm = umbral + 1
        while dm > umbral:
            pass

def chi2(x,y,ey,N,modelo,param,ex=0,dx=0):
    k = len(param)
    gl = N - k
    sigma_cuadrado = np.power(ey,2) + ex * derivada(modelo,x,dx)
    s2 = np.sum((np.power(y - modelo(x,*param),2)) / sigma_cuadrado)
    s2red = s2 / gl
    p = 1-sc.stats.chi2.cdf(s2,gl)
    print("El S cuadrado da: ", s2)
    print("El S cuadrado reducido da: ", s2red)
    print("El P-valor da: ", p)

def redondeo(val,err,cifras_significativas=1):
    from math import log10, floor
    e=round(err, -int(floor(log10(abs(err))))+cifras_significativas-1)
    v=round(val, -int(floor(log10(abs(e))))+cifras_significativas-1)
    return (v,e)

def lineal(x,m,b):
    return m*x+b

def lineal_malus(tita,tita_0):
    pass

def gaussiana(x, mu, sig):
    return (
        1.0 / (np.sqrt(2.0 * np.pi) * sig) * np.exp(-np.power((x - mu) / sig, 2.0) / 2)
    )

def seno_modulado2(pos, A, frecuencia, phi,x0,d,m):
    return A * np.abs(np.cos(frecuencia * (pos-x0) + phi)) * corte(pos,0.1,1,d,m,x0)#gaussiana(pos,x0,b)   #(1-b*(pos-x0)**2)




carpeta = '../Lampara de Sodio/intensidad vs distancia'
archivos = [f for f in os.listdir(carpeta) if os.path.isfile(carpeta+'/'+f)]
datos_interfranja = ['distancia,interfranja,error,N']
#'150b.csv','250b.csv','390.csv','400.csv',
for arch in ['100b.csv','rendija.csv']:#
    if arch != 'rendija.csv':

        try:
            dist = arch[:3]
            print(dist+' bien')
            url = carpeta + '/' + arch
            datos = pd.read_csv(url)
            val = datos['Gray_Value'].to_numpy()

            max_val = max(val)
            serie = -1*val+max_val
            sens = 0.05
            if int(dist)>400:
                sens = 0.1
            picos,otro = sc.signal.find_peaks(serie,prominence=max_val*sens,plateau_size=(None,None))#0.20*max_val)
            error_picos = otro['plateau_sizes']
            if dist=='530':
                print(picos,error_picos)

            y=[]
            for p in picos:
                y.append(val[p])


            fig, (ax1, ax2) = plt.subplots(1, 2, width_ratios=(4,2),figsize=(12,4))

            ax1.scatter(picos,y,label='mínimos',color='g')
            ax1.plot(range(len(val)),val)
            ax1.legend()
            ax1.set_xlabel('Separación (píxeles)')
            ax1.set_ylabel('Intensidad')
            ax1.set_title('a) Intensidad')

            xs = range(len(picos))
            param, otro = sc.optimize.curve_fit(lineal,xs,picos,sigma=error_picos)
            perr = np.sqrt(np.diag(otro))

            
            v,e = redondeo(param[0],perr[0])
            ax2.errorbar(xs,picos,yerr=error_picos,fmt='go',ecolor='r')
            ax2.plot(xs,lineal(xs,*param),label='$m='+str(v)+' \pm '+str(e)+'$')
            ax2.set_xlabel('N° mínimo')
            ax2.set_ylabel('Separación (píxeles)')
            ax2.set_title('b) Ajuste lineal')
            ax2.legend()

            N = len(picos)
            datos_interfranja.append(f'\n{dist},{v},{e},{N}')
            fig.suptitle('Distancia: '+dist)


            plt.show()
##            plt.savefig(f'{dist}.png')
        except:
            print(arch[:3]+' fallo')


##f = open('datos.csv','w')
##f.writelines(datos_interfranja)
##f.close()










    
