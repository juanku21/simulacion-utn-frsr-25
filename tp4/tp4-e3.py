

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


caminante = Caminate()

pasos = 50

x = []
y = []
origen = caminante.get_origen()

dominio = []
cuadratico = 0
cuadraticos = []
cuadraticos_medio = []

for i in range(pasos):

    pos_x = caminante.get_posicion_x()
    pos_y = caminante.get_posicion_y()

    caminante.mover()
    x.append(pos_x)
    y.append(pos_y)

    dominio.append(i)
    cuadratico += pow(pos_x, 2) + pow(pos_y, 2)
    cuadraticos.append(cuadratico)
    cuadraticos_medio.append(promedio(cuadraticos))


# 1er gráfico - Desplazamiento de un caminante en un plano bidimensional

plt.plot(x, y)
plt.plot(origen[0], origen[1], marker='o', color='red', markersize=10, label='Punto Inicio')

plt.title("Trayecto caminante en 2D")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.grid(True)
plt.legend()

plt.show()


# 2do gráfico - Desplazamiento Cuadrático Medio vs Tiempo

plt.figure(figsize=(10, 6)) 
plt.plot(dominio, cuadraticos_medio, 'r-o')  

plt.title('Desplazamiento Cuadrático vs Tiempo')
plt.xlabel('Unidad de tiempo')
plt.ylabel('<X^2 + Y^2>')
plt.grid(True)

plt.show()