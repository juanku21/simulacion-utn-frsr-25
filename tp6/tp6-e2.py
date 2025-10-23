
import random as rd
import math
import matplotlib.pyplot as plt

def choose_min(n, m):
    if n < m:
        return n
    elif n == m:
        return n
    else: 
        return m


class Vector:

    def __init__(self, size):
        self.size = size
        self.vector = []

        for i in range(self.size):
            # iniciar con valores aleatorios entre 0 o 1 para simular un estado inicial con particulas ocupando espacios
            self.vector.append(0) 
    
    def agregar(self, index):
        if index < self.size:
            self.vector[index] = 1
    
    def despegar(self, index):
        if index < self.size:
            self.vector[index] = 0

    def check_disponibilidad(self, index):
        if self.vector[index] == 1:
            return False
        elif self.vector[index] == 0:
            return True

    def get_size(self):
        return self.size
    
    def get_cantidad_ocupados(self):
        cant = 0
        for num in self.vector:
            if num == 1:
                cant += 1
        return cant
    
    def get_cantidad_libres(self):
        cant = 0
        for num in self.vector:
            if num == 0:
                cant += 1
        return cant

    def get_porcentaje_libres(self):
        return round(self.get_cantidad_libres() / self.get_size(), 5)
    
    def get_porcentaje_ocupados(self):
        return round(self.get_cantidad_ocupados() / self.get_size(), 5)


class Simulacion:
    
    def __init__(self, presion, iteraciones):
        self.presion = presion
        self.iteraciones = iteraciones
        self.vector = Vector(1000)

    def calcular_constantes(self):
        self.wdes = choose_min(1, pow(math.e, -1 * self.presion))
        self.wabs = choose_min(1, pow(math.e, self.presion))
    
    def simular(self):

        self.calcular_constantes()

        for i in range(self.iteraciones):

            casillero = rd.randint(0, self.vector.get_size() - 1)

            num = rd.random()

            if (num < self.wabs) and (self.vector.check_disponibilidad(casillero) == True):
                self.vector.agregar(casillero)
            elif (num < self.wdes) and (self.vector.check_disponibilidad(casillero) == False):
                self.vector.despegar(casillero)
    
    def get_libres(self):
        return self.vector.get_porcentaje_libres()
    
    def get_ocupados(self):
        return self.vector.get_porcentaje_ocupados()
    
    def get_presion(self):
        return self.presion


# Inicio del programa (código de principal)

x, libres, ocupados = [[], [], []]

for i in range(-10, 10):
    simulacion = Simulacion(i, pow(10,6))
    simulacion.simular()
    x.append(i)
    libres.append(simulacion.get_libres())
    ocupados.append(simulacion.get_ocupados())


plt.figure(figsize=(10, 6))  
plt.plot(x, libres, 'b-o') 
plt.plot(x, ocupados, 'r-o') 

plt.title('Casilleros')
plt.xlabel('Presion')
plt.ylabel('Proporsión')
plt.grid(True)
plt.legend('Presión vs Proporción de casilleros libres y ocupados')

plt.show()