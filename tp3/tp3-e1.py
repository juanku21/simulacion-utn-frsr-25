
import random


area_cuadrado = 1

azul = 0
blanco = 0

for i in range(pow(10, 6)):
    x = random.random()
    y = random.random()

    if (x + y) > 1:
        blanco += 1
    else:
        azul += 1


proporcion_azul = azul / (azul + blanco)

area_triangulo = area_cuadrado * proporcion_azul

print(f'El área del triángulo es de igual a {area_triangulo} unidades de área')