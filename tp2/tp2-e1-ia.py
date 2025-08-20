import matplotlib.pyplot as plt
import numpy as np

def encontrar_periodo(semilla):
    numeros_vistos = {}  # Diccionario para almacenar número -> posición
    aleatorios = []
    indices = []
    
    i = 0
    while True:
        cuadrado = pow(semilla, 2)
        medio = str(cuadrado)[1:5]
        medio = int(medio)
        aleatorio_normalizado = medio / 10000
        
        if medio in numeros_vistos:
            inicio_periodo = numeros_vistos[medio]
            longitud_periodo = i - inicio_periodo
            return {
                'inicio': inicio_periodo,
                'longitud': longitud_periodo,
                'aleatorios': aleatorios,
                'indices': indices
            }
        
        numeros_vistos[medio] = i
        aleatorios.append(aleatorio_normalizado)
        indices.append(i)
        semilla = medio
        i += 1

# Ejecutar el algoritmo
semilla_inicial = 2025
resultado = encontrar_periodo(semilla_inicial)

# Extraer solo el período
inicio = resultado['inicio']
longitud = resultado['longitud']
periodo_aleatorios = resultado['aleatorios'][inicio:inicio + longitud]
periodo_indices = range(longitud)

# Calcular estadísticos del período
media_periodo = np.mean(periodo_aleatorios)
varianza_periodo = np.var(periodo_aleatorios)
desv_std_periodo = np.sqrt(varianza_periodo)

print(f"Inicio del período: posición {inicio}")
print(f"Longitud del período: {longitud}")
print(f"Números del período: {periodo_aleatorios}")
print(f"Media del período: {media_periodo:.4f}")
print(f"Varianza del período: {varianza_periodo:.4f}")
print(f"Desviación estándar del período: {desv_std_periodo:.4f}")

# Crear el gráfico solo del período
plt.figure(figsize=(10, 6))
plt.plot(periodo_indices, periodo_aleatorios, 'b-o', label='Período')
plt.axhline(y=media_periodo, color='r', linestyle='--', 
label=f'Media = {media_periodo:.4f}\nVarianza = {varianza_periodo:.4f}')

# Personalizar el gráfico
plt.title('Período de la Secuencia - Método Cuadrados Medios')
plt.xlabel('Posición en el período')
plt.ylabel('Valor')
plt.grid(True)
plt.legend()

plt.show()