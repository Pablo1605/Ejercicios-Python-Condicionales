j1 = input("Jugador 1 (piedra/papel/tijera): ").lower()
j2 = input("Jugador 2 (piedra/papel/tijera): ").lower()

if j1 == j2:
    print("Empate")
elif (j1 == "piedra" and j2 == "tijera") or \
     (j1 == "papel" and j2 == "piedra") or \
     (j1 == "tijera" and j2 == "papel"):
    print("Jugador 1 gana")
else:
    print("Jugador 2 gana")