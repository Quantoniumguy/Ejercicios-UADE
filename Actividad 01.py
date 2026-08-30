import os

#Ejercicio: Leer 10 números enteros e imprimir el promedio, el mayor, y en qué orden fue ingresado el mayor valor. Si se ingresó más de una vez debe informar el primer ingreso.
#Pseudocodigo:
#1) Crear una lista vacía para almacenar los números ingresados.
#2) Crear una variable para almacenar el mayor número ingresado.
#3) Crear una variable para almacenar la posición del mayor número ingresado.
#4) Crear un bucle que se repita 10 veces para pedir al usuario que ingrese un número entero.
#5) Dentro del bucle, agregar el número ingresado a la lista.
#6) Comparar el número ingresado con el mayor número almacenado. Si es mayor, actualizar el mayor número y la posición.
#7) Después del bucle, calcular el promedio de los números ingresados.
#8) Imprimir el promedio, el mayor número y la posición del mayor número ingresado.
print("Ejercicio: Leer 10 números enteros e imprimir el promedio, el mayor, y en qué orden fue ingresado el mayor valor.")
numeros = []
mayor = None
posicion_mayor = None

while len(numeros) < 10:
    try:
        numero = int(input(f"Ingrese el número entero {len(numeros) + 1}: "))
        numeros.append(numero)
        if mayor is None or numero > mayor:
            mayor = numero
            posicion_mayor = len(numeros)  # Guardar la posición (1-indexed)
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

promedio = sum(numeros) / len(numeros)

print(f"Promedio: {promedio}")
print(f"Mayor número: {mayor}")
print(f"Posición del mayor número: {posicion_mayor}")

os.system("pause")