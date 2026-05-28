import pandas as pd


def exportar_behavior_statistics_csv(
    data,
    output
):

    pd.DataFrame(
        data
    ).to_csv(
        output,
        index=False
    )


def exportar_behavior_statistics_json(
    data,
    output
):

    pd.DataFrame(
        data
    ).to_json(
        output,
        orient="records",
        indent=4
    )