from collections import defaultdict
from collections import deque

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

from src.validation.filters.velocity_sanity_filter import (
    validar_valores_cinematicos
)

from src.validation.filters.temporal_continuity_filter import (
    validar_continuidad
)

from src.normalization.kinematic_normalizer import (
    normalizar_velocidad,
    normalizar_aceleracion
)

from src.normalization.video_metadata import (
    FRAME_DIAGONAL
)

from src.feature_extraction.social_metrics import (
    detectar_proximidad,
    actualizar_interacciones_sociales
)


def ejecutar_extraccion_features(
    tracking_data,
    fps
):

    historial_posiciones = defaultdict(list)

    historial_suavizado = defaultdict(
        lambda: deque(maxlen=5)
    )

    historial_velocidad = defaultdict(list)

    tiempo_superficie = defaultdict(int)

    posiciones_actuales = {}

    matriz_social = defaultdict(
        lambda: defaultdict(int)
    )

    metricas = []

    for data in tracking_data:

        frame = data["frame"]

        track_id = data["track_id"]

        cx = data["cx"]
        cy = data["cy"]

        # =========================
        # SMOOTHING DE CENTROIDES
        # =========================

        historial_suavizado[track_id].append(
            (cx, cy)
        )

        cx_smooth = int(sum(
            p[0]
            for p in historial_suavizado[track_id]
        ) / len(historial_suavizado[track_id]))

        cy_smooth = int(sum(
            p[1]
            for p in historial_suavizado[track_id]
        ) / len(historial_suavizado[track_id]))

        historial_posiciones[track_id].append(
            (cx_smooth, cy_smooth)
        )

        posiciones_actuales[track_id] = (
            cx_smooth,
            cy_smooth
        )

        historial = historial_posiciones[track_id]

        # =========================
        # VARIABLES INICIALES
        # =========================

        continuidad = {
            "continuidad_valida": True,
            "distancia_frame": 0
        }

        validacion_cinematica = {
            "velocidad_valida": True,
            "aceleracion_valida": True
        }

        velocidad = 0
        aceleracion = 0
        curvatura = 0

        velocidad_normalizada = 0
        aceleracion_normalizada = 0

        # =========================
        # VELOCIDAD
        # =========================

        if len(historial) >= 2:

            continuidad = validar_continuidad(
                historial[-2],
                historial[-1]
            )

            velocidad = calcular_velocidad(
                historial[-2],
                historial[-1],
                fps
            )

            historial_velocidad[track_id].append(
                velocidad
            )

            velocidad_normalizada = (
                normalizar_velocidad(
                    velocidad,
                    FRAME_DIAGONAL
                )
            )

        # =========================
        # ACELERACION
        # =========================

        if len(historial_velocidad[track_id]) >= 2:

            aceleracion = calcular_aceleracion(
                historial_velocidad[track_id][-2],
                historial_velocidad[track_id][-1],
                fps
            )

            aceleracion_normalizada = (
                normalizar_aceleracion(
                    aceleracion,
                    fps
                )
            )

            validacion_cinematica = (
                validar_valores_cinematicos(
                    velocidad,
                    aceleracion
                )
            )

        # =========================
        # MOVIMIENTO BRUSCO
        # =========================

        movimiento_brusco = detectar_cambio_brusco(
            aceleracion,
            ACELERACION_BRUSCA
        )

        # =========================
        # INMOVILIDAD
        # =========================

        inmovil = detectar_inmovilidad(
            historial,
            velocidad,
            movimiento_brusco
        )

        # =========================
        # PROXIMIDAD SOCIAL
        # =========================

        proximidad = detectar_proximidad(
            track_id,
            posiciones_actuales,
            DISTANCIA_SOCIAL
        )

        matriz_social = (
            actualizar_interacciones_sociales(
                track_id,
                proximidad,
                matriz_social
            )
        )

        # =========================
        # CURVATURA
        # =========================

        curvatura = calcular_curvatura(
            historial
        )

        # =========================
        # TIEMPO EN SUPERFICIE
        # =========================

        if calcular_tiempo_superficie(
            cy_smooth,
            SUPERFICIE_Y
        ):
            tiempo_superficie[track_id] += 1

        # =========================
        # ENTROPIA
        # =========================

        entropia = calcular_entropia(
            historial_velocidad[track_id]
        )

        # =========================
        # SCORE GENERAL
        # =========================

        score = calcular_score_comportamiento(
            velocidad,
            aceleracion,
            inmovil,
            proximidad,
            curvatura,
            entropia
        )

        # =========================
        # EXPORT METRICS
        # =========================

        metricas.append({

            "frame": frame,

            "track_id": track_id,

            "velocidad": velocidad,

            "aceleracion": aceleracion,

            "velocidad_normalizada":
                round(velocidad_normalizada, 6),

            "aceleracion_normalizada":
                round(aceleracion_normalizada, 6),

            "inmovil": inmovil,

            "movimiento_brusco": movimiento_brusco,

            "curvatura": round(curvatura, 4),

            "entropia": round(entropia, 4),

            "score": score,

            "tiempo_superficie":
                tiempo_superficie[track_id],

            "velocidad_valida":
                validacion_cinematica[
                    "velocidad_valida"
                ],

            "aceleracion_valida":
                validacion_cinematica[
                    "aceleracion_valida"
                ],

            "continuidad_valida":
                continuidad[
                    "continuidad_valida"
                ],

            "distancia_frame":
                continuidad[
                    "distancia_frame"
                ],

            "peces_cercanos":
                len(proximidad)

        })

    return {
        "metricas": metricas,
        "matriz_social": matriz_social
    }