
import numpy as np
import matplotlib.pyplot as plt
import random
import math

# --- Variables Globales y de Configuración ---
SIZE = 60
NUM_WALKERS = 140000
SPAWN_RADIUS = SIZE // 2 - 5
DEATH_RADIUS = SIZE // 2 + 10
STICK_RADIUS = 1

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.is_dla = False
    
    def __str__(self):
        return f"Point({self.x}, {self.y}, {self.z}, DLA: {self.is_dla})"

class BoxCounting:

    def __init__(self, points):
        
        self.pruebas = []
        self.points = points

        total = 0
        for row in self.points:
            for other_row in row:
                total += len(row)

        current_size = int(pow(total, 1/3))

        while current_size >= 2:
            longitud = pow(current_size, 3)
            self.pruebas.append(longitud)
            current_size = int(current_size / 2)
    

    def dividir_en_cubos(self, cantidad_por_subgrupo):

        if not self.points or not self.points[0] or not self.points[0][0]:
            return []

        # Obtener las dimensiones del cubo general
        num_profundidad = len(self.points)
        num_filas = len(self.points[0])
        num_columnas = len(self.points[0][0])

        # Encontrar las dimensiones óptimas (alto, ancho, profundidad) para los subgrupos cúbicos
        subgrupo_profundidad = 0
        subgrupo_alto = 0
        subgrupo_ancho = 0
        
        # Buscar tres factores cuya multiplicación sea la cantidad deseada
        for p in range(1, int(cantidad_por_subgrupo**(1/3)) + 2):
            if cantidad_por_subgrupo % p == 0:
                area_restante = cantidad_por_subgrupo // p
                for r in range(1, int(area_restante**0.5) + 2):
                    if area_restante % r == 0:
                        c = area_restante // r
                        
                        # Validar si las dimensiones encajan en la estructura principal
                        if p <= num_profundidad and r <= num_filas and c <= num_columnas:
                            if (p * r * c) > (subgrupo_profundidad * subgrupo_alto * subgrupo_ancho):
                                subgrupo_profundidad = p
                                subgrupo_alto = r
                                subgrupo_ancho = c
                        
                        # Considerar todas las permutaciones de los factores para el mejor ajuste
                        if p <= num_columnas and r <= num_profundidad and c <= num_filas:
                            if (p * r * c) > (subgrupo_profundidad * subgrupo_alto * subgrupo_ancho):
                                subgrupo_profundidad = r
                                subgrupo_alto = c
                                subgrupo_ancho = p


        if subgrupo_profundidad == 0 or subgrupo_alto == 0 or subgrupo_ancho == 0:
            print(f"Advertencia: No se pueden formar subgrupos de {cantidad_por_subgrupo} puntos con una forma cúbica dentro de la estructura existente.")
            print("Intentando encontrar el mayor subgrupo rectangular posible...")
            
            # Lógica para encontrar el mayor subgrupo si no hay un ajuste perfecto
            max_volumen = 0
            for p in range(1, num_profundidad + 1):
                for r in range(1, num_filas + 1):
                    for c in range(1, num_columnas + 1):
                        volumen = p * r * c
                        if volumen <= cantidad_por_subgrupo and volumen > max_volumen:
                            max_volumen = volumen
                            subgrupo_profundidad = p
                            subgrupo_alto = r
                            subgrupo_ancho = c
            if max_volumen == 0:
                return []
            print(f"Se utilizará un subgrupo de {subgrupo_profundidad}x{subgrupo_alto}x{subgrupo_ancho} = {subgrupo_profundidad * subgrupo_alto * subgrupo_ancho} puntos.")


        subgrupos_resultantes = []
        
        # Iterar sobre las 3 dimensiones para formar los cubos
        for p_inicio in range(0, num_profundidad, subgrupo_profundidad):
            for r_inicio in range(0, num_filas, subgrupo_alto):
                for c_inicio in range(0, num_columnas, subgrupo_ancho):
                    
                    # Asegurarse de que el subgrupo no exceda los límites del espacio 3D
                    if (p_inicio + subgrupo_profundidad <= num_profundidad and
                        r_inicio + subgrupo_alto <= num_filas and
                        c_inicio + subgrupo_ancho <= num_columnas):
                        
                        subgrupo_actual = []
                        for p in range(p_inicio, p_inicio + subgrupo_profundidad):
                            for r in range(r_inicio, r_inicio + subgrupo_alto):
                                for c in range(c_inicio, c_inicio + subgrupo_ancho):
                                    subgrupo_actual.append(self.points[p][r][c])
                        subgrupos_resultantes.append(subgrupo_actual)
                        
        return subgrupos_resultantes


    def get_datos(self):

        sizes = []
        numero_cajas = []

        for prueba in self.pruebas:
            division = self.dividir_en_cubos(prueba)
            cajas_dla = 0
            for caja in division:
                for point in caja:
                    if point.is_dla == True:
                        cajas_dla += 1
                        break
            
            numero_cajas.append(cajas_dla)
            sizes.append(int(math.sqrt(prueba)))

        return [sizes, numero_cajas]


def get_neighbors(x, y, z):
    return [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]

