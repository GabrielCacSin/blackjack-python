import random

PALOS = ["♠", "♥", "♦", "♣"]
VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def crear_baraja():
    baraja = [(v, p) for p in PALOS for v in VALORES]
    random.shuffle(baraja)
    return baraja


def puntos(mano):
    total = 0
    ases = 0
    for valor, _ in mano:
        if valor in ("J", "Q", "K"):
            total += 10
        elif valor == "A":
            total += 11
            ases += 1
        else:
            total += int(valor)
    while total > 21 and ases:
        total -= 10
        ases -= 1
    return total


def es_blackjack(mano):
    """Blackjack natural: 21 puntos con las dos primeras cartas."""
    return len(mano) == 2 and puntos(mano) == 21


def mostrar(nombre, mano, ocultar=False):
    if ocultar:
        print(f"{nombre}: {mano[0][0]}{mano[0][1]} ??")
    else:
        cartas = " ".join(v + p for v, p in mano)
        print(f"{nombre}: {cartas}  ({puntos(mano)} puntos)")


def jugar_partida():
    baraja = crear_baraja()
    jugador = [baraja.pop(), baraja.pop()]
    crupier = [baraja.pop(), baraja.pop()]

    # Comprobación de Blackjack natural antes de jugar
    bj_jugador, bj_crupier = es_blackjack(jugador), es_blackjack(crupier)
    if bj_jugador or bj_crupier:
        mostrar("Crupier", crupier)
        mostrar("Tú", jugador)
        if bj_jugador and bj_crupier:
            print("Los dos tenéis Blackjack. Empate.")
            return "empate"
        if bj_jugador:
            print("¡Blackjack! Ganas.")
            return "victoria"
        print("El crupier tiene Blackjack. Pierdes.")
        return "derrota"

    # Turno del jugador
    while True:
        mostrar("Crupier", crupier, ocultar=True)
        mostrar("Tú", jugador)
        if puntos(jugador) > 21:
            print("Te has pasado. Pierdes.")
            return "derrota"
        opcion = input("¿Pedir carta (p) o plantarse (s)? ").strip().lower()
        if opcion == "p":
            jugador.append(baraja.pop())
        elif opcion == "s":
            break

    # Turno del crupier: pide hasta tener 17 o más
    while puntos(crupier) < 17:
        crupier.append(baraja.pop())

    print()
    mostrar("Crupier", crupier)
    mostrar("Tú", jugador)

    pj, pc = puntos(jugador), puntos(crupier)
    if pc > 21 or pj > pc:
        print("¡Ganas!")
        return "victoria"
    if pj < pc:
        print("Gana el crupier.")
        return "derrota"
    print("Empate.")
    return "empate"


if __name__ == "__main__":
    print("=== BLACKJACK ===")
    jugar_partida()
