import pandas as pd


def exportar_behavior_csv(
    behavior_data,
    output
):

    pd.DataFrame(
        behavior_data
    ).to_csv(
        output,
        index=False
    )


def exportar_behavior_json(
    behavior_data,
    output
):

    pd.DataFrame(
        behavior_data
    ).to_json(
        output,
        orient="records",
        indent=4
    )