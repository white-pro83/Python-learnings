# ERROR COMUN DE PRINCIPIANTE
respuesta_usuario = "False" # Esto es texto

# La funcion bool evalua si el string esta vacio
es_verdad = bool(respuesta_usuario)

print(f'El valor es: {es_verdad}')
# Output: El valor es: True
# Por que? Porque el string "False" tiene 5 letras. NO esta vacio
 # Forma correcta de validar vacio:
texto_vacio = ""
print(bool(texto_vacio))    # False