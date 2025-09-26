

import random as rd
import matplotlib.pyplot as plt

class Caminate:

    def __init__(self):
        self.origen = 0
        self.posicion_x = self.origen
    
    def mover(self):
        num = rd.random()
        if num > 0.5:
            self.posicion_x += 1
        else:
            self.posicion_x -= 1

    def get_posicion(self):
        return self.posicion_x


cantidad_m = 500
caminantes = []

for i in range(cantidad_m):
    caminante = Caminate()
    caminantes.append(caminante)


pasos = 100

posiciones_finales = []

for i in range(pasos):
    for caminante in caminantes:
        caminante.mover()
        if i == pasos - 1:
            posiciones_finales.append(caminante.get_posicion())



# Crear el histograma (Frecuencias relativas de posiciones finales)

plt.figure(figsize=(10, 6))
plt.hist(posiciones_finales, bins='auto', density=True, alpha=0.7, color='blue', edgecolor='black')

plt.title('Distribución de posiciones finales')
plt.xlabel('Posición final')
plt.ylabel('Frecuencia relativa')
plt.grid(True, alpha=0.3)

plt.show()
