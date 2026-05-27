import numpy as np


def generar_estadisticas(metricas):

    scores = [
        m["score"]
        for m in metricas
    ]

    entropias = [
        m["entropia"]
        for m in metricas
    ]

    velocidades = [
        m["velocidad"]
        for m in metricas
    ]

    velocidades_norm = [
        m["velocidad_normalizada"]
        for m in metricas
    ]

    aceleraciones_norm = [
        m["aceleracion_normalizada"]
        for m in metricas
    ]

    stats = {

        "score_promedio":
            round(np.mean(scores), 2),

        "score_maximo":
            round(np.max(scores), 2),

        "entropia_promedio":
            round(np.mean(entropias), 2),

        "velocidad_promedio":
            round(np.mean(velocidades), 2),

        "velocidad_normalizada_promedio":
            round(np.mean(velocidades_norm), 4),

        "aceleracion_normalizada_promedio":
            round(np.mean(aceleraciones_norm), 4),

        "frames_analizados":
            len(metricas)
    }

    return stats