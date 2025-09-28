
import random as rd
import matplotlib.pyplot as plt


def promedio(array):
    avg = sum(array) / len(array)
    return avg


class Caminate:

    def __init__(self):
        self.origen = (0,0)
        self.posicion_x = self.origen[0]
        self.posicion_y = self.origen[1]
    
    def mover(self):
        num = rd.random()
        if num >= 0 and num < 0.25:
            self.posicion_x += 1
        elif num >=  0.25 and num < 0.5:
            self.posicion_x -= 1
        elif num >=  0.5 and num < 0.75:
            self.posicion_y += 1
        else:
            self.posicion_y -= 1

    def get_posicion_x(self):
        return self.posicion_x
    
    def get_posicion_y(self):
        return self.posicion_y
    
    def get_origen(self):
        return self.origen


cantidad_m = 10000
caminantes = []

for i in range(cantidad_m):
    caminante = Caminate()
    caminantes.append(caminante)

pasos = 50
posiciones_finales_x = []
posiciones_finales_y = []

for i in range(pasos):
    for caminante in caminantes:
        caminante.mover()
        if i == pasos - 1:
            posiciones_finales_x.append(caminante.get_posicion_x())
            posiciones_finales_y.append(caminante.get_posicion_y())


# 1er gráfico - Histograma 2D de posiciones finales

plt.hist2d(posiciones_finales_x, posiciones_finales_y, bins=50, cmap='Blues')      
plt.colorbar(label='Frecuencia')

plt.title("Distribución Final de Caminantes 2D")
plt.xlabel("X Final")
plt.ylabel("Y Final")

plt.show()