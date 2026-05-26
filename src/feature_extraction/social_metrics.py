import math


def distancia_entre_peces(p1, p2):

    return math.sqrt(
        (p2[0] - p1[0]) ** 2 +
        (p2[1] - p1[1]) ** 2
    )


def detectar_proximidad(
    track_id,
    centroides,
    distancia_social
):

    relaciones = []

    ids = list(centroides.keys())

    for other_id in ids:

        if other_id == track_id:
            continue

        distancia = distancia_entre_peces(
            centroides[track_id],
            centroides[other_id]
        )

        if distancia < distancia_social:

            relaciones.append({
                "otro_pez": other_id,
                "distancia": distancia
            })

    return relaciones