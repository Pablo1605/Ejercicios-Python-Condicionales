n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
prom = (n1 + n2 + n3) / 3

if prom >= 6:
    print("Aprobado con promedio:", prom)
else:
    print("Reprobado con promedio:", prom)