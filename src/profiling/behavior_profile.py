from collections import defaultdict
import numpy as np


def generar_perfiles_comportamiento(
    metricas
):

    perfiles = defaultdict(list)

    # =========================
    # AGRUPAR POR TRACK_ID
    # =========================

    for metrica in metricas:

        track_id = metrica["track_id"]

        perfiles[track_id].append(
            metrica
        )

    perfiles_finales = []

    # =========================
    # GENERAR PERFIL
    # =========================

    for track_id, datos in perfiles.items():

        velocidades = [
            d["velocidad"]
            for d in datos
        ]

        aceleraciones = [
            abs(d["aceleracion"])
            for d in datos
        ]

        entropias = [
            d["entropia"]
            for d in datos
        ]

        scores = [
            d["score"]
            for d in datos
        ]

        curvaturas = [
            d["curvatura"]
            for d in datos
        ]

        proximidades = [
            d["peces_cercanos"]
            for d in datos
        ]

        inmovil_frames = sum(
            1
            for d in datos
            if d["inmovil"]
        )

        tiempo_superficie = max(
            d["tiempo_superficie"]
            for d in datos
        )

        perfil = {

            "track_id":
                track_id,

            "frames_detectado":
                len(datos),

            "velocidad_media":
                round(np.mean(velocidades), 2),

            "velocidad_maxima":
                round(np.max(velocidades), 2),

            "aceleracion_media":
                round(np.mean(aceleraciones), 2),

            "entropia_media":
                round(np.mean(entropias), 4),

            "curvatura_media":
                round(np.mean(curvaturas), 2),

            "indice_social":
                round(np.mean(proximidades), 2),

            "tiempo_inmovil":
                inmovil_frames,

            "tiempo_superficie":
                tiempo_superficie,

            "score_general":
                round(np.mean(scores), 2)
        }

        perfiles_finales.append(
            perfil
        )

    return perfiles_finales