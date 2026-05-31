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
# BEHAVIOR PROFILES
# =========================

PROFILES_DIR = OUTPUTS_DIR / "profiles"

PROFILE_JSON_DIR = (
    PROFILES_DIR / "json"
)

PROFILE_CSV_DIR = (
    PROFILES_DIR / "csv"
)

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

# =========================
# TRACKING EXPORTS
# =========================

TRACKING_DIR = OUTPUTS_DIR / "tracking"

TRACKING_CSV_DIR = (
    TRACKING_DIR / "csv"
)

TRACKING_JSON_DIR = (
    TRACKING_DIR / "json"
)

# =========================
# QUALITY
# =========================

QUALITY_DIR = (
    OUTPUTS_DIR / "quality"
)

QUALITY_CSV_DIR = (
    QUALITY_DIR / "csv"
)

QUALITY_JSON_DIR = (
    QUALITY_DIR / "json"
)

# =========================
# BEHAVIOR
# =========================

BEHAVIOR_DIR = (
    OUTPUTS_DIR / "behavior"
)

BEHAVIOR_CSV_DIR = (
    BEHAVIOR_DIR / "csv"
)

BEHAVIOR_JSON_DIR = (
    BEHAVIOR_DIR / "json"
)

# =========================
# BEHAVIOR STATISTICS
# =========================

BEHAVIOR_STATS_DIR = (
    OUTPUTS_DIR / "behavior_stats"
)

BEHAVIOR_STATS_CSV_DIR = (
    BEHAVIOR_STATS_DIR / "csv"
)

BEHAVIOR_STATS_JSON_DIR = (
    BEHAVIOR_STATS_DIR / "json"
)

# =========================
# SOCIAL EVENTS
# =========================

SOCIAL_PROXIMITY_DIR = (
    OUTPUTS_DIR / "social_proximity"
)

SOCIAL_PROXIMITY_CSV_DIR = (
    SOCIAL_PROXIMITY_DIR / "csv"
)

SOCIAL_PROXIMITY_JSON_DIR = (
    SOCIAL_PROXIMITY_DIR / "json"
)