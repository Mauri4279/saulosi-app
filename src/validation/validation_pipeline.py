import json

from pathlib import Path

from src.validation.metric_consistency import (
    validar_consistencia
)

from src.validation.threshold_validator import (
    analizar_thresholds
)

from src.validation.statistics import (
    generar_estadisticas
)


OUTPUT_DIR = Path(
    "outputs/validation"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


def ejecutar_validacion(
    metricas,
    nombre_base
):

    inconsistencias = validar_consistencia(
        metricas
    )

    thresholds = analizar_thresholds(
        metricas
    )

    estadisticas = generar_estadisticas(
        metricas
    )

    consistency_output = (
        OUTPUT_DIR /
        f"{nombre_base}_consistency.json"
    )

    threshold_output = (
        OUTPUT_DIR /
        f"{nombre_base}_thresholds.json"
    )

    stats_output = (
        OUTPUT_DIR /
        f"{nombre_base}_stats.json"
    )

    with open(
        consistency_output,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            inconsistencias,
            f,
            indent=4
        )

    with open(
        threshold_output,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            thresholds,
            f,
            indent=4
        )

    with open(
        stats_output,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            estadisticas,
            f,
            indent=4
        )

    print("\n======================")
    print("VALIDACION FINALIZADA")
    print("======================")

    print(
        f"Inconsistencias: "
        f"{len(inconsistencias)}"
    )

    print(
        f"Thresholds exportados:"
        f" {threshold_output}"
    )

    print(
        f"Estadisticas exportadas:"
        f" {stats_output}"
    )