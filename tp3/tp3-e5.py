
import random as rd
import math
import matplotlib.pyplot as plt
from prettytable import PrettyTable


def probabilidad_binomial(intentos, exitos, p_exito):
    dif = intentos - exitos
    coeficiente = math.factorial(intentos) / (math.factorial(exitos) * math.factorial(dif))
    p_fracaso = 1 - p_exito
    resultado = coeficiente * pow(p_exito, exitos) * pow(p_fracaso, dif)
    return resultado

class Volados:

    def __init__(self, disponible, meta):
        self.disponible = disponible
        self.meta = meta
        self.cantidad_anterior = []
        self.apuesta = []
        self.aleatorio = []
        self.resultado = []
        self.cantidad_posterior = []
    

    def get_disponible(self):
        return self.disponible
    
    def get_resultado_final(self):
        return self.resultado_final
    
    def simular(self):

        base = 10

        while (self.disponible <= self.meta) and (self.disponible > 0):

            if base > self.disponible:
                base = self.disponible

            self.cantidad_anterior.append(self.disponible)
            self.apuesta.append(base)

            numero = rd.random()

            if numero > 0.5:
                self.disponible -= base
                base = base * 2
                self.resultado.append(False)
            else:
                self.disponible += base
                base = 10
                self.resultado.append(True)
            
            self.aleatorio.append(numero)
            self.cantidad_posterior.append(self.disponible)
        
        if self.disponible == 0:
            self.resultado_final = False
        else:
            self.resultado_final = True


    def get_table(self):
        self.simular()

        table = PrettyTable()

        table.field_names = ['$ Antes del volado', '$ Apuesta', 'Aleatorio', '¿Ganó?', '$ Después del volado']

        for i in range(len(self.resultado)):
            table.add_row([
                self.cantidad_anterior[i],
                self.apuesta[i],
                self.aleatorio[i],
                self.resultado[i],
                self.cantidad_posterior[i]
            ])
        
        return table


# Inicio del programa principal

disponible = 30
meta = 50

# Ejemplo de muestra de funcionamiento 
volado = Volados(disponible, meta)
print(volado.get_table())
print(volado.get_resultado_final())

# estimación de probabilidad, $30 disponibles, $50 meta
ganadas = 0
perdidas = 0

for i in range(pow(10, 6)):
    volado = Volados(disponible, meta)
    volado.simular()
    resultado = volado.get_resultado_final()

    if resultado == True:
        ganadas += 1
    else:
        perdidas += 1


probabilidad = ganadas / (perdidas + ganadas)

print(f'La probabilidad de alcanzar la meta es de {probabilidad}')


# calculo de la distribución de probabilidad binomial 

intentos = 50
probabilidades = []

for i in range(intentos):
    p = probabilidad_binomial(intentos, i, probabilidad)
    probabilidades.append(p)


plt.figure(figsize=(12, 6))
dominio = range(intentos)

plt.bar(dominio, probabilidades)

# Personalizar el gráfico
plt.title(f'Distribución binomial - Exito en corridas con {intentos} intentos')
plt.xlabel('Exitos')
plt.ylabel('Probabilidad')

plt.grid(True, alpha=0.3)

plt.show()