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

    stats = {

        "score_promedio":
            round(np.mean(scores), 2),

        "score_maximo":
            round(np.max(scores), 2),

        "entropia_promedio":
            round(np.mean(entropias), 2),

        "velocidad_promedio":
            round(np.mean(velocidades), 2),

        "frames_analizados":
            len(metricas)
    }

    return stats