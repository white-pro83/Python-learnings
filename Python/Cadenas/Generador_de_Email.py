# Hacer un generador de email para que sea mas facil encontrar los correos de una empresa
print("*** Generador de Email ***")

# Definimos el nombre del usuario
nombre_usuario = " Erick Esteban Ruiz Ramirez "
nombre_usuario_normalizado = nombre_usuario.strip().lower().replace(" ", ".")

# Datos adicionales. Empresa y dominio
nombre_empresa = " Global Mentoring "
dominio = "com.mx"

# modificamos los datos adicionales
nombre_empresa_normalizado = nombre_empresa.strip().lower().replace(" ", ".")
extencion_dominio = f'.{dominio}'

# Email Generado
email = f'{nombre_usuario_normalizado}@{nombre_empresa_normalizado}{extencion_dominio}'

print("Nombre usuario:", nombre_usuario)
print("Nombre usuario normalizado:", nombre_usuario_normalizado)
print()
print("Nombre empresa:", " "*4, nombre_empresa)
print("Extencion del dominio:", extencion_dominio)
print("Dominio de email normalizado:", f'@{nombre_empresa_normalizado}{extencion_dominio}')
print()
print("Email final generado:", email)