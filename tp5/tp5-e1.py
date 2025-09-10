
import random as rd
import numpy as np

"""
Simula el tiempo que tarda un operario en realizar una tarea
basado en una tabla de frecuencias relativas acumuladas.

Returns:
    float: Tiempo de operación en unidades de tiempo
"""

def calcular_acumulada(array):
    res = []
    acumulada = 0
    for num in array:
        acumulada += num
        res.append(round(acumulada, 2))
    return res


def restar_arrays(array1, array2):
    if len(array1) == len(array2):
        res = []
        for i in range(len(array2) - 1):
            resta = array2[i] - array1[i+1] 
            if resta < 0:
                res.append(0)
            else:
                res.append(round(resta, 2))
        return res
    else:
        return "Los arrays deben ser de igual longitud"

def simular_tiempo_operario_A():

    p = rd.random()
    
    # Tabla de rangos y tiempos correspondientes
    rangos = [
        (0, 0.0180, 0.25),
        (0.0180, 0.0299, 0.30),
        (0.0299, 0.0898, 0.35),
        (0.0898, 0.2216, 0.40),
        (0.2216, 0.3892, 0.45),
        (0.3892, 0.5509, 0.50),
        (0.5509, 0.6946, 0.55),
        (0.6946, 0.8024, 0.60),
        (0.8024, 0.8922, 0.65),
        (0.8922, 0.9581, 0.70),
        (0.9581, 0.9880, 0.75),
        (0.9880, 1.0000, 0.80)
    ]
    
    # Buscar el tiempo correspondiente al número aleatorio generado
    for min_rango, max_rango, tiempo in rangos:
        if min_rango <= p < max_rango:
            return tiempo
            
    return rangos[-1][2]  # Retorna el último tiempo si p = 1.0



def simular_tiempo_operario_B():
    p = rd.random()
    
    # Tabla de rangos y tiempos correspondientes para operario B
    rangos = [
        (0, 0.0174, 0.25),
        (0.0174, 0.1043, 0.30),
        (0.1043, 0.2522, 0.35),
        (0.2522, 0.4261, 0.40),
        (0.4261, 0.5826, 0.45),
        (0.5826, 0.6957, 0.50),
        (0.6957, 0.7826, 0.55),
        (0.7826, 0.8348, 0.60),
        (0.8348, 0.8783, 0.65),
        (0.8783, 0.9217, 0.70),
        (0.9217, 0.9565, 0.75),
        (0.9565, 0.9826, 0.80),
        (0.9826, 1.0000, 0.85)
    ]
    
    # Buscar el tiempo correspondiente al número aleatorio generado
    for min_rango, max_rango, tiempo in rangos:
        if min_rango <= p < max_rango:
            return tiempo
            
    return rangos[-1][2]  # Retorna el último tiempo si p = 1.0


print(simular_tiempo_operario_A())
print(simular_tiempo_operario_B())

tiempos_a = []
tiempos_b = []

for i in range(20):
    tiempos_a.append(simular_tiempo_operario_A())
    tiempos_b.append(simular_tiempo_operario_B())

matrix = np.matrix([tiempos_a, tiempos_b])

print(f'El tiempo total de A luego de 20 iteraciones es {sum(tiempos_a)}')
print(f'El tiempo total de B luego de 20 iteraciones es {sum(tiempos_b)}')

print(matrix)



tiempos_a[0] = 0
disponibles_para_b = calcular_acumulada(tiempos_a)
iniciacion_b = calcular_acumulada([0] + tiempos_b[0: len(tiempos_b) - 1])
finalizacion_b = calcular_acumulada(tiempos_b)

print(disponibles_para_b)
print(iniciacion_b)
print(finalizacion_b)
print(restar_arrays(disponibles_para_b, finalizacion_b))

# class Estadisticas:
#     def __init__(self, tA, tB):
#         self.tA = tA
#         self.tB = tB
#         self.transporte = 0.5
#         self.tiempo = 0

#     def calcular():
#         return "hola"



