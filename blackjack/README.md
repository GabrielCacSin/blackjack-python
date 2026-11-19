# Blackjack en Python

Juego de Blackjack por consola hecho para practicar Git y GitHub.

## Integrantes

- Gabriel Cáceres Sinclair (propietario del repositorio)
- Roberto Aguilar Rivera (colaborador)

## Cómo ejecutarlo

Hace falta Python 3. Desde la carpeta `blackjack/`:

```
python blackjack.py     # una sola partida
python marcador.py      # varias partidas seguidas con marcador
```

Durante la partida:

- `p` = pedir carta
- `s` = plantarse

## Funcionamiento

1. Se baraja una baraja de 52 cartas y se reparten dos al jugador y dos al crupier
   (la segunda del crupier queda oculta).
2. Si alguien tiene Blackjack (21 con las dos primeras cartas) la partida termina en ese momento.
3. El jugador pide cartas o se planta. Si pasa de 21, pierde.
4. El crupier pide cartas hasta llegar a 17 o más.
5. Gana quien tenga más puntos sin pasarse de 21.

El As vale 11, salvo que eso haga pasarse de 21; entonces vale 1. J, Q y K valen 10.

## Organización de los archivos

```
blackjack/
├── .gitignore     archivos que Git no debe seguir (__pycache__)
├── README.md      este documento
├── blackjack.py   lógica del juego: baraja, puntos, Blackjack y partida (Gabriel)
└── marcador.py    varias partidas seguidas con marcador (Roberto)
```

## Funcionalidades

- Baraja de 52 cartas barajada en cada partida.
- Cálculo de puntos con el valor flexible del As.
- Detección del Blackjack natural.
- Turno del jugador con validación de la opción escrita.
- Turno automático del crupier (se planta con 17).
- Resultado de la partida: victoria, derrota o empate.
- Marcador de victorias, derrotas y empates en varias partidas.
