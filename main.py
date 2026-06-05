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

from src.validation.validation_pipeline import (
    ejecutar_validacion
)

VIDEO_NAME = (
    "vid_022_part_03_acuario_domestico_agresion_distancia_varias_posiciones.mp4"
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

    resultado_features = (
        ejecutar_extraccion_features(
            tracking_data,
            fps
        )
    )

    metricas = resultado_features[
        "metricas"
    ]

    matriz_social = resultado_features[
        "matriz_social"
    ]

    exportar_resultados(
        metricas,
        tracking_data,
        nombre_base,
        matriz_social,
        fps
        )
    
    ejecutar_validacion(
        metricas,
        nombre_base
        )

    print(
        f"Metricas generadas: "
        f"{len(metricas)}"
    )


if __name__ == "__main__":
    main()