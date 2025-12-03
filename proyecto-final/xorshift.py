
import matplotlib.pyplot as plt


class Xorshift:

    def __init__(self, estado):        
        self.estado = estado
        self.a = 13
        self.b = 17
        self.c = 5
        self.mask = 0xFFFFFFFFFFFFFFFF

    def generar(self):

        self.aleatorios = []

        self.aleatorios.append(self.estado)

        generar = True
        index = 0
        
        while generar:
            
            primero = int(bin(self.estado ^ int(bin(self.estado << self.a), 2)), 2)
            primero &= self.mask
            segundo = int(bin(primero ^ int(bin(primero >> self.b), 2)), 2)
            segundo &= self.mask
            tercero = int(bin(segundo ^ int(bin(segundo << self.c), 2)), 2)
            tercero &= self.mask

            n = tercero
            self.estado = n

            
            if (n in self.aleatorios) or (index == pow(10, 5)):
                generar = False
                self.__normalizar()
                break
            else:
                index += 1

            self.aleatorios.append(n)

        
        return self.aleatorios
    
    def __normalizar(self):
        for z in range(len(self.aleatorios)):
            self.aleatorios[z] = self.aleatorios[z] / pow(2, 64)

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



seed = 12345

algoritmo = Xorshift(seed)
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