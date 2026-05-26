from pathlib import Path

# ROOT DEL PROYECTO
ROOT_DIR = Path(__file__).resolve().parents[2]

# =========================
# DATA
# =========================
DATA_DIR = ROOT_DIR / "data"

RAW_VIDEOS_DIR = DATA_DIR / "raw" / "videos"
PROCESSED_DIR = DATA_DIR / "processed"

# =========================
# OUTPUTS
# =========================

OUTPUTS_DIR = ROOT_DIR / "outputs"

METRICS_DIR = OUTPUTS_DIR / "metrics"

CSV_METRICS_DIR = METRICS_DIR / "csv"

PARQUET_METRICS_DIR = METRICS_DIR / "parquet"

JSON_METRICS_DIR = METRICS_DIR / "json"

HEATMAPS_DIR = OUTPUTS_DIR / "heatmaps"

# =========================
# MODELOS
# =========================
MODELS_DIR = ROOT_DIR / "models"

DETECTION_MODELS_DIR = MODELS_DIR / "detection"

MODEL_PATH = DETECTION_MODELS_DIR / "trained" / "best.pt"

# =========================
# TRACKING
# =========================
TRACKING_DIR = ROOT_DIR / "src" / "tracking"

TRACKER_CONF = TRACKING_DIR / "botsort" / "custom_botsort.yaml"