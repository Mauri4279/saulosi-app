import math


def calcular_diagonal_frame(
    width,
    height
):

    return math.sqrt(
        width ** 2 +
        height ** 2
    )


def normalizar_velocidad(
    velocidad,
    diagonal_frame
):

    if diagonal_frame == 0:
        return 0

    return velocidad / diagonal_frame


def normalizar_aceleracion(
    aceleracion,
    fps
):

    if fps == 0:
        return 0

    return aceleracion / fps