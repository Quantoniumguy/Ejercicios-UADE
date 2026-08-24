import os
#Ejercicio 1
#Pseudocodigo:
#Ingresar el nombre del usuario del programa y saludarlo. Ejemplo: si el usuario se llama Juan, se debe mostrar el mensaje “Hola Juan”.
#1) Ingresar nombre de usuario.
#2) Saludar al usuario con su nombre.
print("Ejercicio 1: Saludo al usuario")
nombre = str(input("Ingrese su nombre: "))
print("Hola " + nombre + ", bienvenido/a al programa.")

#Entradas: nombre del usuario.
#Salidas: saludo al usuario.

#Ejercicio 2
#Ingresar tres notas de una materia de un alumno y muestre la suma y el promedio.
#Pseudocodigo:
#1) Pedirle al usuario que ingrese 3 notas.
#2) Calcular la suma de las notas.
#3) Calcular el promedio de las notas.
#4) Mostrar la suma de notas al usuario.
#5) Mostrar el promedio de las notas al usuario.
print("Ejercicio 2: Cálculo del promedio de notas")
nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))
suma = nota1 + nota2 + nota3
promedio = suma / 3
print("La suma de las notas del alumno es: ", (suma))
print("El promedio de las notas del alumno es: ", (promedio))

#Entradas: Notas del alumno.
#Salidas: Suma y promedio de las notas del alumno.

#Ejercicio 3
#Pseudocodigo:
#1) Pedirle al usuario que ingrese el valor de un producto.
#2) Calcular el IVA del producto (21%).
#3) Calcular el precio final del producto sumando el IVA al valor original.
#4) Mostrar el precio final del producto al usuario.
print("Ejercicio 3: Cálculo del precio final con IVA")
valor_producto = float(input("Ingrese el valor del producto en pesos: "))
iva = valor_producto * 0.21
precio_final = valor_producto + iva
print("El iva del producto es: ", (iva))
print("El precio final del producto con IVA es: ", (precio_final))

#Entradas: Valor del producto.
#Salidas: IVA y precio final del producto con IVA.


#Ejercicio 4
#Pseudocodigo:
#1) Pedirle al 3 usuarios que ingresen la cantidad de dinero que quieran para la empresa.
#2) Calcular la suma total del dinero ingresado por los 3 usuarios.
#3) Mostrar la suma total del dinero a los 3 usuarios.
#4) Mostrar el promedio del dinero ingresado a los 3 usuarios.
print("Ejercicio 4: Suma y promedio de dinero ingresado por 3 usuarios")
usuario1 = float(input("Ingrese la cantidad de dinero del primer usuario: "))
usuario2 = float(input("Ingrese la cantidad de dinero del segundo usuario: "))
usuario3 = float(input("Ingrese la cantidad de dinero del tercer usuario: "))
suma = usuario1 + usuario2 + usuario3
promedio1 = (usuario1 * 100) / suma
promedio2 = (usuario2 * 100) / suma
promedio3 = (usuario3 * 100) / suma
print("La suma total del dinero ingresado es: ", (suma))
print("El promedio del dinero ingresado del usuario 1 es: ", (promedio1), "%")
print("El promedio del dinero ingresado del usuario 2 es: ", (promedio2), "%")
print("El promedio del dinero ingresado del usuario 3 es: ", (promedio3), "%")

#Entradas: Cantidad de dinero ingresado por los 3 usuarios.
#Salidas: Suma total del dinero ingresado y promedio del dinero ingresado por cada usuario.



os.system("pause")  