def clasificar_comportamiento(
    perfiles,
    quality_metrics
):

    quality_map = {

        q["track_id"]: q

        for q in quality_metrics
    }

    resultados = []

    MIN_FRAMES_VALIDOS = 60

    for perfil in perfiles:

        track_id = perfil["track_id"]

        # ======================
        # EVIDENCIA INSUFICIENTE
        # ======================

        if perfil["frames_analizados"] < MIN_FRAMES_VALIDOS:

            resultados.append({

                "track_id":
                    track_id,

                "behavior_class":
                    "insuficiente_evidencia",

                "behavior_score":
                    round(
                        perfil["score_general"],
                        2
                    ),

                "confidence": 0.0
            })

            continue

        reliability = quality_map.get(
            track_id,
            {}
        ).get(
            "reliability_score",
            0
        )

        comportamiento = "normal"

        # ======================
        # LETARGO
        # ======================

        if (

            perfil["tiempo_inmovil"]

            >

            perfil["frames_analizados"] * 0.20

            and

            perfil["velocidad_media"] < 0.015

        ):

            comportamiento = "letargo"

        # ======================
        # TERRITORIALIDAD
        # ======================

        elif (

            perfil["tiempo_superficie"]

            >

            perfil["frames_analizados"] * 0.60

            and

            perfil["indice_social"] < 1

            and

            perfil["ratio_exploracion"] < 0.20

        ):

            comportamiento = (
                "territorial"
            )

        # ======================
        # AFINIDAD SOCIAL
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
        # NADO CIRCULAR
        # ======================

        elif (

            perfil["curvatura_media"] > 20

            and

            perfil["ratio_exploracion"] < 0.20

        ):

            comportamiento = (
                "nado_circular"
            )

        # ======================
        # FORRAJEO / EXPLORADOR
        # ======================

        elif (

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
        # EXPORT
        # ======================

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