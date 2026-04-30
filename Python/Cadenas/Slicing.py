# Programa: Aplicar el concepto slicing

texto = "PROGRAMACIÓN"

# 1. Basico [inicio:fin]
print(texto[0:4])   # "PROG" (El indice 4 no se incluye)

# 2. Atajo desde el inicio [:fin]
print(texto[:4])    # "PROG" (Asume inicio 0)

# 3. Atajo hasta el final [Inicio:]
print(texto[8:])    # "CION" (Hasta el ultimo char

# 4. Indices Negativos
print(texto[-4:])   # "CION" (Los ultimos 4)

# 5. Pasos [::paso] (Invertir cadena)
print(texto[::-1])  # "NOICAMARGORP"