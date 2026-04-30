from operator import truediv

print('*** Sistema de Empleados ***')

# Nombre del empleado
nombre_empleado = input("Ingrese su nombre: ")

# Edad del empleado
edad_empleado = int(input("Ingrese su edad: "))

# Salario del empleado
salario_empleado = float(input("Ingrese su salario: "))

# Es jefe de departamento y/n
jefe_depto = input("Es jefe de departamento (Si/No)? ")

# Vamos a convertir a un tipo bool la variable jefe_depto
jefe_depto = jefe_depto.lower() == 'si'

# print
print(f'Nombre del empleado: {nombre_empleado}')
print(f'Edad del empleado: {edad_empleado}')
print(f'Salario del empleado: {salario_empleado:.5f}')
print(f'Jefe de departamento: {jefe_depto}')