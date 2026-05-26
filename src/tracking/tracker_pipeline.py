import cv2
import numpy as np

from collections import defaultdict

from src.visualization.drawing import dibujar_texto_borde
from src.utils.paths import TRACKER_CONF

TARGET_W = 640
TARGET_H = 360

COLOR_TRAYECTORIA = (190, 232, 255)
OPACIDAD = 0.6


def ejecutar_tracking(video_path, output_video, model):

    tracking_data = []
    frame_number = 0

    track_history = defaultdict(list)
    peces_unicos_historico = set()

    cap = cv2.VideoCapture(str(video_path))

    if not cap.isOpened():
        raise ValueError(f"Error al abrir el video: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    out_video = cv2.VideoWriter(
        str(output_video),
        fourcc,
        fps,
        (TARGET_W, TARGET_H)
    )

    while True:

        frame_number += 1

        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.resize(frame, (TARGET_W, TARGET_H))

        annotated_frame = frame.copy()
        overlay = annotated_frame.copy()

        results = model.track(
            frame,
            persist=True,
            tracker=str(TRACKER_CONF),
            conf=0.15,
            iou=0.4,
            verbose=False
        )

        peces_en_pantalla = 0

        if results[0].boxes.id is not None:

            boxes = results[0].boxes.xyxy.cpu().numpy()
            track_ids = results[0].boxes.id.int().cpu().tolist()
            confs = results[0].boxes.conf.cpu().numpy()

            peces_en_pantalla = len(track_ids)

            for box, track_id, conf in zip(boxes, track_ids, confs):

                peces_unicos_historico.add(track_id)

                x1, y1, x2, y2 = map(int, box)

                cx = int((x1 + x2) / 2)
                cy = int((y1 + y2) / 2)

                track_history[track_id].append((cx, cy))

                tracking_data.append({
                    "frame": frame_number,
                    "track_id": track_id,
                    "cx": cx,
                    "cy": cy,
                    "conf": float(conf)
                    })

                if len(track_history[track_id]) > 90:
                    track_history[track_id].pop(0)

                puntos = np.hstack(
                    track_history[track_id]
                ).astype(np.int32).reshape((-1, 1, 2))

                cv2.polylines(
                    overlay,
                    [puntos],
                    isClosed=False,
                    color=COLOR_TRAYECTORIA,
                    thickness=2
                )

                cv2.rectangle(
                    overlay,
                    (x1, y1),
                    (x2, y2),
                    (175, 106, 64),
                    2
                )

                etiqueta = f"id:{track_id} Pez {conf:.2f}"

                dibujar_texto_borde(
                    overlay,
                    etiqueta,
                    (x1, y1 - 6),
                    escala=0.5,
                    color=(175, 106, 64),
                    grosor=1
                )

        cv2.addWeighted(
            overlay,
            OPACIDAD,
            annotated_frame,
            1 - OPACIDAD,
            0,
            annotated_frame
        )

        texto_pantalla = f"Peces actuales: {peces_en_pantalla}"

        texto_total = (
            f"Total historico (Unicos): "
            f"{len(peces_unicos_historico)}"
        )

        dibujar_texto_borde(
            annotated_frame,
            texto_pantalla,
            (15, 30),
            escala=0.6,
            color=(255, 255, 255),
            grosor=2
        )

        dibujar_texto_borde(
            annotated_frame,
            texto_total,
            (15, 60),
            escala=0.6,
            color=(181, 122, 64),
            grosor=2
        )

        out_video.write(annotated_frame)

        cv2.imshow(
            "Tracking y Metricas de Peces",
            annotated_frame
        )

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out_video.release()
    cv2.destroyAllWindows()
    
    print("\n===============================")
    print("✔ ANÁLISIS FINALIZADO")
    print(
        f"Peces únicos detectados: "
        f"{len(peces_unicos_historico)}"
    )
    print(f"Video exportado: {output_video}")
    print("===============================\n")

    return tracking_data
