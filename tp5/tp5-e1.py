
import random as rd
import numpy as np
from prettytable import PrettyTable

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


def tiempo_espera_piezas(array1, array2):
    if len(array1) == len(array2):
        res = [0]
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



'''
Simulamos ahora la línea de producción desde el punto de vista del Empleado B.
Considerando en tiempo = 0 en nuestro sistema de referencia, cuando este empleado 
recibe la primera pieza. 
'''



class LineaProduccion:

    def __init__(self, iteraciones):
        self.interaciones = iteraciones
        self.tiempos_a = []
        self.tiempos_b = []

        self.disponible_para_b = []
        self.comienza_b = []
        self.finaliza_b = []
        self.ocioso_b = []
        self.espera = []
        self.piezas_procesando_b = []
        self.piezas_en_espera = 0 


    def simular(self):

        for i in range(self.interaciones):
            tiempo_a = simular_tiempo_operario_A()
            tiempo_b = simular_tiempo_operario_B()

            print(tiempo_a, tiempo_b)

            self.tiempos_a.append(tiempo_a)
            self.tiempos_b.append(tiempo_b)

            piezas_operadas_b = 0

            if i == 0:
                self.disponible_para_b.append(0)
                self.comienza_b.append(0)
                self.finaliza_b.append(tiempo_b)
                self.ocioso_b.append(0)
                self.espera.append(0)
                self.piezas_procesando_b.append(0)

            else:
                self.disponible_para_b.append(round(self.disponible_para_b[-1] + tiempo_a, 2))

                espera = self.finaliza_b[-1] - self.disponible_para_b[-1]
                espera = round(espera, 2)

                if espera >= 0:
                    self.espera.append(espera)
                    self.ocioso_b.append(0)
                    self.comienza_b.append(self.finaliza_b[-1])
                    self.finaliza_b.append(round(self.comienza_b[-1] + tiempo_b, 2))
                    self.piezas_en_espera += 1

                else:
                    self.espera.append(0)
                    self.ocioso_b.append(-1 * espera)
                    self.comienza_b.append(self.disponible_para_b[-1])
                    self.finaliza_b.append(round(self.comienza_b[-1] + tiempo_b, 2))
                    self.piezas_en_espera = 0

                self.piezas_procesando_b.append(self.piezas_en_espera)

    def get_tabla(self):
        tabla = PrettyTable()
        tabla.field_names = ['Disponibles para B a las', 'B comienza a las', 'B termina a las', 'Ocioso B', 'Espera', 'Piezas procesando en B']

        for i in range(self.interaciones):
            tabla.add_row([
                self.disponible_para_b[i], 
                self.comienza_b[i], 
                self.finaliza_b[i], 
                self.ocioso_b[i], 
                self.espera[i],
                self.piezas_procesando_b[i]
            ])

        return tabla
    
    def calcular_ocio_b(self):
        return calcular_acumulada(self.ocioso_b)
    
    def calcular_espera_piezas(self):
        return calcular_acumulada(self.espera)
    
    



linea_produccion = LineaProduccion(20)
linea_produccion.simular()
print(linea_produccion.get_tabla())


