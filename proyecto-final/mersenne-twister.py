
import matplotlib.pyplot as plt


def obtener_31_bits_menores(n_32_bits):
    MASK_31_LSB = 0x7FFFFFFF
    return n_32_bits & MASK_31_LSB

def obtener_1_bit_mayor(n_32_bits):
    MSB_MASK = 0x80000000
    return n_32_bits & MSB_MASK

def obtener_1_bit_menor(n_32_bits):
    LSB_MASK = 0x1  # o simplemente 1
    return n_32_bits & LSB_MASK


class MersenneTwister:

    def __init__(self, semilla):        
        self.semilla = semilla
        self.estado = []
        self.mask = 0xFFFFFFFFFFFFFFFF
        self.a = 0x9908B0DF
        self.mask_b = 0x9D2C5680
        self.mask_c =  0xEFC60000

    def __cargar_vector_estado(self):
        n = self.semilla
        for i in range(624):
            n = 1812433253 * n + i 
            n = n % pow(2, 32)
            self.estado.append(n)
    
    def __templar(self, n):
        y = int(bin(n ^ int(bin(n >> 11), 2)), 2)
        y = int(bin(y ^ int(bin(self.mask_b & int(bin(y << 7), 2)), 2)), 2)
        y = int(bin(y ^ int(bin(self.mask_c & int(bin(y << 15), 2)), 2)), 2)
        salida = int(bin(y ^ int(bin(y >> 18), 2)) , 2)
        return salida

    def __twist(self):

        nuevo = []
        tap = 397

        for i in range(len(self.estado)):
            a = obtener_1_bit_mayor(self.estado[i])

            if (i + 1) >= (len(self.estado) - 1):
                b = obtener_31_bits_menores(self.estado[0])
            else:
                b = obtener_31_bits_menores(self.estado[i+1])

            x = bin(a)[2:] + bin(b)[2:]
            x = int(x, 2)

            x_desplazado = int(bin(x >> 1), 2)

            if (i + tap) <= (len(self.estado) - 1):
                n = int(bin(self.estado[i + tap]  ^ x_desplazado), 2)
            else:
                indice = (i + tap) - len(self.estado)
                n = int(bin(self.estado[indice]  ^ x_desplazado), 2)

            if x_desplazado == 1:
                n = int(bin(n ^ self.a))

            n = self.__templar(n)

            nuevo.append(n)
        
        self.estado = nuevo

    def __agregar_numeros(self):
        for num in self.estado:
            self.aleatorios.append(num)

    def __chequear(self):
        agregar = True
        for num in self.estado:
            if num in self.aleatorios:
                agregar = False
                break
        return agregar

    def generar(self):

        self.aleatorios = []

        self.__cargar_vector_estado()
        self.__agregar_numeros()

        generar = True
        index = 0
        
        while generar:
            
            self.__twist()
            agregar = self.__chequear()
            
            if (agregar == False) or (index * len(self.estado) >= pow(10, 5)):
                generar = False
                self.__normalizar()
                break
            else:
                index += 1

            self.__agregar_numeros()

        
        return self.aleatorios
    
    def __normalizar(self):
        max = sorted(self.aleatorios, reverse=True)[0]
        for z in range(len(self.aleatorios)):
            self.aleatorios[z] = self.aleatorios[z] / max

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



seed = pow(2, 32)

algoritmo = MersenneTwister(seed)
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