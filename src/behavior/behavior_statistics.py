import numpy as np

from collections import defaultdict


def generar_behavior_statistics(
    metricas
):

    raw = defaultdict(
        lambda: {
            "velocidades": [],
            "aceleraciones": [],
            "entropias": [],
            "socialidad": [],
            "inmovilidad": 0,
            "superficie": 0,
            "movimientos_bruscos": 0,
            "frames": 0
        }
    )

    # =========================
    # ACUMULACION
    # =========================

    for m in metricas:

        track_id = m["track_id"]

        raw[track_id]["velocidades"].append(
            m["velocidad_normalizada"]
        )

        raw[track_id]["aceleraciones"].append(
            abs(
                m["aceleracion_normalizada"]
            )
        )

        raw[track_id]["entropias"].append(
            m["entropia"]
        )

        raw[track_id]["socialidad"].append(
            m["peces_cercanos"]
        )

        raw[track_id]["frames"] += 1

        if m["inmovil"]:

            raw[track_id]["inmovilidad"] += 1

        if m["movimiento_brusco"]:

            raw[track_id]["movimientos_bruscos"] += 1

        if m["tiempo_superficie"] > 0:

            raw[track_id]["superficie"] += 1

    # =========================
    # ESTADISTICAS
    # =========================

    salida = []

    for track_id, data in raw.items():

        frames = max(
            data["frames"],
            1
        )

        salida.append({

            "track_id":
                track_id,

            "frames":
                frames,

            "p95_velocidad":
                round(
                    np.percentile(
                        data["velocidades"],
                        95
                    ),
                    6
                ),

            "p95_aceleracion":
                round(
                    np.percentile(
                        data["aceleraciones"],
                        95
                    ),
                    6
                ),

            "ratio_inmovilidad":
                round(
                    data["inmovilidad"] / frames,
                    4
                ),

            "ratio_superficie":
                round(
                    data["superficie"] / frames,
                    4
                ),

            "ratio_movimientos_bruscos":
                round(
                    data[
                        "movimientos_bruscos"
                    ] / frames,
                    4
                ),

            "socialidad_media":
                round(
                    np.mean(
                        data["socialidad"]
                    ),
                    4
                ),

            "entropia_media":
                round(
                    np.mean(
                        data["entropias"]
                    ),
                    4
                )
        })

    return salida