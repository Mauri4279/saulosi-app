from collections import defaultdict


def detectar_proximidades_sociales(
    tracking_data,
    distancia_umbral=120,
    frames_minimos=10
):

    eventos = []

    historial = defaultdict(list)

    # =========================
    # AGRUPAR POR FRAME
    # =========================

    frames = defaultdict(list)

    for d in tracking_data:

        frames[d["frame"]].append(d)

    persecuciones_activas = {}

    # =========================
    # RECORRER VIDEO
    # =========================

    for frame_id in sorted(frames.keys()):

        detecciones = frames[frame_id]

        for pez_a in detecciones:

            for pez_b in detecciones:

                if pez_a["track_id"] == pez_b["track_id"]:
                    continue

                dx = (
                    pez_b["cx"]
                    - pez_a["cx"]
                )

                dy = (
                    pez_b["cy"]
                    - pez_a["cy"]
                )

                distancia = (
                    dx**2 + dy**2
                ) ** 0.5

                if distancia > distancia_umbral:
                    continue

                clave = (
                    pez_a["track_id"],
                    pez_b["track_id"]
                )

                persecuciones_activas[
                    clave
                ] = (
                    persecuciones_activas.get(
                        clave,
                        0
                    )
                    + 1
                )

    # =========================
    # FILTRADO FINAL
    # =========================

    for clave, duracion in (
        persecuciones_activas.items()
    ):

        if duracion >= frames_minimos:

            eventos.append({

                "pez_a":
                    clave[0],

                "pez_b":
                    clave[1],

                "frames_juntos":
                    duracion
            })

    return eventos