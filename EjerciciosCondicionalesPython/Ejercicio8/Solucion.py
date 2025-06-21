n = int(input("Ingresa un número: "))

if 0 <= n <= 10:
    print("Está entre 0 y 10")
elif 11 <= n <= 20:
    print("Está entre 11 y 20")
elif 21 <= n <= 30:
    print("Está entre 21 y 30")
else:
    print("Fuera de rango")