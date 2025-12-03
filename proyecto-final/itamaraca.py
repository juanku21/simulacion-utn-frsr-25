
import matplotlib.pyplot as plt
import math


class GeneradorItamaraca:

    def __init__(self, semilla, xr, n=10000):        
        self.semilla = semilla
        self.racional = xr
        self.num = n

    def generar(self):
        self.aleatorios = []

        for num in self.semilla:
            print(num)
            self.aleatorios.append(num)

        index = len(self.aleatorios)
        generar = True
        
        while generar:
            
            n = self.aleatorios[index - 4] - self.aleatorios[index - 3] + self.aleatorios[index - 2] - self.aleatorios[index - 1]
            n = abs(n)
            n = int(abs(self.num - (n * self.racional))) % self.num

            print(n)

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
            self.aleatorios[z] = self.aleatorios[z] / self.num

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


seed = [200, 400, 876, 280]
xr = math.sqrt(3.85)

algoritmo = GeneradorItamaraca(seed, xr)
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