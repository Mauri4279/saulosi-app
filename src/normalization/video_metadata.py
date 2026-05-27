from src.tracking.tracker_pipeline import (
    TARGET_W,
    TARGET_H
)

from src.normalization.kinematic_normalizer import (
    calcular_diagonal_frame
)


FRAME_WIDTH = TARGET_W

FRAME_HEIGHT = TARGET_H

FRAME_DIAGONAL = calcular_diagonal_frame(
    FRAME_WIDTH,
    FRAME_HEIGHT
)