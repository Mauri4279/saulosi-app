import math
import numpy as np


def calcular_distancia(p1, p2):

    return math.sqrt(
        (p2[0] - p1[0]) ** 2 +
        (p2[1] - p1[1]) ** 2
    )


def calcular_velocidad(p1, p2, fps):

    distancia = calcular_distancia(p1, p2)

    return distancia * fps


def calcular_aceleracion(v1, v2, fps):

    return (v2 - v1) * fps


def detectar_cambio_brusco(aceleracion, umbral):

    return abs(aceleracion) > umbral


def calcular_curvatura(historial):

    if len(historial) < 3:
        return 0

    p1 = np.array(historial[-3])
    p2 = np.array(historial[-2])
    p3 = np.array(historial[-1])

    v1 = p2 - p1
    v2 = p3 - p2

    norm1 = np.linalg.norm(v1)
    norm2 = np.linalg.norm(v2)

    if norm1 == 0 or norm2 == 0:
        return 0

    cos_theta = np.dot(v1, v2) / (norm1 * norm2)

    cos_theta = np.clip(cos_theta, -1.0, 1.0)

    angulo = np.arccos(cos_theta)

    return np.degrees(angulo)

def calcular_desplazamiento_neto(historial):

    if len(historial) < 2:
        return 0

    return calcular_distancia(
        historial[0],
        historial[-1]
    )


def calcular_distancia_total(historial):

    if len(historial) < 2:
        return 0

    distancia_total = 0

    for i in range(1, len(historial)):

        distancia_total += calcular_distancia(
            historial[i - 1],
            historial[i]
        )

    return distancia_total


def calcular_ratio_exploracion(historial):

    distancia_total = (
        calcular_distancia_total(
            historial
        )
    )

    if distancia_total == 0:
        return 0

    desplazamiento_neto = (
        calcular_desplazamiento_neto(
            historial
        )
    )

    return (
        desplazamiento_neto
        /
        distancia_total
    )