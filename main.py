from pathlib import Path

from src.detection.detector import cargar_modelo

from src.tracking.tracker_pipeline import (
    ejecutar_tracking
)

from src.feature_extraction.feature_pipeline import (
    ejecutar_extraccion_features
)

from src.utils.paths import (
    RAW_VIDEOS_DIR,
    PROCESSED_DIR
)

from src.feature_extraction.export_pipeline import (
    exportar_resultados
)

VIDEO_NAME = (
    "vid_014_part_01_acuario_domestico_peces_en_el_cristal.mp4"
)


def main():

    video_path = RAW_VIDEOS_DIR / VIDEO_NAME

    nombre_base = Path(VIDEO_NAME).stem

    output_dir = PROCESSED_DIR / nombre_base

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    output_video = (
        output_dir /
        f"{nombre_base}_tracking.avi"
    )

    model = cargar_modelo()

    tracking_data = ejecutar_tracking(
        video_path=video_path,
        output_video=output_video,
        model=model
    )

    fps = 30

    metricas = ejecutar_extraccion_features(
        tracking_data,
        fps
    )

    exportar_resultados(
        metricas,
        tracking_data,
        nombre_base
        )

    print(
        f"Metricas generadas: "
        f"{len(metricas)}"
    )


if __name__ == "__main__":
    main()