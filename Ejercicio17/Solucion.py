edad = int(input("Edad: "))
tiene_dni = input("¿Tiene DNI? (s/n): ").lower()

if edad >= 18 and tiene_dni == "s":
    print("Puede votar")
else:
    print("No puede votar")