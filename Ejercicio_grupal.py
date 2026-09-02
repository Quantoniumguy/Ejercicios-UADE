'''Ingresar las notas de los dos parciales de un alumno e indicar si promociona, aprueba o debe recuperar. 
Si el valor de la nota no está entre 0 y 10, debe informar un error.  
Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
Recupera cuando al menos una de las dos notas es menor a 4.'''


#Pedirle al usuario que ingrese las notas de los dos parciales
#Se tiene que promediar el valor de las notas
#Se tiene que mostrar por pantalla si promociona, aprueba o debe recuperar
#El alumno aprueba si las notas de ambos parciales son mayores o iguales a 4
#El alumno promociona si las notas de ambos parciales son mayores o iguales a 7
#El alumno debe recuperar si al menos una de las dos notas es menor a 4

nota_1 = int(input("Ingrese a primera nota (0-10): "))
while nota_1 < 0 or nota_1 > 10:
    nota_1 = int(input("Nota inválida. Ingrese a primera nota (0-10): "))
 
nota_2 = int(input("Ingrese a segunda nota (0-10): "))
while nota_2 < 0 or nota_2 > 10:
    nota_2 = int(input("Nota inválida. Ingrese a segunda nota (0-10): "))
 
promedio = (nota_1 + nota_2) / 2
 
if promedio >= 7:
    print(f"El alumno promocionó con un promedio de: {promedio}")
elif promedio >= 4:
    print("El alumno aprobó con un promedio de:", promedio)
elif promedio < 4:
    print("El alumno está reprobado con un promedio de:", promedio)