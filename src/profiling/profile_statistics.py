import numpy as np
from collections import defaultdict


def generar_perfiles(metricas):

    perfiles_raw = defaultdict(
        lambda: {
            "velocidades": [],
            "aceleraciones": [],
            "entropias": [],
            "scores": [],
            "curvaturas": [],
            "tiempo_inmovil": 0,
            "tiempo_superficie": 0,
            "frames": 0,
            "interacciones_sociales": 0
        }
    )

    # =========================
    # ACUMULACION DE METRICAS
    # =========================

    for m in metricas:

        track_id = m["track_id"]

        perfiles_raw[track_id][
            "velocidades"
        ].append(
            m["velocidad_normalizada"]
        )

        perfiles_raw[track_id][
            "aceleraciones"
        ].append(
            m["aceleracion_normalizada"]
        )

        perfiles_raw[track_id][
            "entropias"
        ].append(
            m["entropia"]
        )

        perfiles_raw[track_id][
            "scores"
        ].append(
            m["score"]
        )

        perfiles_raw[track_id][
            "curvaturas"
        ].append(
            m["curvatura"]
        )

        perfiles_raw[track_id][
            "interacciones_sociales"
        ] += m["peces_cercanos"]

        perfiles_raw[track_id][
            "frames"
        ] += 1

        if m["inmovil"]:

            perfiles_raw[track_id][
                "tiempo_inmovil"
            ] += 1

        perfiles_raw[track_id][
            "tiempo_superficie"
        ] = max(
            perfiles_raw[track_id][
                "tiempo_superficie"
            ],
            m["tiempo_superficie"]
        )

    # =========================
    # PERFIL FINAL
    # =========================

    perfiles_finales = []

    for track_id, data in perfiles_raw.items():

        frames = max(data["frames"], 1)

        indice_social = (
            data["interacciones_sociales"]
            / frames
        )

        perfil = {

            "track_id":
                track_id,

            "frames_analizados":
                frames,

            "velocidad_media":
                round(
                    np.mean(data["velocidades"]),
                    6
                ),

            "velocidad_maxima":
                round(
                    np.max(data["velocidades"]),
                    6
                ),

            "aceleracion_media":
                round(
                    np.mean(data["aceleraciones"]),
                    6
                ),

            "entropia_media":
                round(
                    np.mean(data["entropias"]),
                    4
                ),

            "curvatura_media":
                round(
                    np.mean(data["curvaturas"]),
                    4
                ),

            "indice_social":
                round(
                    indice_social,
                    4
                ),

            "tiempo_inmovil":
                data["tiempo_inmovil"],

            "tiempo_superficie":
                data["tiempo_superficie"],

            "score_general":
                round(
                    np.mean(data["scores"]),
                    2
                )
        }

        perfiles_finales.append(perfil)

    return perfiles_finales