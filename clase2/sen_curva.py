
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(2*np.pi,10*np.pi,0.1)   # inicio,final,intervalo
y = np.sin(x)

fig = plt.figure()
plt.plot(x,y)
plt.savefig("/home/u196560/carpeta_test/sen_curva.png", dpi = 72)
plt.close(fig)
