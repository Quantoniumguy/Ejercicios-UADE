'''
Una empresa cuenta con N empleados, divididos en tres categorías A, B y C. Por cada empleado se lee su legajo, categoría y salario. Se solicita elaborar un informe que contenga: 

-Importe total de salarios pagados por la empresa. 

-Cantidad de empleados que ganan más de $20000. 

-Cantidad de empleados que ganan menos de $5000, cuya categoría sea “C”. 

-Legajo del empleado que más gana. 

-Sueldo más bajo. 

-Importe total de sueldos por cada categoría. 

-Salario promedio.
'''

'''
Ejemplo de entrada:
Ingrese la cantidad de empleados: 5
Ingrese el legajo del empleado 1: 1001
Ingrese la categoría del empleado 1 (A, B o C): A
Ingrese el salario del empleado 1: 25000
Ingrese el legajo del empleado 2: 1002
Ingrese la categoría del empleado 2 (A, B o C): B
Ingrese el salario del empleado 2: 18000
Ingrese el legajo del empleado 3: 1003
Ingrese la categoría del empleado 3 (A, B o C): C
Ingrese el salario del empleado 3: 4000
Ingrese el legajo del empleado 4: 1004
Ingrese la categoría del empleado 4 (A, B o C): C
Ingrese el salario del empleado 4: 6000
Ingrese el legajo del empleado 5: 1005
Ingrese la categoría del empleado 5 (A, B o C): A
Ingrese el salario del empleado 5: 22000


Ejemplo de salida:
Informe Final:
Importe total de salarios pagados por la empresa: $75000.00
Cantidad de empleados que ganan más de $20000: 2
Cantidad de empleados que ganan menos de $5000 y son de categoría C: 1
Legajo del empleado que más gana: 1005
Sueldo más bajo: $4000.00
Importe total de sueldos por categoría A: $47000.00
Importe total de sueldos por categoría B: $18000.00
Importe total de sueldos por categoría C: $10000.00
Salario promedio: $15000.00
'''


# Pseudocodigo:
# Solicitar al usuario que ingrese x cantidad de empleados.
# Solicitar al usuario que ingrese la categoria del empleado (A, B o C).
# Solicitar al usuario que ingrese el legajo del empleado.
# Solicitar al usuario que ingrese el salario del empleado.
# Sumar el salario ingresado al total de salarios.
# Si el salario es mayor a 20000, incrementar el contador de empleados que ganan más de 20000.
# Si el salario es menor a 5000 y la categoría es C, incrementar el contador de empleados que ganan menos de 5000 y son de categoría C.
# Si el salario es mayor al salario más alto registrado, actualizar el salario más alto.
# Almacenar el legajo del empleado que más gana.
# Almacenar el salario más bajo registrado.
# Calcular el importe total de sueldos por cada categoría.
# Hacer un promedio de los salarios ingresados.


# Declaración de variables
total_salarios = 0
empleados_mas_20000 = 0
empleados_menos_5000_categoria_c = 0

total_categoria_a = 0
total_categoria_b = 0
total_categoria_c = 0

mayor_salario = 0
menor_salario = 0
legajo_mayor_salario = None


# Solicitar cantidad de empleados
while True:
    entrada = input("Ingrese la cantidad de empleados: ").strip()

    if entrada == "":
        print("Error: no puede dejar este campo vacío. Intente nuevamente.")
        continue

    try:
        empleados = int(entrada)

        if empleados <= 0:
            print("Error: la cantidad de empleados debe ser mayor a 0.")
        else:
            break

    except ValueError:
        print("Error: debe ingresar un número entero. Intente nuevamente.")


# Ingreso de datos de los empleados
for ciclo in range(empleados):

    # Ingresar legajo
    while True:
        legajo = input(
            f"Ingrese el legajo del empleado {ciclo + 1}: "
        ).strip()

        if legajo == "":
            print("Error: el legajo no puede quedar vacío. Intente nuevamente.")
            continue

        if not legajo.isdigit():
            print("Error: el legajo debe contener solamente números.")
            continue

        break


    # Ingresar categoría
    while True:
        categoria = input(
            f"Ingrese la categoría del empleado {ciclo + 1} (A, B o C): "
        ).strip().upper()

        if categoria == "":
            print("Error: la categoría no puede quedar vacía. Intente nuevamente.")
            continue

        if categoria not in ["A", "B", "C"]:
            print("Error: la categoría debe ser A, B o C.")
            continue

        break


    # Ingresar salario
    while True:
        entrada = input(
            f"Ingrese el salario del empleado {ciclo + 1}: "
        ).strip()

        if entrada == "":
            print("Error: el salario no puede quedar vacío. Intente nuevamente.")
            continue

        try:
            salario = float(entrada)

            if salario < 0:
                print("Error: el salario no puede ser negativo.")
            else:
                break

        except ValueError:
            print("Error: debe ingresar un número válido. Intente nuevamente.")


    # Acumular salarios
    total_salarios += salario


    # Empleados que ganan más de $20000
    if salario > 20000:
        empleados_mas_20000 += 1


    # Empleados categoría C que ganan menos de $5000
    if salario < 5000 and categoria == "C":
        empleados_menos_5000_categoria_c += 1


    # Buscar el mayor salario
    if salario > mayor_salario:
        mayor_salario = salario
        legajo_mayor_salario = legajo


    # Buscar el menor salario
    if menor_salario == 0 or salario < menor_salario:
        menor_salario = salario


    # Total de salarios por categoría
    if categoria == "A":
        total_categoria_a += salario

    elif categoria == "B":
        total_categoria_b += salario

    elif categoria == "C":
        total_categoria_c += salario


# Calcular promedio
promedio = total_salarios / empleados


# Informe final
print("Informe Final:")
print(f"Importe total de salarios pagados por la empresa: ${total_salarios:.2f}")
print(f"Cantidad de empleados que ganan más de $20000: {empleados_mas_20000}")
print(f"Cantidad de empleados que ganan menos de $5000 y son de categoría C: {empleados_menos_5000_categoria_c}")
print(f"Legajo del empleado que más gana: {legajo_mayor_salario}")
print(f"Sueldo más bajo: ${menor_salario:.2f}")
print(f"Importe total de sueldos por categoría A: ${total_categoria_a:.2f}")
print(f"Importe total de sueldos por categoría B: ${total_categoria_b:.2f}")
print(f"Importe total de sueldos por categoría C: ${total_categoria_c:.2f}")
print(f"Salario promedio: ${promedio:.2f}")