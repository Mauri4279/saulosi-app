def validar_consistencia(metricas):

    inconsistencias = []

    for m in metricas:

        errores = []

        if (
            m["inmovil"] is True and
            m["velocidad"] > 30
        ):

            errores.append(
                "Inmovil con velocidad alta"
            )

        if (
            m["inmovil"] is True and
            m["movimiento_brusco"] is True
        ):

            errores.append(
                "Inmovil y movimiento brusco"
            )

        if (
            m["movimiento_brusco"] is True and
            abs(m["aceleracion"]) < 100
        ):

            errores.append(
                "Movimiento brusco inconsistente"
            )

        if errores:

            inconsistencias.append({

                "frame": m["frame"],

                "track_id": m["track_id"],

                "errores": errores
            })

    return inconsistencias