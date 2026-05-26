import pandas as pd


def exportar_csv(metricas, output):

    pd.DataFrame(metricas).to_csv(
        output,
        index=False
    )


def exportar_parquet(metricas, output):

    pd.DataFrame(metricas).to_parquet(
        output,
        index=False
    )


def exportar_json(metricas, output):

    pd.DataFrame(metricas).to_json(
        output,
        orient="records",
        indent=4
    )