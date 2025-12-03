
import matplotlib.pyplot as plt


class GeneradorLehmer:

    def __init__(self, a, mod, semilla):        
        self.mod = mod
        self.semilla = semilla
        self.multiplicador = a

    def generar(self):
        self.aleatorios = []

        self.aleatorios.append(self.semilla)

        index = 1
        generar = True
        
        while generar:
            
            n = self.aleatorios[index - 1] * self.multiplicador
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
seed = 315
multiplicador = 712


algoritmo = GeneradorLehmer(multiplicador, modulo, seed)
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