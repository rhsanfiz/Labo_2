import numpy as np
from os import listdir
from os.path import isfile, join
import pandas as pd
import matplotlib.pyplot as plt


mypath = "./mediciones interferencia/interferencia cable limpio"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

datos = []
valores = []
x=y=err= []
for i in range(len(onlyfiles)):
    f = pd.read_csv(mypath+'/'+onlyfiles[i])
    lux = f['(LX)'].to_numpy()
    # print(lux)
    # print(onlyfiles[i])
    # print(str(onlyfiles[i][:-4]))
    # print(str(len(onlyfiles[i])))
    # print(str(np.mean(lux)))
    # print(str(np.std(lux)))

#     try:
#         datos.append([int(onlyfiles[i][:-4]),int(len(onlyfiles[i])),np.mean(lux),np.std(lux)])
#         x.append(int(onlyfiles[i][:-4]))
#         y.append(np.mean(lux))
#         err.append(np.std(lux)/len(onlyfiles[i])**0.5)
#     except:
#         pass
    

# a = pd.DataFrame(datos,columns=('distancia','N','media','sigma'))
# print(a)
# a.to_csv(path_or_buf=mypath+'/datos (sin puntos dudosos).csv',index=False)
# b = a[a.distancia!=293]

# plt.scatter(b['distancia'],b['media'])#,yerr=err,xerr=1)
# plt.show()