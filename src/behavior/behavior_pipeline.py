from src.behavior.behavior_classifier import (
    clasificar_comportamiento
)


def generar_behavior_profiles(
    perfiles,
    quality_metrics
):

    return clasificar_comportamiento(
        perfiles,
        quality_metrics
    )