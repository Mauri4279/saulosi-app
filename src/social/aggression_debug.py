def exportar_candidatos_agresion(
    candidatos,
    output_path
):
    import json

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            candidatos,
            f,
            indent=4
        )