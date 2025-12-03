
import matplotlib.pyplot as plt


def encontrarCentro(num, cant):
    cadena = str(num)
    longitud = len(cadena)
    
    # Calcular posiciones inicial y final
    inicio = (longitud - cant) // 2
    fin = inicio + cant
    
    # Extraer los dígitos del centro
    return int(cadena[inicio:fin])


class CuadradosMedios:

    def __init__(self, semilla):
        self.semilla = semilla
        self.aleatorios = []
        self.normalizador = pow(10, len(str(semilla)))

    def generarCantidad(self, n):
        if len(self.aleatorios) != 0:
            self.aleatorios = []
        
        for i in range(n):
            cuadrado = pow(self.semilla, 2)
            medio = encontrarCentro(cuadrado, len(str(self.semilla)))
            normalizado = medio / self.normalizador

            self.aleatorios.append(normalizado)
            self.semilla = medio
        
        return self.aleatorios


    def generar(self):
        if len(self.aleatorios) != 0:
            self.aleatorios = []

        generar = True
        
        while generar:
            cuadrado = pow(self.semilla, 2)
            medio = encontrarCentro(cuadrado, len(str(self.semilla)))
            normalizado = medio / self.normalizador

            if normalizado in self.aleatorios:
                generar = False
                break

            self.aleatorios.append(normalizado)
            self.semilla = medio

        
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



algoritmo = CuadradosMedios(2025)
pseudoaleatorios = algoritmo.generar()
media = algoritmo.obtenerMedia()
varianza = algoritmo.obtenerVarianza()

print(f'El ciclo de vida de la secuencia es de {len(pseudoaleatorios)}')
print(f'La media de la secuencia es de {media}')
print(f'La varianza de la secuencia es de {varianza}')

# Crear datos para el eje x (índices de los números aleatorios)
x = range(len(pseudoaleatorios))

# Crear el gráfico
plt.figure(figsize=(10, 6))  # Tamaño de la figura
plt.plot(x, pseudoaleatorios, 'b-o')  # 'b-o' significa línea azul con marcadores circulares
plt.axhline(y=media, color='r', linestyle='--', label=f'Media = {media:.5f}\nVarianza = {varianza:.5f}')

# Personalizar el gráfico
plt.title('Números Aleatorios Generados')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.grid(True)
plt.legend()

# Mostrar el gráfico
plt.show()