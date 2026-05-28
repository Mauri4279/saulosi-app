def clasificar_comportamiento(
    perfiles,
    quality_metrics
):

    quality_map = {

        q["track_id"]: q

        for q in quality_metrics
    }

    resultados = []

    for perfil in perfiles:

        track_id = perfil["track_id"]

        reliability = quality_map.get(
            track_id,
            {}
        ).get(
            "reliability_score",
            0
        )

        comportamiento = "normal"

        # ======================
        # FORRAJEO / EXPLORADOR
        # ======================

        if (

            perfil["velocidad_media"] > 0.02

            and

            perfil["curvatura_media"] > 10

            and

            perfil["entropia_media"] > 0.8

        ):

            comportamiento = (
                "forrajeo_explorador"
            )

        # ======================
        # LETARGO
        # ======================

        elif (

            perfil["tiempo_inmovil"]

            >

            perfil["frames_analizados"] * 0.20

            and

            perfil["velocidad_media"] < 0.015

        ):

            comportamiento = "letargo"

        # ======================
        # CARDUMEN
        # ======================

        elif (

            perfil["indice_social"] > 2

            and

            perfil["velocidad_media"] > 0.01

        ):

            comportamiento = (
                "afinidad_social"
            )

        # ======================
        # TERRITORIALIDAD
        # ======================

        elif (

            perfil["tiempo_superficie"]

            >

            perfil["frames_analizados"] * 0.60

            and

            perfil["indice_social"] < 1

        ):

            comportamiento = (
                "territorial"
            )

        # ======================
        # NADO CIRCULAR
        # ======================

        elif (

            perfil["curvatura_media"] > 20

            and

            perfil["velocidad_media"] < 0.04

        ):

            comportamiento = (
                "nado_circular"
            )

        resultados.append({

            "track_id":
                track_id,

            "behavior_class":
                comportamiento,

            "behavior_score":
                round(
                    perfil["score_general"],
                    2
                ),

            "confidence":
                round(
                    reliability / 100,
                    2
                )
        })

    return resultados