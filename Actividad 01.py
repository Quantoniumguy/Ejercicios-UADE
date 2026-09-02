import os

#Ejercicio: Leer 10 números enteros e imprimir el promedio, el mayor, y en qué orden fue ingresado el mayor valor. Si se ingresó más de una vez debe informar el primer ingreso.
#Pseudocodigo:
#1) Crear una lista vacía para almacenar los números ingresados.
#2) Crear una variable para almacenar el numero mayor ingresado.
#3) Crear una variable para almacenar la posición del mayor número ingresado.
#4) Crear un bucle que se repita 10 veces para pedir al usuario que ingrese un número entero.
#5) Dentro del bucle, agregar el número ingresado a la lista.
#6) Si se ingresa mas de una vez el mismo numero, se debe informar la primera posición en la que se ingreso el numero mayor.
#7) Comparar el número ingresado con el numero mayor almacenado. Si es mayor, actualizar el numero mayor y la posición.
#8) Después del bucle, calcular el promedio de los números ingresados.
#9) Imprimir el promedio, el numero mayor y la posición del numero mayor ingresado.


numeros = []
mayor = None
posicion_mayor = None

while len(numeros) < 10:

    try:
        numero = int(input(f"Ingrese un número entero {len(numeros) + 1}: "))

        # Verificar si el número ya fue ingresado
        if numero in numeros:
            posicion_anterior = numeros.index(numero) + 1
            print(f"ADVERTENCIA: el número {numero} ya fue ingresado en la posición {posicion_anterior}.")
            print("Por favor, ingrese otro número.")
            continue

        numeros.append(numero)

        # Buscar el mayor y su posición
        if mayor is None or numero > mayor:
            mayor = numero
            posicion_mayor = len(numeros)

    except ValueError:
        print("Por favor, ingrese un número entero válido.")

promedio = sum(numeros) / len(numeros)

print(f"Promedio: {promedio}")
print(f"Número Mayor: {mayor}")
print(f"Posición del número Mayor: {posicion_mayor}")




os.system("pause")