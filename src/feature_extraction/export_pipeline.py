from src.feature_extraction.exporters import (
    exportar_csv,
    exportar_parquet,
    exportar_json
)

from src.feature_extraction.heatmap_generator import (
    generar_heatmap
)

from src.utils.paths import (
    CSV_METRICS_DIR,
    PARQUET_METRICS_DIR,
    JSON_METRICS_DIR,
    HEATMAPS_DIR
)


def exportar_resultados(
    metricas,
    tracking_data,
    nombre_base
):

    CSV_METRICS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    PARQUET_METRICS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    JSON_METRICS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    HEATMAPS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    csv_output = (
        CSV_METRICS_DIR /
        f"{nombre_base}_metricas.csv"
    )

    parquet_output = (
        PARQUET_METRICS_DIR /
        f"{nombre_base}_metricas.parquet"
    )

    json_output = (
        JSON_METRICS_DIR /
        f"{nombre_base}_metricas.json"
    )

    exportar_csv(
        metricas,
        csv_output
    )

    exportar_parquet(
        metricas,
        parquet_output
    )

    exportar_json(
        metricas,
        json_output
    )

    posiciones = [

        (d["cx"], d["cy"])

        for d in tracking_data
    ]

    heatmap_output = (
        HEATMAPS_DIR /
        f"{nombre_base}_heatmap.png"
    )

    generar_heatmap(
        posiciones,
        heatmap_output
    )

    print(
        f"CSV exportado: {csv_output}"
    )

    print(
        f"PARQUET exportado: {parquet_output}"
    )

    print(
        f"JSON exportado: {json_output}"
    )

    print(
        f"Heatmap exportado: {heatmap_output}"
    )