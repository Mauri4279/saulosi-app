from ultralytics import YOLO
from src.utils.paths import MODEL_PATH

def cargar_modelo():
    print(f"Cargando modelo YOLO desde: {MODEL_PATH}")
    return YOLO(str(MODEL_PATH))