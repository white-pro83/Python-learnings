print("*** Sistema de Tienda Online ***")

#Definir datos
nombre_producto = "Cámara digital"
precio_producto = 399.99
cantidad_inventario = 20
disponible = True

#Imprimir código
print("Producto:", nombre_producto)
print("Precio: $", precio_producto)
print("Cantidad inventario:", cantidad_inventario)
print("Disponible:", disponible)

#Redefinir datos
precio_producto = 280.00
cantidad_inventario = 0
disponible = False

#Reimprimir datos
print()
print("Producto:", nombre_producto)
print("Precio: $", precio_producto)
print("Cantidad inventario:", cantidad_inventario)
print("Disponible:", disponible)