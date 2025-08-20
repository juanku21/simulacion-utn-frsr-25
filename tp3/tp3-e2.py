
import random

azul = 0
blanco = 0

for i in range(pow(10, 6)):
    x = random.random()
    y = random.random()

    if (pow(x, 2) + pow(y, 2)) > 1:
        blanco += 1
    else:
        azul += 1

print(azul)
print(blanco)

proporcion_azul = azul / pow(10, 6)

print(f'La estimación del número Pi es {proporcion_azul * 4}')