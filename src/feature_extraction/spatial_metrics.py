from collections import deque

from src.feature_extraction.thresholds import (
    RADIO_INMOVILIDAD
)


def detectar_inmovilidad(historial):

    if len(historial) < 10:
        return False

    xs = [p[0] for p in historial]
    ys = [p[1] for p in historial]

    rango_x = max(xs) - min(xs)
    rango_y = max(ys) - min(ys)

    return (
        rango_x < RADIO_INMOVILIDAD and
        rango_y < RADIO_INMOVILIDAD
    )


def calcular_tiempo_superficie(cy, superficie_y):

    return cy < superficie_y