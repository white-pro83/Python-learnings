print('*** Sistema Generador de Emails ***')

# Input de informacion principal
nombre = input('Ingrese su nombre: ')
apellidos = input('Ingrese su apellidos: ')
empresa = input('Ingrese su empresa: ')
extension_dominio = input('Ingrese su extension de dominio: ')

# Adaptar la info
nombre = nombre.strip().lower().replace(' ', '.')
apellidos = apellidos.strip().lower().replace(' ', '.')
empresa = empresa.strip().lower().replace(' ', '')
extension_dominio = extension_dominio.strip().lower()

# Juntar todo
email = f'{nombre}.{apellidos}@{empresa}{extension_dominio}'

# print
print()
print(f'Tu nuevo email generado por el sistema es:\n {email}\n Felicidades!')