import math

from collections import defaultdict

from src.feature_extraction.movement_metrics import (
    calcular_vector_movimiento
)


def producto_escalar(v1, v2):

    return (
        v1[0] * v2[0]
        +
        v1[1] * v2[1]
    )


def norma(v):

    return math.sqrt(
        v[0]**2
        +
        v[1]**2
    )


def coseno_angulo(v1, v2):

    n1 = norma(v1)
    n2 = norma(v2)

    if n1 == 0 or n2 == 0:
        return 0

    return (
        producto_escalar(v1, v2)
        /
        (n1 * n2)
    )


def detectar_persecuciones(
    tracking_data,
    distancia_maxima=120,
    alineacion_minima=0.8,
    frames_minimos=20
):

    eventos = []

    frames = defaultdict(list)

    for d in tracking_data:

        frames[
            d["frame"]
        ].append(d)

    trayectorias = defaultdict(list)

    persecuciones = defaultdict(int)

    for frame_id in sorted(frames.keys()):

        detecciones = frames[frame_id]

        posiciones = {}

        for pez in detecciones:

            track_id = pez["track_id"]

            posiciones[track_id] = (
                pez["cx"],
                pez["cy"]
            )

            trayectorias[
                track_id
            ].append(
                (
                    pez["cx"],
                    pez["cy"]
                )
            )

        ids = list(posiciones.keys())

        for id_a in ids:

            for id_b in ids:

                if id_a == id_b:
                    continue

                pos_a = posiciones[id_a]
                pos_b = posiciones[id_b]

                dx = pos_b[0] - pos_a[0]
                dy = pos_b[1] - pos_a[1]

                distancia = math.sqrt(
                    dx**2 + dy**2
                )

                if distancia > distancia_maxima:
                    continue

                historial_a = trayectorias[id_a]
                historial_b = trayectorias[id_b]

                if (
                    len(historial_a) < 2
                    or
                    len(historial_b) < 2
                ):
                    continue

                vector_a = (
                    calcular_vector_movimiento(
                        historial_a
                    )
                )

                vector_b = (
                    calcular_vector_movimiento(
                        historial_b
                    )
                )

                alineacion = coseno_angulo(
                    vector_a,
                    vector_b
                )

                if alineacion > alineacion_minima:

                    persecuciones[
                        (id_a, id_b)
                    ] += 1

    for clave, duracion in persecuciones.items():

        if duracion >= frames_minimos:

            eventos.append({

                "perseguidor":
                    clave[0],

                "perseguido":
                    clave[1],

                "duracion":
                    duracion
            })

    return eventos