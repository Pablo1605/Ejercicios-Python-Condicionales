pin_correcto = "1234"
saldo = 10000

pin = input("Ingresa tu PIN: ")
if pin == pin_correcto:
    monto = float(input("Monto a retirar: "))
    if 0 < monto <= saldo:
        saldo -= monto
        print(f"Retiro exitoso. Saldo restante: {saldo}")
    else:
        print("Monto inválido o insuficiente")
else:
    print("PIN incorrecto")