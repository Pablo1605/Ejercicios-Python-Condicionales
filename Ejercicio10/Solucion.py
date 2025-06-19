precio = float(input("Precio del producto: "))
edad = int(input("Edad del comprador: "))

if edad < 18:
    descuento = 0.10
elif edad > 60:
    descuento = 0.20
else:
    descuento = 0

precio_final = precio * (1 - descuento)
print(f"Precio final: {precio_final:.2f}")