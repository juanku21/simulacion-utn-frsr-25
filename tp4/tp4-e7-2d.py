

import numpy as np
import matplotlib.pyplot as plt
import random as rd
import math

# --- Variables Globales y de Configuración ---
SIZE = 120
NUM_WALKERS = 15000
SPAWN_RADIUS = SIZE // 2 - 5
DEATH_RADIUS = SIZE // 2 + 10
STICK_RADIUS = 1

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_dla = False
    
    def __str__(self):
        return f"Point({self.x}, {self.y}, DLA: {self.is_dla})"


class Caminante:

    def __init__(self, possible_points):
        self.possible_points = possible_points
        num = rd.randint(0, len(self.possible_points) - 1)
        self.origen = self.possible_points[num]
        self.posicion_x = self.origen[0]
        self.posicion_y = self.origen[1]

        self.cuadratico = 0
        self.cuadraticos = []
        self.cuadraticos_medio = []
    
    def mover(self):

        movido = False    

        while movido != True:

            actual_x = self.posicion_x
            actual_y = self.posicion_y

            num = rd.random()
            if num >= 0 and num < 0.25:
                actual_x += 1
            elif num >=  0.25 and num < 0.5:
                actual_x -= 1
            elif num >=  0.5 and num < 0.75:
                actual_y += 1
            else:
                actual_y -= 1
            
            if (actual_x, actual_y) in self.possible_points:
                self.posicion_x = actual_x
                self.posicion_y = actual_y
                movido = True
        
        self.cuadratico += pow(self.posicion_x, 2) + pow(self.posicion_y, 2)
        self.cuadraticos.append(self.cuadratico)
        self.cuadraticos_medio.append(promedio(self.cuadraticos))

    def get_posicion_x(self):
        return self.posicion_x
    
    def get_posicion_y(self):
        return self.posicion_y
    
    def get_origen(self):
        return self.origen
    
    def get_cuadratico_medio(self):
        return self.cuadraticos_medio


def promedio(array):
    avg = sum(array) / len(array)
    return avg


def get_neighbors(x, y):
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def generate_dla():

    print(f"Generando DLA con {NUM_WALKERS} caminantes en un plano de {SIZE}x{SIZE}...")
    
    all_points = [[Point(x, y) for y in range(SIZE)] for x in range(SIZE)]
    
    center_x, center_y = SIZE // 2, SIZE // 2
    all_points[center_x][center_y].is_dla = True
    
    dla_points_set = {(center_x, center_y)}
    dla_points_list = [(center_x, center_y)]

    for i in range(NUM_WALKERS):
        angle = rd.uniform(0, 2 * np.pi)
        start_x = int(center_x + SPAWN_RADIUS * np.cos(angle))
        start_y = int(center_y + SPAWN_RADIUS * np.sin(angle))
        
        current_x = np.clip(start_x, 0, SIZE - 1)
        current_y = np.clip(start_y, 0, SIZE - 1)

        while True:
            dx, dy = rd.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            current_x += dx
            current_y += dy

            distance_from_center = np.sqrt((current_x - center_x)**2 + (current_y - center_y)**2)
            
            if distance_from_center > DEATH_RADIUS:
                break

            adhered = False
            for nx, ny in get_neighbors(current_x, current_y):
                if 0 <= nx < SIZE and 0 <= ny < SIZE and (nx, ny) in dla_points_set:
                    # Marcar el punto como parte del DLA
                    all_points[current_x][current_y].is_dla = True
                    dla_points_list.append((current_x, current_y))
                    dla_points_set.add((current_x, current_y))
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

    x_coords = [p[0] for p in dla_points]
    y_coords = [p[1] for p in dla_points]

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


# Inicio del código principal

all_points, dla_points = generate_dla()
plot_dla(all_points, dla_points)


cantidad_m = 1000
caminantes = []

for i in range(cantidad_m):
    caminante = Caminante(dla_points)
    caminantes.append(caminante)

pasos = 100

for i in range(pasos):
    for caminante in caminantes:
        caminante.mover()
    print(f'Los 1000 caminantes han realizado el paso {i}')


# 2do gráfico - Desplazamiento Cuadrático Medio vs Tiempo

tiempo = list(range(pasos))

for caminante in caminantes:
    plt.figure(figsize=(10, 6)) 
    plt.plot(tiempo, caminante.get_cuadratico_medio(), 'r-o')  

    plt.title('Desplazamiento Cuadrático vs Tiempo')
    plt.xlabel('Unidad de tiempo')
    plt.ylabel('<X^2 + Y^2>')
    plt.grid(True)

    plt.show()