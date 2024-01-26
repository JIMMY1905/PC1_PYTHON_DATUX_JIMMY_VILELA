numero_1=int(input('ingrese un número: '))
numero_2=int(input('ingrese un segundo número: '))
seleccion=int(input('\nSeleccione una opción: Mostrar una suma de los dos números (1) \n Mostrar una resta de los dos números (el primero menos el segundo) (2) \nMostrar una multiplicación de los dos números (3) \n' ))
if seleccion == 1:
    print("\nresultado = " + str(numero_1 + numero_2))
elif seleccion == 2:
   print("\nresultado = " + str(numero_1 - numero_2))
elif seleccion == 3:
   print("\nresultado = " + str(numero_1 * numero_2))
else:
   print("No se seleccionó una opción válida")