import pandas as pd


def exportar_tracking_csv(
    tracking_data,
    output
):

    pd.DataFrame(
        tracking_data
    ).to_csv(
        output,
        index=False
    )


def exportar_tracking_json(
    tracking_data,
    output
):

    pd.DataFrame(
        tracking_data
    ).to_json(
        output,
        orient="records",
        indent=4
    )