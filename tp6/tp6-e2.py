
import random as rd

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
        return round(self.get_cantidad_libres() / self.get_size(), 2)
    
    def get_porcentaje_ocupados(self):
        return round(self.get_cantidad_ocupados() / self.get_size(), 2)


m = 1000
wabs = 0.6
wdes = 0.3

vector = Vector(1000)

for i in range(m):

    casillero = rd.randint(0, vector.get_size() - 1)

    num = rd.random()

    if (num < wabs) and (vector.check_disponibilidad(casillero) == True):
        vector.agregar(casillero)
    elif (num < wdes) and (vector.check_disponibilidad(casillero) == False):
        vector.despegar(casillero)


print(f'El porcentaje de casilleros libres es {vector.get_porcentaje_libres()}')
print(f'El porcentaje de casilleros ocupados es {vector.get_porcentaje_ocupados()}')

