

import numpy as np
import matplotlib.pyplot as plt
import random
import math

# --- Variables Globales y de Configuración ---
SIZE = 30
NUM_WALKERS = 500000
SPAWN_RADIUS = SIZE // 2 - 5
DEATH_RADIUS = SIZE // 2 + 10
STICK_RADIUS = 1

class Point:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.is_dla = False
    
    def __str__(self):
        return f"Point({self.x}, {self.y}, {self.z}, {self.w}, DLA: {self.is_dla})"

class BoxCounting:

    def __init__(self, points):
        
        self.pruebas = []
        self.points = points

        total = 0
        for row in self.points:
            for other_row in row:
                for other_other_row in other_row:
                    total += len(other_other_row)

        current_size = int(pow(total, 1/4))

        while current_size >= 2:
            longitud = pow(current_size, 4)
            self.pruebas.append(longitud)
            current_size = int(current_size / 2)
    

    def dividir_en_cubos_4d(self, cantidad_por_subgrupo):

        if not self.points or not self.points[0] or not self.points[0][0] or not self.points[0][0][0]:
            return []

        num_w = len(self.points)
        num_profundidad = len(self.points[0])
        num_filas = len(self.points[0][0])
        num_columnas = len(self.points[0][0][0])

        subgrupo_w = 0
        subgrupo_profundidad = 0
        subgrupo_alto = 0
        subgrupo_ancho = 0
        
        for w in range(1, int(cantidad_por_subgrupo**(1/4)) + 2):
            if cantidad_por_subgrupo % w == 0:
                volumen_restante = cantidad_por_subgrupo // w
                for p in range(1, int(volumen_restante**(1/3)) + 2):
                    if volumen_restante % p == 0:
                        area_restante = volumen_restante // p
                        for r in range(1, int(area_restante**0.5) + 2):
                            if area_restante % r == 0:
                                c = area_restante // r
                                
                                factores = sorted([w, p, r, c])
                                dims = sorted([num_w, num_profundidad, num_filas, num_columnas])
                                
                                if (factores[0] <= dims[0] and factores[1] <= dims[1] and
                                    factores[2] <= dims[2] and factores[3] <= dims[3]):
                                    
                                    if (w * p * r * c) > (subgrupo_w * subgrupo_profundidad * subgrupo_alto * subgrupo_ancho):
                                        subgrupo_w = w
                                        subgrupo_profundidad = p
                                        subgrupo_alto = r
                                        subgrupo_ancho = c


        if subgrupo_w == 0 or subgrupo_profundidad == 0 or subgrupo_alto == 0 or subgrupo_ancho == 0:
            print(f"Advertencia: No se pueden formar subgrupos de {cantidad_por_subgrupo} puntos con una forma cúbica 4D dentro de la estructura existente.")
            print("Intentando encontrar el mayor subgrupo rectangular posible...")
            
            max_volumen = 0
            for w in range(1, num_w + 1):
                for p in range(1, num_profundidad + 1):
                    for r in range(1, num_filas + 1):
                        for c in range(1, num_columnas + 1):
                            volumen = w * p * r * c
                            if volumen <= cantidad_por_subgrupo and volumen > max_volumen:
                                max_volumen = volumen
                                subgrupo_w = w
                                subgrupo_profundidad = p
                                subgrupo_alto = r
                                subgrupo_ancho = c
            if max_volumen == 0:
                return []
            print(f"Se utilizará un subgrupo de {subgrupo_w}x{subgrupo_profundidad}x{subgrupo_alto}x{subgrupo_ancho} = {max_volumen} puntos.")


        subgrupos_resultantes = []
        

        for w_inicio in range(0, num_w, subgrupo_w):
            for p_inicio in range(0, num_profundidad, subgrupo_profundidad):
                for r_inicio in range(0, num_filas, subgrupo_alto):
                    for c_inicio in range(0, num_columnas, subgrupo_ancho):
                        
                        if (w_inicio + subgrupo_w <= num_w and
                            p_inicio + subgrupo_profundidad <= num_profundidad and
                            r_inicio + subgrupo_alto <= num_filas and
                            c_inicio + subgrupo_ancho <= num_columnas):
                            
                            subgrupo_actual = []

                            for w in range(w_inicio, w_inicio + subgrupo_w):
                                for p in range(p_inicio, p_inicio + subgrupo_profundidad):
                                    for r in range(r_inicio, r_inicio + subgrupo_alto):
                                        for c in range(c_inicio, c_inicio + subgrupo_ancho):
                                            subgrupo_actual.append(self.points[w][p][r][c])
                            subgrupos_resultantes.append(subgrupo_actual)
                            
        return subgrupos_resultantes


    def get_datos(self):

        sizes = []
        numero_cajas = []

        for prueba in self.pruebas:
            division = self.dividir_en_cubos_4d(prueba)
            cajas_dla = 0
            for caja in division:
                for point in caja:
                    if point.is_dla == True:
                        cajas_dla += 1
                        break
            
            numero_cajas.append(cajas_dla)
            sizes.append(int(pow(prueba, 1/4)))

        return [sizes, numero_cajas]


