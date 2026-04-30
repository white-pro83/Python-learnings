# Programa: Ejemplo de concatenacion de cadenas

# 1. Usando el operador +
nombre = "Lucia"
apellido = "Garcia"
nombre_completo = nombre + " " + apellido
print("Usando + :" + nombre_completo)

# 2. Usando el metodo print
edad = 28
print("Usando comas:", "Nombre:", nombre_completo, ", Edad:", edad)

# 3. Usando f-strings
ciudad = "Barcelona"
pais = "Espana"
profesion = "Ingeniera"
presentacion = f"Hola, soy {nombre_completo}, tengo {edad + 1} anos y soy {profesion} en {ciudad}, {pais}"
print(presentacion)