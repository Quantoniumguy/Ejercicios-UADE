import os
#Ejercicios UVA 3

#Ejercio 1 a
#Pseudocodigo:
#1) Mostrar por pantalla el mensaje "Hola mundo".
print("Hola mundo")

#Ejercicio 1 b
#Ingresar el nombre del usuario del programa y saludarlo. Ejemplo: si el usuario se llama Juan, se debe mostrar el mensaje “Hola Juan”.
#Pseudocodigo:
#1) Solicitar al usuario que ingrese su nombre.
#2) Saludar al usuario mostrando el mensaje "Hola" seguido de su nombre.
nombre = str(input("Ingrese su nombre: "))
print("Hola " + nombre)


#Ejercicio 1 c
#Ingresar dos números y mostrar la suma y la diferencia. 
#Pseudocodigo:
#1) Solicitar al usuario que ingrese dos números.
#2) Calcular la suma de los dos números.
#3) Calcular la diferencia entre los dos números.
#4) Mostrar la suma y la diferencia al usuario.
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
suma = num1 + num2
diferencia = num1 - num2
print("La suma de los dos números es: ", suma)
print("La diferencia entre los dos números es: ", diferencia)

#Ejercicio 1 d
#Ingresar tres números y mostrar la suma y el promedio. 
#Pseudocodigo:
#1) Solicitar al usuario que ingrese tres números.
#2) Calcular la suma de los tres números.
#3) Calcular el promedio de los tres números.
#4) Mostrar la suma y el promedio al usuario.
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
suma = num1 + num2 + num3
promedio = suma / 3
print("La suma de los tres números es: ", suma)
print("El promedio de los tres números es: ", promedio)


#Ejercicio 1 e
#Pseudocodigo:
#1) Pedirle al usuario que ingrese el valor de un producto.
#2) Calcular el IVA del producto (21%).
#3) Calcular el precio final del producto sumando el IVA al valor original.
#4) Mostrar el precio final del producto al usuario.
valor_producto = float(input("Ingrese el valor del producto en pesos: "))
iva = valor_producto * 0.21
precio_final = valor_producto + iva
print("El iva del producto es: ", (iva))
print("El precio final del producto con IVA es: ", (precio_final))

os.system("pause")