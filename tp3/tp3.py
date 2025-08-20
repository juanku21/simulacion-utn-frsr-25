
import random

azul = 0
blanco = 0

for i in range(pow(10, 3)):
    num = random.random()
    if num > 0.5:
        blanco += 1
    else:
        azul += 1

print(azul)
print(blanco)


azul = 0
blanco = 0

for i in range(pow(10, 6)):
    x = random.random()
    y = random.random()

    if (x + y) > 1:
        blanco += 1
    else:
        azul += 1

print(azul)
print(blanco)