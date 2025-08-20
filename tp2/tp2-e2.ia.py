import matplotlib.pyplot as plt
import numpy as np

def encontrar_periodo_productos_medios(semilla1, semilla2):
    numeros_vistos = {}
    aleatorios = []
    indices = []
    
    i = 0
    while True:
        # Multiplicar las semillas
        producto = semilla1 * semilla2
        str_producto = str(producto).zfill(8)
        medio = str_producto[2:6]
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
        semilla1 = semilla2
        semilla2 = medio
        i += 1

# Ejecutar el algoritmo
semilla_inicial1 = 2025
semilla_inicial2 = 5202
resultado = encontrar_periodo_productos_medios(semilla_inicial1, semilla_inicial2)

# Extraer solo el período
inicio = resultado['inicio']
longitud = resultado['longitud']
periodo_aleatorios = resultado['aleatorios'][inicio:inicio + longitud]
periodo_indices = range(longitud)

# Calcular estadísticos del período
media_periodo = np.mean(periodo_aleatorios)
varianza_periodo = np.var(periodo_aleatorios)
desv_std_periodo = np.sqrt(varianza_periodo)

# Mostrar resultados
print(f"Inicio del período: posición {inicio}")
print(f"Longitud del período: {longitud}")
print(f"Números del período: {periodo_aleatorios}")
print(f"Media del período: {media_periodo:.4f}")
print(f"Varianza del período: {varianza_periodo:.4f}")
print(f"Desviación estándar del período: {desv_std_periodo:.4f}")

# Crear el gráfico solo del período
plt.figure(figsize=(10, 6))
plt.plot(periodo_indices, periodo_aleatorios, 'g-o', label='Período')
plt.axhline(y=media_periodo, color='r', linestyle='--', 
label=f'Media = {media_periodo:.4f}\nVarianza = {varianza_periodo:.4f}')

# Personalizar el gráfico
plt.title('Período de la Secuencia - Método Productos Medios')
plt.xlabel('Posición en el período')
plt.ylabel('Valor')
plt.grid(True)
plt.legend()

plt.show()