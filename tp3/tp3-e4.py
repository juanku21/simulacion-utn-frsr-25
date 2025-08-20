
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

particulas = []

for i in range(100):
    x = random.random() * 10
    y = random.random() * 10
    z = random.random() * 10
    particulas.append((x, y, z))

print(particulas)

# Separar las coordenadas x, y, z de las partículas
x = [particula[0] for particula in particulas]
y = [particula[1] for particula in particulas]
z = [particula[2] for particula in particulas]

# Crear la figura y el eje 3D
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Graficar las partículas
ax.scatter(x, y, z, c='b', marker='o', alpha=0.6)

# Personalizar el gráfico
ax.set_title('Distribución de Partículas en 3D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Ajustar los límites de los ejes
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)

# Agregar una grilla
ax.grid(True)

# Mostrar el gráfico
plt.show()