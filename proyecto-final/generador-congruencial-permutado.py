
import matplotlib.pyplot as plt


def rotar_binario_dinamico(n, k, direccion="izquierda"):

    if n < 0:
        raise ValueError("Esta rotación dinámica está diseñada para enteros positivos.")
    if n == 0:
        return 0

    bits = n.bit_length()
    
    k = k % bits

    mask = (1 << bits) - 1 

    if direccion.lower() == "izquierda":

        parte_izquierda = (n << k) & mask
        parte_derecha = n >> (bits - k)
        
        return parte_izquierda | parte_derecha
        
    elif direccion.lower() == "derecha":
    
        parte_derecha = n >> k
        parte_izquierda = (n << (bits - k)) & mask
        
        return parte_derecha | parte_izquierda
        
    else:
        raise ValueError("La dirección debe ser 'izquierda' o 'derecha'.")


class PCG:

    def __init__(self, estado, a, c, mod):        
        self.mod = mod
        self.estado = estado
        self.multiplicador = a
        self.incremento = c
        self.y = 2700259504

    def generar(self):
        self.aleatorios = []

        generar = True
        index = 0
        
        while generar:
            
            self.estado = (self.estado * self.multiplicador + self.incremento) % self.mod
            n = self.__generar_numero()

            if (n in self.aleatorios) or (index == pow(10, 5)):
                generar = False
                self.__normalizar()
                break
            else:
                index += 1

            self.aleatorios.append(n)

        
        return self.aleatorios
    
    def __generar_numero(self):
        rotar = rotar_binario_dinamico(self.estado, int(bin(self.estado)[2:7], 2), 'derecha')
        n = int(bin(rotar ^ self.y), 2)
        print(n, len(bin(n)[2:]))
        return n
    
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


modulo = pow(2, 64)
seed = 12345
multiplicador = 6364136223846793005
incremento = 1442695040888963407

algoritmo = PCG(seed, multiplicador, incremento, modulo)
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