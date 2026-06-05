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

from src.tracking.tracking_exporter import (
    exportar_tracking_csv,
    exportar_tracking_json
)

from src.quality.track_quality import (
    generar_quality_metrics
)

from src.quality.quality_exporter import (
    exportar_quality_csv,
    exportar_quality_json
)

from src.behavior.behavior_pipeline import (
    generar_behavior_profiles
)

from src.behavior.behavior_exporter import (
    exportar_behavior_csv,
    exportar_behavior_json
)

from src.behavior.behavior_statistics import (
    generar_behavior_statistics
)

from src.behavior.behavior_statistics_exporter import (
    exportar_behavior_statistics_csv,
    exportar_behavior_statistics_json
)

from src.social.social_proximity import (
    detectar_proximidades_sociales
)

from src.social.social_exporter import (
    exportar_social_csv,
    exportar_social_json
)

from src.social.chase_detection import (
    detectar_persecuciones
)

from src.social.chase_exporter import (
    exportar_persecuciones_csv,
    exportar_persecuciones_json
)

from src.social.aggression_detection import (
    detectar_agresiones
)

from src.social.aggression_exporter import (
    exportar_agresiones_csv,
    exportar_agresiones_json
)

from src.utils.paths import (
    CSV_METRICS_DIR,
    PARQUET_METRICS_DIR,
    JSON_METRICS_DIR,
    HEATMAPS_DIR,
    PROFILE_JSON_DIR,
    PROFILE_CSV_DIR,
    TRACKING_CSV_DIR,
    TRACKING_JSON_DIR,
    QUALITY_CSV_DIR,
    QUALITY_JSON_DIR,
    BEHAVIOR_CSV_DIR,
    BEHAVIOR_JSON_DIR,
    BEHAVIOR_STATS_CSV_DIR,
    BEHAVIOR_STATS_JSON_DIR,
    SOCIAL_PROXIMITY_CSV_DIR,
    SOCIAL_PROXIMITY_JSON_DIR,
    CHASE_CSV_DIR,
    CHASE_JSON_DIR,
    AGGRESSION_CSV_DIR,
    AGGRESSION_JSON_DIR
    )


