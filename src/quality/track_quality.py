from collections import defaultdict

import numpy as np


def calcular_reliability_score(
    duracion_frames,
    confianza_media,
    distancia_promedio
):
    """
    Score de confiabilidad del track.

    Componentes:

    - Duración del track (40%)
    - Confianza promedio YOLO (40%)
    - Estabilidad espacial (20%)

    Resultado:
        0 - 100
    """

    score = 0

    # =========================
    # DURACION
    # =========================

    score += min(
        duracion_frames / 600,
        1
    ) * 40

    # =========================
    # CONFIANZA YOLO
    # =========================

    score += (
        confianza_media
    ) * 40

    # =========================
    # ESTABILIDAD ESPACIAL
    # =========================

    score += max(
        0,
        (
            1
            - distancia_promedio / 50
        )
    ) * 20

    # =========================
    # PENALIZACION TRACKS CORTOS
    # =========================

    if duracion_frames < 10:
        score *= 0.25

    elif duracion_frames < 30:
        score *= 0.50

    elif duracion_frames < 60:
        score *= 0.75

    return round(score, 2)


def generar_quality_metrics(
    tracking_data
):
    """
    Genera métricas de calidad para cada track.

    Input:
        tracking_data

    Output:
        [
            {
                track_id,
                duracion_frames,
                confianza_media,
                confianza_minima,
                confianza_maxima,
                distancia_promedio,
                distancia_maxima,
                reliability_score
            }
        ]
    """

    tracks = defaultdict(list)

    # =========================
    # AGRUPAR POR TRACK_ID
    # =========================

    for registro in tracking_data:

        track_id = registro["track_id"]

        tracks[
            track_id
        ].append(
            registro
        )

    quality_metrics = []

    # =========================
    # ANALISIS POR TRACK
    # =========================

    for track_id, registros in tracks.items():

        registros = sorted(
            registros,
            key=lambda x: x["frame"]
        )

        duracion_frames = len(
            registros
        )

        confs = [

            r["conf"]

            for r in registros
        ]

        confianza_media = float(
            np.mean(confs)
        )

        confianza_minima = float(
            np.min(confs)
        )

        confianza_maxima = float(
            np.max(confs)
        )

        # =========================
        # DISTANCIAS ENTRE FRAMES
        # =========================

        distancias = []

        for i in range(
            1,
            len(registros)
        ):

            x1 = registros[
                i - 1
            ]["cx"]

            y1 = registros[
                i - 1
            ]["cy"]

            x2 = registros[
                i
            ]["cx"]

            y2 = registros[
                i
            ]["cy"]

            distancia = np.sqrt(
                (x2 - x1) ** 2 +
                (y2 - y1) ** 2
            )

            distancias.append(
                distancia
            )

        distancia_promedio = (
            float(np.mean(distancias))
            if len(distancias) > 0
            else 0
        )

        distancia_maxima = (
            float(np.max(distancias))
            if len(distancias) > 0
            else 0
        )

        # =========================
        # SCORE FINAL
        # =========================

        reliability_score = (
            calcular_reliability_score(
                duracion_frames,
                confianza_media,
                distancia_promedio
            )
        )

        # =========================
        # EXPORT
        # =========================

        quality_metrics.append({

            "track_id":
                track_id,

            "duracion_frames":
                duracion_frames,

            "confianza_media":
                round(
                    confianza_media,
                    4
                ),

            "confianza_minima":
                round(
                    confianza_minima,
                    4
                ),

            "confianza_maxima":
                round(
                    confianza_maxima,
                    4
                ),

            "distancia_promedio":
                round(
                    distancia_promedio,
                    2
                ),

            "distancia_maxima":
                round(
                    distancia_maxima,
                    2
                ),

            "reliability_score":
                reliability_score
        })

    quality_metrics = sorted(
        quality_metrics,
        key=lambda x: x[
            "reliability_score"
        ],
        reverse=True
    )

    return quality_metrics