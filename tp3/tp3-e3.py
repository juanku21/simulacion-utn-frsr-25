import random
import matplotlib.pyplot as plt

# Generar un millón de números aleatorios entre 1 y 100
numeros = [random.randint(1, 100) for _ in range(1_000_000)]

# Crear el histograma
plt.figure(figsize=(12, 6))
plt.hist(numeros, bins=100, range=(1, 101), edgecolor='black', alpha=0.7)

# Personalizar el gráfico
plt.title('Distribución de Números Aleatorios (1-100)')
plt.xlabel('Número')
plt.ylabel('Frecuencia')
plt.grid(True, alpha=0.3)

# Mostrar el gráfico
plt.show()



# Generar un millón de sumas de pares de números aleatorios entre 1 y 100
sumas = [random.randint(1, 100) + random.randint(1, 100) for _ in range(1_000_000)]

# Crear el histograma
plt.figure(figsize=(12, 6))
# Ajustamos bins y range para las sumas (que irán de 2 a 200)
plt.hist(sumas, bins=199, range=(2, 201), edgecolor='black', alpha=0.7)

# Personalizar el gráfico
plt.title('Distribución de Sumas de Pares de Números Aleatorios (1-100)')
plt.xlabel('Suma')
plt.ylabel('Frecuencia')
plt.grid(True, alpha=0.3)

# Mostrar el gráfico
plt.show()



# Generar un millón de sumas de ternas de números aleatorios entre 1 y 100
sumas = [random.randint(1, 100) + random.randint(1, 100) + random.randint(1, 100) for _ in range(1_000_000)]

# Crear el histograma
plt.figure(figsize=(12, 6))
# Ajustamos bins y range para las sumas (que irán de 3 a 300)
plt.hist(sumas, bins=298, range=(3, 301), edgecolor='black', alpha=0.7)

# Personalizar el gráfico
plt.title('Distribución de Sumas de Ternas de Números Aleatorios (1-100)')
plt.xlabel('Suma')
plt.ylabel('Frecuencia')
plt.grid(True, alpha=0.3)

# Mostrar el gráfico
plt.show()