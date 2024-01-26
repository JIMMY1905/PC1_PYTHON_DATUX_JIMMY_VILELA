
    tiempo = input("Ingrese la hora en formato de 24 horas (por ejemplo, 08:30): ")
    horas, minutos = int(tiempo.split(':'))
    if 7 <= horas <= 8:
        print("Es hora de desayunar.")
    elif 12 <= horas <= 13:
        print("Es hora de almorzar.")
    elif 18 <= horas <= 19:
        print("Es hora de cenar.")
    else:
        pass