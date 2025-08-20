

import matplotlib.pyplot as plt


def encontrarCentro(num, cant):
    cadena = str(num)
    longitud = len(cadena)
    
    # Calcular posiciones inicial y final
    inicio = (longitud - cant) // 2
    fin = inicio + cant
    
    # Extraer los dígitos del centro
    return int(cadena[inicio:fin])


class CongruencialMultiplicativo:

    def __init__(self, semilla, a, m=pow(2, 8)):
        self.semilla = semilla
        self.a = a
        self.c = 0
        self.m = m
        self.normalizador = m - 1
        self.aleatorios = []


    def generarCantidad(self, n):
        if len(self.aleatorios) != 0:
            self.aleatorios = []
        
        for i in range(n):
            numero = (self.a * self.semilla + self.c) % (self.m)
            normalizado = numero / self.normalizador

            self.aleatorios.append(normalizado)
            self.semilla = numero

        
        return self.aleatorios


    def generar(self):
        if len(self.aleatorios) != 0:
            self.aleatorios = []

        generar = True
        
        while generar:
            numero = (self.a * self.semilla + self.c) % (self.m)
            normalizado = numero / self.normalizador

            if normalizado in self.aleatorios:
                generar = False
                break

            self.aleatorios.append(normalizado)
            self.semilla = numero

        
        return self.aleatorios
    

    def obtenerMedia(self):
        if self.aleatorios:
            media = sum(self.aleatorios) / len(self.aleatorios)
            return media
        else:
            return 0


    def obtenerVarianza(self):
        promedio = self.obtenerMedia()
        sumaCuadrada = 0
        for num in self.aleatorios:
            sumaCuadrada += pow((num - promedio), 2)
        varianza = sumaCuadrada / (len(self.aleatorios) - 1)
        return varianza



algoritmo1 = CongruencialMultiplicativo(17, 203, pow(10, 5))
pseudoaleatorios1 = algoritmo1.generar()

print('1er Algoritmo')

print(f'El ciclo de vida de la secuencia es de {len(pseudoaleatorios1)}')
print(f'La media de la secuencia es de {algoritmo1.obtenerMedia()}')
print(f'La varianza de la secuencia es de {algoritmo1.obtenerVarianza()}')


algoritmo2 = CongruencialMultiplicativo(19, 211, pow(10, 3))
pseudoaleatorios2 = algoritmo2.generar()

print('2do Algoritmo')

print(f'El ciclo de vida de la secuencia es de {len(pseudoaleatorios2)}')
print(f'La media de la secuencia es de {algoritmo2.obtenerMedia()}')
print(f'La varianza de la secuencia es de {algoritmo2.obtenerVarianza()}')