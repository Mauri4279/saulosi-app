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


def normalizar(
    valor,
    minimo,
    maximo
):

    if maximo - minimo == 0:
        return 0

    valor = max(min(valor, maximo), minimo)

    return (
        (valor - minimo)
        / (maximo - minimo)
    )


def calcular_score_comportamiento(
    velocidad,
    aceleracion,
    inmovil,
    proximidad,
    curvatura,
    entropia
):

    velocidad_norm = normalizar(
        velocidad,
        0,
        150
    )

    aceleracion_norm = normalizar(
        abs(aceleracion),
        0,
        3000
    )

    curvatura_norm = normalizar(
        curvatura,
        0,
        180
    )

    entropia_norm = normalizar(
        entropia,
        0,
        3
    )

    proximidad_norm = normalizar(
        len(proximidad),
        0,
        5
    )

    score = 0

    score += velocidad_norm * 30

    score += aceleracion_norm * 25

    score += curvatura_norm * 15

    score += entropia_norm * 20

    score += proximidad_norm * 10

    if inmovil:
        score -= 15

    score = max(score, 0)

    return round(score, 2)