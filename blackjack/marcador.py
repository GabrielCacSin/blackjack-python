from blackjack import jugar_partida

marcador = {"victoria": 0, "derrota": 0, "empate": 0}

print("=== BLACKJACK CON MARCADOR ===")
while True:
    resultado = jugar_partida()
    marcador[resultado] += 1
    print(f"Victorias: {marcador['victoria']} | Derrotas: {marcador['derrota']} | Empates: {marcador['empate']}")
    if input("¿Otra partida? (s/n) ").strip().lower() != "s":
        break
print("¡Gracias por jugar!")