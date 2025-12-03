
import matplotlib.pyplot as plt


class GeneradorFibonacciRetardado:

    def __init__(self, mod, semilla, k, j):        
        self.mod = mod
        self.semilla = semilla
        self.k = k
        self.j = j

    def generar(self):
        self.aleatorios = []

        for num in self.semilla:
            self.aleatorios.append(num)

        index = len(self.aleatorios) - 1
        generar = True
        
        while generar:
            
            n = self.aleatorios[index - self.j] + self.aleatorios[index - self.k]
            n = n % self.mod

            if n in self.aleatorios:
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


modulo = 1000
seed = [200, 400, 876, 29, 634]
retardo_mayor = 5
retardo_menor = 3


algoritmo = GeneradorFibonacciRetardado(modulo, seed, retardo_mayor, retardo_menor)
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