def get_neighbors(x, y, z, w):
    return [(x + 1, y, z, w), (x - 1, y, z, w), (x, y + 1, z, w), (x, y - 1, z, w), (x, y, z + 1, w), (x, y, z - 1, w), (x, y, z, w + 1), (x, y, z, w - 1)]

def generate_dla():

    print(f"Generando DLA con {NUM_WALKERS} caminantes en un espacio 4D de {SIZE}x{SIZE}x{SIZE}x{SIZE}...")
    
    # Inicializar grid de puntos
    all_points = [[[[Point(x, y, z, w) for w in range(SIZE)] for z in range(SIZE)] for y in range(SIZE)] for x in range(SIZE)]
    
    # Punto central como semilla
    center_x, center_y, center_z, center_w = SIZE // 2, SIZE // 2, SIZE // 2, SIZE // 2
    all_points[center_x][center_y][center_z][center_w].is_dla = True
    
    # Conjuntos para tracking
    dla_points_set = {(center_x, center_y, center_z, center_w)}
    dla_points_list = [(center_x, center_y, center_z, center_w)]

    for i in range(NUM_WALKERS):
        angle = random.uniform(0, 2 * np.pi)
        start_x = int(center_x + SPAWN_RADIUS * np.cos(angle))
        start_y = int(center_y + SPAWN_RADIUS * np.sin(angle))
        start_z = int(center_z + SPAWN_RADIUS * np.sin(angle))
        start_w = int(center_w + SPAWN_RADIUS * np.sin(angle))
        
        current_x = np.clip(start_x, 0, SIZE - 1)
        current_y = np.clip(start_y, 0, SIZE - 1)
        current_z = np.clip(start_z, 0, SIZE - 1)
        current_w = np.clip(start_w, 0, SIZE - 1)

        while True:
            dx, dy, dz, dw = random.choice([(0, 1, 0, 0), (0, -1, 0, 0), (1, 0, 0, 0), (-1, 0, 0, 0), (0, 0, 1, 0), (0, 0, -1, 0), (0, 0, 0, 1), (0, 0, 0, -1)])
            current_x += dx
            current_y += dy
            current_y += dz
            current_w += dw

            distance_from_center = np.sqrt((current_x - center_x)**2 + (current_y - center_y)**2 + (current_z - center_z)**2 + (current_w - center_w)**2)
            
            if distance_from_center > DEATH_RADIUS:
                break

            adhered = False
            for nx, ny, nz, nw in get_neighbors(current_x, current_y, current_z, current_w):
                if 0 <= nx < SIZE and 0 <= ny < SIZE and 0 <= nz < SIZE and 0 <= nw < SIZE and (nx, ny, nz, nw) in dla_points_set:
                    # Marcar el punto como parte del DLA
                    all_points[current_x][current_y][current_z][current_w].is_dla = True
                    dla_points_list.append((current_x, current_y, current_z, current_w))
                    dla_points_set.add((current_x, current_y, current_z, current_w))
                    adhered = True
                    print(f"Caminante {i+1}/{NUM_WALKERS} adherido. Total DLA: {len(dla_points_list)}")
                    break

            if adhered:
                break

    return all_points, dla_points_list



all_points, dla_points = generate_dla()

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