def generate_dla():

    print(f"Generando DLA con {NUM_WALKERS} caminantes en un plano de {SIZE}x{SIZE}...")
    
    # Inicializar grid de puntos
    all_points = [[[Point(x, y, z) for z in range(SIZE)] for y in range(SIZE)] for x in range(SIZE)]
    
    # Punto central como semilla
    center_x, center_y, center_z = SIZE // 2, SIZE // 2, SIZE // 2
    all_points[center_x][center_y][center_z].is_dla = True
    
    # Conjuntos para tracking
    dla_points_set = {(center_x, center_y, center_z)}
    dla_points_list = [(center_x, center_y, center_z)]

    for i in range(NUM_WALKERS):
        angle = random.uniform(0, 2 * np.pi)
        start_x = int(center_x + SPAWN_RADIUS * np.cos(angle))
        start_y = int(center_y + SPAWN_RADIUS * np.sin(angle))
        start_z = int(center_z + SPAWN_RADIUS * np.sin(angle))
        
        current_x = np.clip(start_x, 0, SIZE - 1)
        current_y = np.clip(start_y, 0, SIZE - 1)
        current_z = np.clip(start_z, 0, SIZE - 1)

        while True:
            dx, dy, dz = random.choice([(0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1)])
            current_x += dx
            current_y += dy
            current_y += dz

            distance_from_center = np.sqrt((current_x - center_x)**2 + (current_y - center_y)**2 + (current_z - center_z)**2)
            
            if distance_from_center > DEATH_RADIUS:
                break

            adhered = False
            for nx, ny, nz in get_neighbors(current_x, current_y, current_z):
                if 0 <= nx < SIZE and 0 <= ny < SIZE and 0 <= nz < SIZE and (nx, ny, nz) in dla_points_set:
                    # Marcar el punto como parte del DLA
                    all_points[current_x][current_y][current_z].is_dla = True
                    dla_points_list.append((current_x, current_y, current_z))
                    dla_points_set.add((current_x, current_y, current_z))
                    adhered = True
                    print(f"Caminante {i+1}/{NUM_WALKERS} adherido. Total DLA: {len(dla_points_list)}")
                    break

            if adhered:
                break

    return all_points, dla_points_list

def plot_dla(all_points, dla_points):
    plt.figure(figsize=(10, 10), facecolor='black')
    ax = plt.gca()
    ax.set_facecolor('black')

    # Extraer coordenadas de puntos DLA
    x_coords = [p[0] for p in dla_points]
    y_coords = [p[1] for p in dla_points]
    z_coords = [p[2] for p in dla_points]

    plt.scatter(x_coords, y_coords, s=1, color='lightgray', marker='s')
    
    plt.title("Estructura DLA generada por Agregación Limitada por Difusión", color='white')
    plt.xlabel("Posición X", color='white')
    plt.ylabel("Posición Y", color='white')
    
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    plt.xlim(0, SIZE)
    plt.ylim(0, SIZE)
    plt.axis('off')
    plt.gca().set_aspect('equal', adjustable='box')
    
    plt.show()


def plot_dla_3d(all_points, dla_points):
    
    # Crear una figura y un conjunto de ejes con proyección 3D
    fig = plt.figure(figsize=(10, 10), facecolor='black')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('black')
    
    # Extraer las coordenadas X, Y y Z de los puntos DLA
    x_coords = [p[0] for p in dla_points]
    y_coords = [p[1] for p in dla_points]
    z_coords = [p[2] for p in dla_points]
    
    # Graficar los puntos en 3D
    # Usamos ax.scatter en lugar de plt.scatter
    ax.scatter(x_coords, y_coords, z_coords, s=1, color='blue', marker='o')
    
    # Configurar títulos y etiquetas de los ejes
    ax.set_title("Estructura DLA generada por Agregación Limitada por Difusión", color='white')
    ax.set_xlabel("Posición X", color='white')
    ax.set_ylabel("Posición Y", color='white')
    ax.set_zlabel("Posición Z", color='white')
    
    # Configurar los parámetros de las marcas de los ejes
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.tick_params(axis='z', colors='white')
    
    # Configurar límites y el aspecto (opcional)
    # plt.xlim(0, SIZE) # Estas líneas no se usan para 3D de la misma manera
    # plt.ylim(0, SIZE)
    # ax.set_aspect('equal') # No es compatible directamente con proyección 3D
    
    plt.show()


all_points, dla_points = generate_dla()
plot_dla_3d(all_points, dla_points)


caracterizacion = BoxCounting(all_points)
datos_dla = caracterizacion.get_datos()

x = []
y = []

for i in range(len(datos_dla[0])):
    xi = math.log(1 / datos_dla[0][i])
    x.append(xi)
    yi = math.log(datos_dla[1][i])
    y.append(yi)


# 1er gráfico - Ajuste lineal de la caracterización de un fractal mediante algoritmo de Box Counting 

plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', label='Puntos de datos')

m, b = np.polyfit(x, y, 1) 
dimension_fractal = m

x_fit = np.linspace(min(x), max(y), 100)
y_fit = m * x_fit + b
plt.plot(x_fit, y_fit, color='red', linestyle='-', label=f'Ajuste lineal (D = {dimension_fractal:.3f})')


plt.title('Gráfico de Box-Counting')
plt.xlabel('Log(1/r)')
plt.ylabel('Log(N(r))')
plt.legend()
plt.grid(True)
plt.show()


