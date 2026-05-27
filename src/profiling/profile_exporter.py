import pandas as pd


def exportar_perfiles_csv(
    perfiles,
    output
):

    pd.DataFrame(perfiles).to_csv(
        output,
        index=False
    )


def exportar_perfiles_json(
    perfiles,
    output
):

    pd.DataFrame(perfiles).to_json(
        output,
        orient="records",
        indent=4
    )