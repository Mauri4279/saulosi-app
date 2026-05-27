from src.feature_extraction.exporters import (
    exportar_csv,
    exportar_parquet,
    exportar_json
)

from src.feature_extraction.heatmap_generator import (
    generar_heatmap
)

from src.profiling.profile_statistics import (
    generar_perfiles
)

from src.profiling.profile_exporter import (
    exportar_perfiles_csv,
    exportar_perfiles_json
)

from src.utils.paths import (
    CSV_METRICS_DIR,
    PARQUET_METRICS_DIR,
    JSON_METRICS_DIR,
    HEATMAPS_DIR,
    PROFILE_JSON_DIR,
    PROFILE_CSV_DIR
)


def exportar_resultados(
    metricas,
    tracking_data,
    nombre_base
):

    # =========================
    # CREAR DIRECTORIOS
    # =========================

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

    PROFILE_JSON_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    PROFILE_CSV_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    # =========================
    # OUTPUTS METRICAS
    # =========================

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

    # =========================
    # EXPORT CSV
    # =========================

    try:

        exportar_csv(
            metricas,
            csv_output
        )

        print(
            f"CSV exportado: "
            f"{csv_output}"
        )

    except Exception as e:

        print(
            f"Error exportando CSV: "
            f"{e}"
        )

    # =========================
    # EXPORT PARQUET
    # =========================

#    try:
#
#        exportar_parquet(
#            metricas,
#            parquet_output
#        )
#
#        print(
#            f"PARQUET exportado: "
#            f"{parquet_output}"
#        )
#
#    except Exception as e:
#
#        print(
#            f"Error exportando PARQUET: "
#            f"{e}"
#        )

    # =========================
    # EXPORT JSON
    # =========================

    try:

        exportar_json(
            metricas,
            json_output
        )

        print(
            f"JSON exportado: "
            f"{json_output}"
        )

    except Exception as e:

        print(
            f"Error exportando JSON: "
            f"{e}"
        )

    # =========================
    # HEATMAP
    # =========================

    posiciones = [

        (d["cx"], d["cy"])

        for d in tracking_data
    ]

    heatmap_output = (
        HEATMAPS_DIR /
        f"{nombre_base}_heatmap.png"
    )

    try:

        generar_heatmap(
            posiciones,
            heatmap_output
        )

        print(
            f"Heatmap exportado: "
            f"{heatmap_output}"
        )

    except Exception as e:

        print(
            f"Error generando heatmap: "
            f"{e}"
        )

    # =========================
    # GENERAR PERFILES
    # =========================

    perfiles = generar_perfiles(
        metricas
    )

    # =========================
    # OUTPUTS PERFILES
    # =========================

    profile_csv_output = (
        PROFILE_CSV_DIR /
        f"{nombre_base}_profiles.csv"
    )

    profile_json_output = (
        PROFILE_JSON_DIR /
        f"{nombre_base}_profiles.json"
    )

    # =========================
    # EXPORT PROFILE CSV
    # =========================

    try:

        exportar_perfiles_csv(
            perfiles,
            profile_csv_output
        )

        print(
            f"Profiles CSV exportado: "
            f"{profile_csv_output}"
        )

    except Exception as e:

        print(
            f"Error exportando profiles CSV: "
            f"{e}"
        )

    # =========================
    # EXPORT PROFILE JSON
    # =========================

    try:

        exportar_perfiles_json(
            perfiles,
            profile_json_output
        )

        print(
            f"Profiles JSON exportado: "
            f"{profile_json_output}"
        )

    except Exception as e:

        print(
            f"Error exportando profiles JSON: "
            f"{e}"
        )