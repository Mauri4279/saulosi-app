from src.feature_extraction.thresholds import (
    RADIO_INMOVILIDAD,
    UMBRAL_INMOVILIDAD
)


def detectar_inmovilidad(
    historial,
    velocidad,
    movimiento_brusco
):

    if len(historial) < 10:
        return False

    xs = [p[0] for p in historial]
    ys = [p[1] for p in historial]

    rango_x = max(xs) - min(xs)
    rango_y = max(ys) - min(ys)

    inmovil_espacial = (
        rango_x < RADIO_INMOVILIDAD and
        rango_y < RADIO_INMOVILIDAD
    )

    if velocidad > UMBRAL_INMOVILIDAD:
        return False

    if movimiento_brusco:
        return False

    return inmovil_espacial


def calcular_tiempo_superficie(
    cy,
    superficie_y
):

    return cy < superficie_y