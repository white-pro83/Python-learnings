# Programa: Funcion bool

# 1. Numeros (int y float)
print(bool(0))         # False (El vacio numerico)
print(bool(0.0))       # False
print(bool('42'))      # True (Existe valor)

# 2. Texto (Strings)
# Cadena vacia = Nada = False
print(bool(""))

# Cadena con espacio o texto = Algo = True
print(bool(" "))        # True
print(bool("Hola"))     # True

# 3. None (Ausencia total)
vacio = None
print(bool(vacio))      # False

print(bool(False))      # False
print(bool(True))       # True