import numpy as np
from collections import defaultdict

from src.feature_extraction.movement_metrics import (
    calcular_desplazamiento_neto,
    calcular_ratio_exploracion
)


def generar_perfiles(metricas, tracking_data, matriz_social):

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
            "interacciones_sociales": 0,
            "movimientos_bruscos": 0,
            "posiciones": []
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

    trayectorias = defaultdict(list)

    for registro in tracking_data:

        trayectorias[
            registro["track_id"]
        ].append(

            (
                registro["cx"],
                registro["cy"]
            )

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

        historial = trayectorias.get(
            track_id,
            []
        )

        desplazamiento_neto = (
            calcular_desplazamiento_neto(
                historial
            )
        )

        ratio_exploracion = (
            calcular_ratio_exploracion(
                historial
            )
        )

        relaciones = matriz_social.get(
            track_id,
            {}
        )

        companero_preferido = None

        persistencia_social = 0

        if len(relaciones) > 0:

            companero_preferido = max(
                relaciones,
                key=relaciones.get
            )

            total_interacciones = sum(
                relaciones.values()
            )

            persistencia_social = (
                relaciones[
                    companero_preferido
                ]
                /
                total_interacciones
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

            "desplazamiento_neto":
                round(
                    desplazamiento_neto,
                    4
                ),

            "ratio_exploracion":
                round(
                    ratio_exploracion,
                    4
                ),

            "score_general":
                round(
                    np.mean(data["scores"]),
                    2
                ),

            "companero_preferido":
                companero_preferido,

            "persistencia_social":
                round(
                    persistencia_social,
                    4
                )

        }

        perfiles_finales.append(perfil)

    return perfiles_finales