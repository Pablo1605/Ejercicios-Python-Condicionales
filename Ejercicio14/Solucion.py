monto = float(input("Monto de compra: "))
iva = monto * 0.21

if monto > 1000:
    total = monto + iva
else:
    total = monto
    
print(f"Total a pagar: {total:.2f}")