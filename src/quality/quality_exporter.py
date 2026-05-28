import pandas as pd


def exportar_quality_csv(
    quality_data,
    output
):
    """
    Exporta quality metrics a CSV.
    """

    df = pd.DataFrame(
        quality_data
    )

    df.to_csv(
        output,
        index=False
    )


def exportar_quality_json(
    quality_data,
    output
):
    """
    Exporta quality metrics a JSON.
    """

    df = pd.DataFrame(
        quality_data
    )

    df.to_json(
        output,
        orient="records",
        indent=4
    )