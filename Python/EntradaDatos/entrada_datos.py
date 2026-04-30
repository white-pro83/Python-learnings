# Programa: Entrada Datos Python
nombre = input("ingrese su nombre: ")
print(f'Tu nombre es: {nombre}')

# Cuidado con la conversion de tipos al trabajar con valores numericos
# Forma Correcta: Envolver con int() o float()

# Para enteros (edad, cantidad)
edad = int(input("ingrese su edad: "))
print(f'Tu edad es: {edad}')
print(edad + 5) # funciona!! (15 + 5 = 20)

# Para decimales (precio, altura)
altura = float(input("ingrese su altura: "))
print(f'Tu altura es: {altura}')