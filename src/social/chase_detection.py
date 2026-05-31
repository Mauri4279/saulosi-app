import math

from collections import defaultdict

from src.feature_extraction.movement_metrics import (
    calcular_vector_movimiento,
    calcular_vector_hacia_objetivo
)


def producto_escalar(v1, v2):

    return (
        v1[0] * v2[0]
        +
        v1[1] * v2[1]
    )


def norma(v):

    return math.sqrt(
        v[0] ** 2
        +
        v[1] ** 2
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
    alineacion_minima=0.6,
    direccion_minima=0.7,
    frames_minimos=3
):

    eventos = []

    frames = defaultdict(list)

    for d in tracking_data:

        frames[
            d["frame"]
        ].append(d)

    trayectorias = defaultdict(list)

    # contador de persecuciones consecutivas
    persecuciones_activas = defaultdict(int)

    # máximo alcanzado por cada pareja
    max_duracion = defaultdict(int)

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

        parejas_validas_en_frame = set()

        for id_a in ids:

            for id_b in ids:

                if id_a == id_b:
                    continue

                historial_a = trayectorias[id_a]
                historial_b = trayectorias[id_b]

                if (
                    len(historial_a) < 2
                    or
                    len(historial_b) < 2
                ):
                    continue

                pos_a = posiciones[id_a]
                pos_b = posiciones[id_b]

                distancia = math.sqrt(
                    (pos_b[0] - pos_a[0]) ** 2
                    +
                    (pos_b[1] - pos_a[1]) ** 2
                )

                # filtro de distancia
                if distancia > distancia_maxima:
                    continue

                pos_a_anterior = historial_a[-2]
                pos_b_anterior = historial_b[-2]

                distancia_anterior = math.sqrt(
                    (
                        pos_b_anterior[0]
                        -
                        pos_a_anterior[0]
                    ) ** 2
                    +
                    (
                        pos_b_anterior[1]
                        -
                        pos_a_anterior[1]
                    ) ** 2
                )

                acercamiento = (
                    distancia_anterior
                    -
                    distancia
                )

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

                if (
                    vector_a is None
                    or
                    vector_b is None
                ):
                    continue

                if (
                    norma(vector_a) < 3
                    or
                    norma(vector_b) < 3
                ):
                    continue

                alineacion_movimiento = (
                    coseno_angulo(
                        vector_a,
                        vector_b
                    )
                )

                vector_hacia_objetivo = (
                    calcular_vector_hacia_objetivo(
                        pos_a,
                        pos_b
                    )
                )

                direccion_persecucion = (
                    coseno_angulo(
                        vector_a,
                        vector_hacia_objetivo
                    )
                )

                es_persecucion = (

                    alineacion_movimiento
                    >
                    alineacion_minima

                    and

                    direccion_persecucion
                    >
                    direccion_minima

                    and

                    acercamiento
                    >
                    2

                )

                if es_persecucion:

                    parejas_validas_en_frame.add(
                        (id_a, id_b)
                    )

                    persecuciones_activas[
                        (id_a, id_b)
                    ] += 1

                    max_duracion[
                        (id_a, id_b)
                    ] = max(

                        max_duracion[
                            (id_a, id_b)
                        ],

                        persecuciones_activas[
                            (id_a, id_b)
                        ]
                    )

                else:

                    persecuciones_activas[
                        (id_a, id_b)
                    ] = 0

        # resetear las parejas que no aparecieron
        for pareja in list(
            persecuciones_activas.keys()
        ):

            if pareja not in parejas_validas_en_frame:

                persecuciones_activas[
                    pareja
                ] = 0

    print("\n=== RESUMEN ===")

    for clave, duracion in max_duracion.items():

        print(
            clave,
            duracion
        )

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