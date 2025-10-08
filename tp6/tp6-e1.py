
import random as rd

def simular_desde_vocal():
    num = rd.random()
    if num <= 0.13:
        return True
    elif num > 0.13 and num <= 1:
        return False

def simular_desde_consonante():
    num = rd.random()
    if num <= 0.33:
        return True
    elif num > 0.33 and num <= 1:
        return False


iteraciones = pow(10, 6)

last_letter = 'vocal'

vocales = 0
consonantes = 0

for i in range(iteraciones):
    if last_letter == 'vocal':
        res = simular_desde_vocal()
        if res == False:
            consonantes += 1
            last_letter = 'consonante'
        else:
            vocales += 1

    elif last_letter == 'consonante':
        res = simular_desde_consonante()
        if res == False:
            vocales += 1
            last_letter = 'vocal'
        else:
            consonantes += 1


print(f'La proporción de vocales es {vocales / iteraciones}')
print(f'La proporción de consonantes es {consonantes / iteraciones}')