from pathlib import Path

from src.detection.detector import cargar_modelo
from src.tracking.tracker_pipeline import ejecutar_tracking

from src.utils.paths import (
    RAW_VIDEOS_DIR,
    PROCESSED_DIR
)

VIDEO_NAME = "vid_001_part_02_acuario_domestico_mucho_movimiento.mp4"


def main():

    video_path = RAW_VIDEOS_DIR / VIDEO_NAME

    nombre_base = Path(VIDEO_NAME).stem

    output_dir = PROCESSED_DIR / nombre_base
    output_dir.mkdir(parents=True, exist_ok=True)

    output_video = (
        output_dir /
        f"{nombre_base}_tracking.avi"
    )

    model = cargar_modelo()

    ejecutar_tracking(
        video_path=video_path,
        output_video=output_video,
        model=model
    )


if __name__ == "__main__":
    main()