def exportar_resultados(
    metricas,
    tracking_data,
    nombre_base,
    matriz_social,
    fps
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

    BEHAVIOR_CSV_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    BEHAVIOR_JSON_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    SOCIAL_PROXIMITY_CSV_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    SOCIAL_PROXIMITY_JSON_DIR.mkdir(
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
    # TRACKING EXPORT
    # =========================

    TRACKING_CSV_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    TRACKING_JSON_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    tracking_csv_output = (
        TRACKING_CSV_DIR /
        f"{nombre_base}_tracking.csv"
    )

    tracking_json_output = (
        TRACKING_JSON_DIR /
        f"{nombre_base}_tracking.json"
    )

    try:

        exportar_tracking_csv(
            tracking_data,
            tracking_csv_output
        )

        print(
            f"Tracking CSV exportado: "
            f"{tracking_csv_output}"
        )

    except Exception as e:

        print(
            f"Error exportando tracking CSV: "
            f"{e}"
        )

    try:

        exportar_tracking_json(
            tracking_data,
            tracking_json_output
        )

        print(
            f"Tracking JSON exportado: "
            f"{tracking_json_output}"
        )

    except Exception as e:

        print(
            f"Error exportando tracking JSON: "
            f"{e}"
        )

    # =========================
    # GENERAR PERFILES
    # =========================

    perfiles = generar_perfiles(
        metricas,
        tracking_data,
        matriz_social
    )

    # =========================
    # GENERAR SOCIAL METRICS
    # =========================

    quality_metrics = (
    generar_quality_metrics(
        tracking_data
    )
    )

    behavior_statistics = (
        generar_behavior_statistics(
            metricas
        )
    )

    social_proximity = (
        detectar_proximidades_sociales(
            tracking_data
        )
    )

    persecuciones = (
        detectar_persecuciones(
            tracking_data
        )
    )

    agresiones = (
        detectar_agresiones(
            tracking_data,
            fps=30
        )
    )

    # =========================
    # GENERAR BEHAVIOR
    # =========================

    print(
        "\nGenerando perfiles comportamentales..."
    )

    behavior_profiles = (
        generar_behavior_profiles(
            perfiles,
            quality_metrics
        )
    )

    print(
        f"Perfiles comportamentales generados: "
        f"{len(behavior_profiles)}"
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

    # =========================
    # QUALITY / TRACK RELIABILITY
    # =========================

    QUALITY_CSV_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    QUALITY_JSON_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    quality_metrics = (
        generar_quality_metrics(
            tracking_data
        )
    )

    quality_csv_output = (
        QUALITY_CSV_DIR /
        f"{nombre_base}_quality.csv"
    )

    quality_json_output = (
        QUALITY_JSON_DIR /
        f"{nombre_base}_quality.json"
    )

    # =========================
    # EXPORT QUALITY CSV
    # =========================

    try:

        exportar_quality_csv(
            quality_metrics,
            quality_csv_output
        )

        print(
            f"Quality CSV exportado: "
            f"{quality_csv_output}"
        )

    except Exception as e:

        print(
            f"Error exportando Quality CSV: "
            f"{e}"
        )

    # =========================
    # EXPORT QUALITY JSON
    # =========================

    try:

        exportar_quality_json(
            quality_metrics,
            quality_json_output
        )

        print(
            f"Quality JSON exportado: "
            f"{quality_json_output}"
        )

    except Exception as e:

        print(
            f"Error exportando Quality JSON: "
            f"{e}"
        )

    # =========================
    # BEHAVIOR EXPORT
    # =========================

    behavior_csv_output = (
        BEHAVIOR_CSV_DIR /
        f"{nombre_base}_behavior.csv"
    )

    behavior_json_output = (
        BEHAVIOR_JSON_DIR /
        f"{nombre_base}_behavior.json"
    )

    try:

        exportar_behavior_csv(
            behavior_profiles,
            behavior_csv_output
        )

        print(
            f"Behavior CSV exportado: "
            f"{behavior_csv_output}"
        )

    except Exception as e:

        print(
            f"Error exportando Behavior CSV: "
            f"{e}"
        )

    try:

        exportar_behavior_json(
            behavior_profiles,
            behavior_json_output
        )

        print(
            f"Behavior JSON exportado: "
            f"{behavior_json_output}"
        )

    except Exception as e:

        print(
            f"Error exportando Behavior JSON: "
            f"{e}"
        )

    # =========================
    # BEHAVIOR STATISTICS EXPORT
    # =========================

    BEHAVIOR_STATS_CSV_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    BEHAVIOR_STATS_JSON_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    stats_csv_output = (
        BEHAVIOR_STATS_CSV_DIR /
        f"{nombre_base}_behavior_stats.csv"
    )

    stats_json_output = (
        BEHAVIOR_STATS_JSON_DIR /
        f"{nombre_base}_behavior_stats.json"
    )

    try:

        exportar_behavior_statistics_csv(
            behavior_statistics,
            stats_csv_output
        )

        print(
            f"Behavior Stats CSV exportado: "
            f"{stats_csv_output}"
        )

    except Exception as e:

        print(
            f"Error exportando Behavior Stats CSV: "
            f"{e}"
        )

    try:

        exportar_behavior_statistics_json(
            behavior_statistics,
            stats_json_output
        )

        print(
            f"Behavior Stats JSON exportado: "
            f"{stats_json_output}"
        )

    except Exception as e:

        print(
            f"Error exportando Behavior Stats JSON: "
            f"{e}"
        )

    # =========================
    # SOCIAL PROXIMITY EXPORT
    # =========================

    social_csv_output = (
        SOCIAL_PROXIMITY_CSV_DIR /
        f"{nombre_base}_social.csv"
    )

    social_json_output = (
        SOCIAL_PROXIMITY_JSON_DIR /
        f"{nombre_base}_social.json"
    )

    try:

        exportar_social_csv(
            social_proximity,
            social_csv_output
        )

        print(
            f"Social proximity CSV exportado: "
            f"{social_csv_output}"
        )

    except Exception as e:

        print(
            f"Error Social proximity CSV: "
            f"{e}"
        )

    try:

        exportar_social_json(
            social_proximity,
            social_json_output
        )

        print(
            f"Social proximity JSON exportado: "
            f"{social_json_output}"
        )

    except Exception as e:

        print(
            f"Error Social proximity json: "
            f"{e}"
        )


    # =========================
    # SOCIAL CHASE EXPORT
    # =========================

    CHASE_CSV_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    CHASE_JSON_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    chase_csv_output = (
        CHASE_CSV_DIR /
        f"{nombre_base}_chase.csv"
    )

    chase_json_output = (
        CHASE_JSON_DIR /
        f"{nombre_base}_chase.json"
    )

    try:

        exportar_persecuciones_csv(
            persecuciones,
            chase_csv_output
        )

        print(
            f"Chase CSV exportado: "
            f"{chase_csv_output}"
        )

    except Exception as e:

        print(
            f"Error Chase CSV: "
            f"{e}"
        )

    try:

        exportar_persecuciones_json(
            persecuciones,
            chase_json_output
        )

        print(
            f"Chase JSON exportado: "
            f"{chase_json_output}"
        )

    except Exception as e:

        print(
            f"Error Chase JSON: "
            f"{e}"
        )

    # =========================
    # SOCIAL AGGRESSION EXPORT
    # =========================

    AGGRESSION_CSV_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    AGGRESSION_JSON_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    aggression_csv_output = (
        AGGRESSION_CSV_DIR /
        f"{nombre_base}_aggression.csv"
    )

    aggression_json_output = (
        AGGRESSION_JSON_DIR /
        f"{nombre_base}_aggression.json"
    )

    try:

        exportar_agresiones_csv(
            agresiones,
            aggression_csv_output
        )

        print(
            f"Aggression CSV exportado: "
            f"{aggression_csv_output}"
        )

    except Exception as e:

        print(
            f"Error Aggression CSV: "
            f"{e}"
        )

    try:

        exportar_agresiones_json(
            agresiones,
            aggression_json_output
        )

        print(
            f"Aggression JSON exportado: "
            f"{aggression_json_output}"
        )

    except Exception as e:

        print(
            f"Error Aggression JSON: "
            f"{e}"
        )