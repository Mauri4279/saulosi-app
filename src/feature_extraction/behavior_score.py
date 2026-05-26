import numpy as np
from scipy.stats import entropy


def calcular_entropia(velocidades):

    if len(velocidades) < 5:
        return 0

    hist, _ = np.histogram(
        velocidades,
        bins=10
    )

    return entropy(hist)


def calcular_score_comportamiento(
    velocidad,
    aceleracion,
    inmovil,
    proximidad,
    curvatura,
    entropia
):

    score = 0

    score += velocidad * 0.2

    score += abs(aceleracion) * 0.15

    score += curvatura * 0.15

    score += entropia * 10

    score += len(proximidad) * 5

    if inmovil:
        score -= 20

    return round(score, 2)