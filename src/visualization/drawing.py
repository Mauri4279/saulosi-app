import cv2

def dibujar_texto_borde(img, texto, posicion, escala, color, grosor):
    """
    Dibuja texto con borde negro para mejorar legibilidad.
    """
    cv2.putText(
        img,
        texto,
        posicion,
        cv2.FONT_HERSHEY_SIMPLEX,
        escala,
        (0, 0, 0),
        grosor + 2
    )

    cv2.putText(
        img,
        texto,
        posicion,
        cv2.FONT_HERSHEY_SIMPLEX,
        escala,
        color,
        grosor
    )