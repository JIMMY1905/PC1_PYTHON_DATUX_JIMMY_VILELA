edad=int(input('ingresa tu edad: '))


if edad<4:
    print("Puede entrar gratis")
elif edad>=4 and edad<=18:
   print("La entrada cuesta $5")
elif edad>18:
   print("La entrada cuesta $10")