# Programa: Reemplazar textos en python

mensaje ("Hola mundo, mundo")


# Reemplazar TODAS las apariciones
nuevo = mensaje.replace("mundo", "python")
print(nuevo)
# Salida "Hola Python, Python"

# Reemplazar solo UNA vez
uno_solo = mensaje.replace("mundo", "dev", 1)
print(uno_solo)
# Salida: "Hola dev, mundo"
