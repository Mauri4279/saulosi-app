import math

from collections import defaultdict

from src.feature_extraction.movement_metrics import (
    calcular_vector_movimiento,
    calcular_vector_hacia_objetivo,
    calcular_velocidad_historial,
    calcular_aceleracion,
    calcular_curvatura
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


def detectar_agresiones(
    tracking_data,
    fps,
    distancia_critica=40,
    acercamiento_minimo=10,
    aceleracion_minima=500,
    direccion_minima=0.7
):

    eventos = []

    candidatos = []

    agresiones_activas = defaultdict(int)

    max_duracion = defaultdict(int)

    evidencias = {}

    frames = defaultdict(list)

    for d in tracking_data:

        frames[
            d["frame"]
        ].append(d)

    trayectorias = defaultdict(list)

    for frame_id in sorted(frames.keys()):

        parejas_validas_en_frame = set()

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

        ids = list(
            posiciones.keys()
        )

        for id_a in ids:

            for id_b in ids:

                if id_a == id_b:
                    continue

                historial_a = trayectorias[id_a]
                historial_b = trayectorias[id_b]

                if (
                    len(historial_a) < 6
                    or
                    len(historial_b) < 6
                ):
                    continue

                pos_a = posiciones[id_a]
                pos_b = posiciones[id_b]

                distancia = math.sqrt(
                    (pos_b[0] - pos_a[0]) ** 2
                    +
                    (pos_b[1] - pos_a[1]) ** 2
                )

                pos_a_prev = historial_a[-2]
                pos_b_prev = historial_b[-2]

                distancia_prev = math.sqrt(
                    (pos_b_prev[0] - pos_a_prev[0]) ** 2
                    +
                    (pos_b_prev[1] - pos_a_prev[1]) ** 2
                )

                acercamiento = (
                    distancia_prev
                    -
                    distancia
                )

                vector_a = (
                    calcular_vector_movimiento(
                        historial_a
                    )
                )

                if vector_a is None:
                    continue

                if norma(vector_a) < 3:
                    continue

                vector_hacia_objetivo = (
                    calcular_vector_hacia_objetivo(
                        pos_a,
                        pos_b
                    )
                )

                direccion_ataque = (
                    coseno_angulo(
                        vector_a,
                        vector_hacia_objetivo
                    )
                )

                velocidad_anterior = (
                    calcular_velocidad_historial(
                        historial_a[:-1],
                        fps
                    )
                )

                velocidad_actual = (
                    calcular_velocidad_historial(
                        historial_a,
                        fps
                    )
                )

                if (
                    velocidad_anterior is None
                    or
                    velocidad_actual is None
                ):
                    continue

                aceleracion = (
                    calcular_aceleracion(
                        velocidad_anterior,
                        velocidad_actual,
                        fps
                    )
                )

                curvatura_victima = (
                    calcular_curvatura(
                        historial_b
                    )
                )

                curvatura_victima = float(
                    curvatura_victima
                )

                es_agresion = (

                    distancia
                    <
                    distancia_critica

                    and

                    acercamiento
                    >
                    acercamiento_minimo

                    and

                    aceleracion
                    >
                    aceleracion_minima

                    and

                    direccion_ataque
                    >
                    direccion_minima

                )

                candidatos.append({

                    "frame":
                        int(frame_id),

                    "agresor":
                        int(id_a),

                    "victima":
                        int(id_b),

                    "distancia":
                        float(distancia),

                    "acercamiento":
                        float(acercamiento),

                    "aceleracion":
                        float(aceleracion),

                    "direccion":
                        float(direccion_ataque),

                    "curvatura":
                        float(curvatura_victima)
                })

                if es_agresion:

                    print(
                        f"AGRESION DETECTADA | "
                        f"Frame={frame_id} "
                        f"A={id_a} "
                        f"V={id_b}"
                    )

                    pareja = (
                        id_a,
                        id_b
                    )

                    parejas_validas_en_frame.add(
                        pareja
                    )

                    agresiones_activas[
                        pareja
                    ] += 1

                    max_duracion[
                        pareja
                    ] = max(

                        max_duracion[
                            pareja
                        ],

                        agresiones_activas[
                            pareja
                        ]
                    )

                    if (

                        pareja not in evidencias

                        or

                        aceleracion >

                        evidencias[
                            pareja
                        ]["aceleracion"]

                    ):

                        evidencias[
                            pareja
                        ] = {

                            "agresor":
                                int(id_a),

                            "victima":
                                int(id_b),

                            "frame":
                                int(frame_id),

                            "distancia":
                                round(
                                    float(distancia),
                                    2
                                ),

                            "aceleracion":
                                round(
                                    float(aceleracion),
                                    2
                                ),

                            "acercamiento":
                                round(
                                    float(acercamiento),
                                    2
                                ),

                            "curvatura_victima":
                                round(
                                    float(curvatura_victima),
                                    2
                                ),

                            "evasiva":
                                bool(
                                    curvatura_victima > 60
                                )
                        }

        for pareja in list(
            agresiones_activas.keys()
        ):

            if pareja not in parejas_validas_en_frame:

                agresiones_activas[
                    pareja
                ] = 0

    for pareja, duracion in max_duracion.items():

        if duracion < 1:
            continue

        eventos.append(
            evidencias[pareja]
        )

    print(
        f"\nAGRESIONES EXPORTADAS: "
        f"{len(eventos)}"
    )

    print(
        "\n=== TOP CANDIDATOS AGRESION ==="
    )

    top_candidatos = sorted(

        candidatos,

        key=lambda x: (

            x["direccion"]
            *
            x["aceleracion"]
            *
            max(
                x["acercamiento"],
                0
            )

        ),

        reverse=True
    )

    for candidato in top_candidatos[:20]:

        print(candidato)

    return eventos