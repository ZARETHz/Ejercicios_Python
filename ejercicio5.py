partidas = [
    ("Alex", "Bosque", 120),
    ("Luis", "Desierto", 90),
    ("Alex", "Bosque", 150),
    ("Ana", "Ciudad", 200),
    ("Luis", "Bosque", 110)
]

puntos_por_jugador = {}

for partida in partidas:
    jugador = partida[0]
    puntos = partida[2]

    if jugador in puntos_por_jugador:
        puntos_por_jugador[jugador] += puntos
    else:
        puntos_por_jugador[jugador] = puntos

print(puntos_por_jugador)

mapas_jugados = set()

for partida in partidas:
    mapas_jugados.add(partida[1])

print(mapas_jugados)

partidas_por_jugador = {}

for partida in partidas:
    jugador = partida[0]
    puntos = partida[2]

    if jugador in partidas_por_jugador:
        partidas_por_jugador[jugador].append(puntos)
    else:
        partidas_por_jugador[jugador] = [puntos]

for jugador in partidas_por_jugador:
    promedio = sum(partidas_por_jugador[jugador]) / len(partidas_por_jugador[jugador])
    print("Promedio de", jugador, ":", promedio)

puntos_por_mapa = {}

for partida in partidas:
    mapa = partida[1]
    puntos = partida[2]

    if mapa in puntos_por_mapa:
        puntos_por_mapa[mapa] += puntos
    else:
        puntos_por_mapa[mapa] = puntos
print(puntos_por_mapa)

max_puntos = 0
mejor_mapa = ""

for mapa in puntos_por_mapa:
    if puntos_por_mapa[mapa] > max_puntos:
        max_puntos = puntos_por_mapa[mapa]
        mejor_mapa = mapa

print("Mapa con más puntos:", mejor_mapa)
