a = float(input("Número 1: "))
b = float(input("Número 2: "))
op = input("Operación (+, -, *, /): ")

if op == '+':
    print("Resultado:", a + b)
elif op == '-':
    print("Resultado:", a - b)
elif op == '*':
    print("Resultado:", a * b)
elif op == '/':
    if b != 0:
        print("Resultado:", a / b)
    else:
        print("No se puede dividir por cero")
else:
    print("Operación inválida")