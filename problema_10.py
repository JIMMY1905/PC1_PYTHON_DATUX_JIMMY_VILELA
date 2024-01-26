lista_muestra = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
longitud = len(lista_muestra)
lista_nueva = []
x=0
while x<longitud:
    if x != 0 or x!= 4 or x !=5:
        lista_nueva=lista_muestra[x]
x=x+1
print(lista_nueva)