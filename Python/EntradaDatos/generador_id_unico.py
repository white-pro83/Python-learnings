print('*** Sistema Generador de ID Unico ***')

# Informacion
nombre = input('Cual es tu nombre?: ')
apellido = input('Cual es tu apellido?: ')
fecha_nacimiento = input('Cual es tu año nacimiento? (YYYY): ')

# Proceso de generamiento de id
nombre_separado = nombre[0:2].upper().strip()
apellido_separado = apellido[0:2].upper().strip()
fecha_separada = fecha_nacimiento[2:4].upper().strip()

# Numeros aleatorios
from random import randint
random = randint(1000, 9999)

# Concatenar todo y hacerle print
print('Hola Juan,\n '
      'Tu nuevo numero de identificacion (ID) generado por el sistema es:\n'
      f'{nombre_separado}{apellido_separado}{fecha_separada}{random}\n'
      'Felicidades!'
      )


