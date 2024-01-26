gasto = int(input("Ingrese el costo de su consumo: "))
propina_porcentaje = int(input("Ingrese el porcentaje de propina que desea dejar (%): "))
propina= (gasto*propina_porcentaje)/100
print("Debe dejar de propina "+ str(propina) + " soles")