import json
import csv


def exportar_agresiones_json(
    agresiones,
    output_path
):

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            agresiones,
            archivo,
            indent=4,
            ensure_ascii=False
        )


def exportar_agresiones_csv(
    agresiones,
    output_path
):

    if not agresiones:
        return

    campos = agresiones[0].keys()

    with open(
        output_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as archivo:

        writer = csv.DictWriter(
            archivo,
            fieldnames=campos
        )

        writer.writeheader()

        writer.writerows(
            agresiones
        )