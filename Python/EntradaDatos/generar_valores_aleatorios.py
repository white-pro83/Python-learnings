# Valores aleatorios con la funcion randint

# import random
from random import randint

#  Generar un numero aleatorio entre 1 y 10
numero = randint(1, 10)
print(f'N[umero aleatorio entre 1 y 10: {numero}')

# Simular un dado de seis caras
dado = randint(1, 6)
print(f'Resultado de lanzar el dado: {dado}')

# Si ponemos 'import random' tenemos que especificar 'random.randint(a, b)'