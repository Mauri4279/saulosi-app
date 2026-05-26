import math


DISTANCIA_MAX_FRAME = 120


def validar_continuidad(
    posicion_anterior,
    posicion_actual
):

    x1, y1 = posicion_anterior

    x2, y2 = posicion_actual

    distancia = math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2
    )

    continuidad_valida = (
        distancia <= DISTANCIA_MAX_FRAME
    )

    return {

        "distancia_frame":
            round(distancia, 2),

        "continuidad_valida":
            continuidad_valida
    }