
import random as rd
import matplotlib.pyplot as plt


def promedio(array):
    avg = sum(array) / len(array)
    return avg


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


caminante = Caminate()

pasos = 50

dominio = []
imagen = []

cuadratico = 0
cuadraticos = []
cuadraticos_medio = []


for i in range(pasos):

    caminante.mover()
    dominio.append(i)
    pos_x = caminante.get_posicion()
    imagen.append(pos_x)

    cuadratico += pow(pos_x, 2)
    cuadraticos.append(cuadratico)

    cuadraticos_medio.append(promedio(cuadraticos))



# ARREGLAR DESPLAZAMIENTO CUADRÁTICO MEDIO
print(f'El desplazamiento cuadrático medio es de {cuadraticos_medio[-1]}')


plt.figure(figsize=(10, 6))
plt.plot(dominio, imagen, 'b-o')

plt.title('Posición vs Tiempo')
plt.xlabel('Unidad de tiempo')
plt.ylabel('Posicion X')
plt.grid(True)

plt.show()



plt.figure(figsize=(10, 6)) 
plt.plot(dominio, cuadraticos_medio, 'r-o')  

plt.title('Desplazamiento Cuadrático vs Tiempo')
plt.xlabel('Unidad de tiempo')
plt.ylabel('X^2')
plt.grid(True)

plt.show()