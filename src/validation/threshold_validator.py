import numpy as np


def analizar_thresholds(metricas):

    velocidades = [
        m["velocidad"]
        for m in metricas
    ]

    aceleraciones = [
        abs(m["aceleracion"])
        for m in metricas
    ]

    analisis = {

        "velocidad_media":
            round(np.mean(velocidades), 2),

        "velocidad_maxima":
            round(np.max(velocidades), 2),

        "aceleracion_media":
            round(np.mean(aceleraciones), 2),

        "aceleracion_maxima":
            round(np.max(aceleraciones), 2),

        "percentil_95_aceleracion":
            round(np.percentile(
                aceleraciones,
                95
            ), 2)
    }

    return analisis