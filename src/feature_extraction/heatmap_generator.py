import matplotlib.pyplot as plt


def generar_heatmap(
    posiciones,
    output_path
):

    xs = [p[0] for p in posiciones]
    ys = [p[1] for p in posiciones]

    plt.figure(figsize=(10, 6))

    plt.hist2d(
        xs,
        ys,
        bins=60
    )

    plt.gca().invert_yaxis()

    plt.colorbar()

    plt.savefig(output_path)

    plt.close()