import pandas as pd


def exportar_persecuciones_csv(
    eventos,
    output
):

    pd.DataFrame(
        eventos
    ).to_csv(
        output,
        index=False
    )


def exportar_persecuciones_json(
    eventos,
    output
):

    pd.DataFrame(
        eventos
    ).to_json(
        output,
        orient="records",
        indent=4
    )