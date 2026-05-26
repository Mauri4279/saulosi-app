from collections import defaultdict

from src.feature_extraction.movement_metrics import (
    calcular_velocidad,
    calcular_aceleracion,
    detectar_cambio_brusco,
    calcular_curvatura
)

from src.feature_extraction.spatial_metrics import (
    detectar_inmovilidad,
    calcular_tiempo_superficie
)

from src.feature_extraction.social_metrics import (
    detectar_proximidad
)

from src.feature_extraction.behavior_score import (
    calcular_entropia,
    calcular_score_comportamiento
)

from src.feature_extraction.thresholds import (
    ACELERACION_BRUSCA,
    DISTANCIA_SOCIAL,
    SUPERFICIE_Y
)


def ejecutar_extraccion_features(
    tracking_data,
    fps
):

    historial_posiciones = defaultdict(list)

    historial_velocidad = defaultdict(list)

    tiempo_superficie = defaultdict(int)

    metricas = []

    for data in tracking_data:

        frame = data["frame"]

        track_id = data["track_id"]

        cx = data["cx"]
        cy = data["cy"]

        historial_posiciones[track_id].append(
            (cx, cy)
        )

        historial = historial_posiciones[track_id]

        velocidad = 0
        aceleracion = 0
        curvatura = 0

        if len(historial) >= 2:

            velocidad = calcular_velocidad(
                historial[-2],
                historial[-1],
                fps
            )

            historial_velocidad[track_id].append(
                velocidad
            )

        if len(historial_velocidad[track_id]) >= 2:

            aceleracion = calcular_aceleracion(
                historial_velocidad[track_id][-2],
                historial_velocidad[track_id][-1],
                fps
            )

        inmovil = detectar_inmovilidad(
            historial
        )

        movimiento_brusco = detectar_cambio_brusco(
            aceleracion,
            ACELERACION_BRUSCA
        )

        proximidad = detectar_proximidad(
            track_id,
            {
                track_id: (cx, cy)
            },
            DISTANCIA_SOCIAL
        )

        curvatura = calcular_curvatura(
            historial
        )

        if calcular_tiempo_superficie(
            cy,
            SUPERFICIE_Y
        ):
            tiempo_superficie[track_id] += 1

        entropia = calcular_entropia(
            historial_velocidad[track_id]
        )

        score = calcular_score_comportamiento(
            velocidad,
            aceleracion,
            inmovil,
            proximidad,
            curvatura,
            entropia
        )

        metricas.append({

            "frame": frame,

            "track_id": track_id,

            "velocidad": velocidad,

            "aceleracion": aceleracion,

            "inmovil": inmovil,

            "movimiento_brusco": movimiento_brusco,

            "curvatura": curvatura,

            "entropia": entropia,

            "score": score,

            "tiempo_superficie":
                tiempo_superficie[track_id]
        })

    return metricas