
import matplotlib.pyplot as plt
import math


class CongruencialCuadratico:

    def __init__(self, semilla, a, b, c, mod):        
        self.semilla = semilla
        self.a = a
        self.b = b
        self.c = c
        self.mod = mod

    def generar(self):
        self.aleatorios = []

        self.aleatorios.append(self.semilla)

        index = 1
        generar = True
        
        while generar:
            
            n = self.a * pow(self.aleatorios[index - 1], 2) + self.b * self.aleatorios[index - 1] + self.c
            n = n % self.mod

            if n in self.aleatorios or index == pow(10, 5):
                generar = False
                self.__normalizar()
                break
            else:
                index += 1

            self.aleatorios.append(n)

        
        return self.aleatorios
    
    def __normalizar(self):
        for z in range(len(self.aleatorios)):
            self.aleatorios[z] = self.aleatorios[z] / self.mod

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


seed = 7126
a = 10
b = 5
c = 2
mod = pow(2, 32)

algoritmo = CongruencialCuadratico(seed, a, b, c, mod)
pseudoaleatorios = algoritmo.generar()
media = algoritmo.obtenerMedia()
varianza = algoritmo.obtenerVarianza()

print(f'El ciclo de vida de la secuencia es de {len(pseudoaleatorios)}')
print(f'La media de la secuencia es de {media}')
print(f'La varianza de la secuencia es de {varianza}')


x = range(len(pseudoaleatorios))

plt.figure(figsize=(10, 6))  
plt.plot(x, pseudoaleatorios, 'b-o')  
plt.axhline(y=media, color='r', linestyle='--', label=f'Media = {media:.5f}\nVarianza = {varianza:.5f}')

plt.title('Números Aleatorios Generados')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.grid(True)
plt.legend()

plt.show()