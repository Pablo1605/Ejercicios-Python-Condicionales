respuesta = input("¿Deseas continuar? (s/n): ").lower()

if respuesta == "s":
    print("Continuando...")
elif respuesta == "n":
    print("Saliendo...")
else:
    print("Respuesta inválida")