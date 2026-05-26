VELOCIDAD_MAX_REALISTA = 400

ACELERACION_MAX_REALISTA = 10000


def validar_valores_cinematicos(
    velocidad,
    aceleracion
):

    velocidad_valida = (
        velocidad <= VELOCIDAD_MAX_REALISTA
    )

    aceleracion_valida = (
        abs(aceleracion)
        <= ACELERACION_MAX_REALISTA
    )

    return {

        "velocidad_valida":
            velocidad_valida,

        "aceleracion_valida":
            aceleracion_valida,

        "valido":
            (
                velocidad_valida and
                aceleracion_valida
            )
    }