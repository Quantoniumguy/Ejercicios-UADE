import os

#Ejercicio: Leer 10 números enteros e imprimir el promedio, el mayor, y en qué orden fue ingresado el mayor valor. Si se ingresó más de una vez debe informar el primer ingreso.
#Pseudocodigo:
#1) Crear una lista vacía para almacenar los números ingresados.
#2) Crear una variable para almacenar el numero mayor ingresado.
#3) Crear una variable para almacenar la posición del mayor número ingresado.
#4) Crear un bucle que se repita 10 veces para pedir al usuario que ingrese un número entero.
#5) Dentro del bucle, agregar el número ingresado a la lista.
#6) Comparar el número ingresado con el numero mayor almacenado. Si es mayor, actualizar el numero mayor y la posición.
#7) Después del bucle, calcular el promedio de los números ingresados.
#8) Imprimir el promedio, el numero mayor y la posición del numero mayor ingresado.

print("Ejercicio: Leer 10 números enteros e imprimir el promedio, el mayor, y en qué orden fue ingresado el numero mayor.")
numeros = []
mayor = None
posicion_mayor = None

while len(numeros) < 10:
    try:
        numero = int(input(f"Ingrese un número entero {len(numeros) + 1}: "))
        numeros.append(numero)
        if mayor is None or numero > mayor:
            mayor = numero
            posicion_mayor = len(numeros)  # Guardar la posición (1-indexed)
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

promedio = sum(numeros) / len(numeros)

print(f"Promedio: {promedio}")
print(f"Numero Mayor: {mayor}")
print(f"Posición del numero Mayor: {posicion_mayor}")



os.system("pause")