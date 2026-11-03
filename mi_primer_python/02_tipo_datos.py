# nombre = "Camila" 
# ciudad = "Santiago" 
# print(nombre) 
# print(ciudad) 
# print(type(nombre)) 

pelicula = input('ingrese nombre de una pelicula: ')
videojuego = input('ingrese nombre de un videojuego: ')
asignatura = input('ingrese nombre de una asignatura: ')

print(pelicula , videojuego, asignatura)
print(type(asignatura))

edad = int(input('Ingrese su edad'))
cant_hermanos = int(input('Ingrese la cantidad de hermanos'))
año = int(input('Ingrese el año actual'))
print(f'Edad: {edad} Tipo de dato: {type(edad)} \n|\n Cantidad de Hermanos: {cant_hermanos} Tipo de dato: {type(cant_hermanos)} \n|\n Año actual: {año} Tipo de dato: {type(año)}')
print(f'Cambiando el tipo de dato de "Edad"')
print(f'{type(str(edad))}')

# precio = 1599.90 
# altura = 1.65 
# print(precio) 
# print(altura) 
# print(type(altura)) 

precio = float(input('Ingrese el valor de un videojuego en dolares americanos'))
temp = float(input('Ingrese la temperatura actual'))
promedio = float(input('Coloque su promedio del 1.0 al 7.0: '))
print(f'Precio del videojuego: {precio} {type(precio)}')
print(f'Temperatura actual: {temp} {type(temp)}')
print(f'Promedio de notas: {promedio} {type(promedio)}')

internet = True
tarea = False
clases = True

print(f'Tengo internet en casa? {internet} {type(internet)}')
print(f'Termine la tarea de especialidad? {tarea} {type(tarea)}')
print(f'Tengo clases mañana? {clases}')

nombre_producto = input('Ingrese el nombre del producto: ')
precio_producto = float(input('Ingresa el valor del producto en Dolares Americanos: '))
disponible_producto = True
cantidad_producto = int(input('Coloque la cantidad del producto: '))

print(f'Nombre: {nombre_producto} {type(nombre_producto)} \nPrecio: {precio_producto} {type(precio_producto)} \nDisponible: {disponible_producto} {type(disponible_producto)} \nCantidad de licencias: {cantidad_producto} {type(cantidad_producto)}')