import pandas as pd
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

def lineal(x,m,b):
    return m*x+b

def redondeo(val,err,cifras_significativas=1):
    from math import log10, floor
    e=round(err, -int(floor(log10(abs(err))))+cifras_significativas-1)
    v=round(val, -int(floor(log10(abs(e))))+cifras_significativas-1)
    return (v,e)

url = 'datos maxs.csv'
datos = pd.read_csv(url)
dist = datos['distancia'].to_numpy()
e_dist = 1
i = datos['interfranja'].to_numpy()
e_i = datos['error'].to_numpy()

k = 0.00459
e_k = 0.000015
i2 = i*k
e_i2 = i2 * (e_i/i+e_k/k)


param, otro = sc.optimize.curve_fit(lineal,dist,i2,sigma=e_i2)
perr = np.sqrt(np.diag(otro))
v,e = redondeo(param[0],perr[0])

plt.errorbar(dist,i2,yerr=e_i2,xerr=e_dist,fmt='go')
plt.plot(dist,lineal(dist,*param),label='$m='+str(v)+' \pm '+str(e)+'$')
plt.legend()
plt.show()


