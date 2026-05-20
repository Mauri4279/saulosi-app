# 🐠 Saulosi App

## Descripción

Saulosi App es un sistema experimental de Inteligencia Artificial y Visión por Computadora orientado al monitoreo inteligente de ecosistemas acuáticos domésticos mediante análisis automatizado de video.

El proyecto utiliza técnicas de Deep Learning, tracking multiobjeto y análisis comportamental para interpretar patrones de movimiento en peces ornamentales dentro de acuarios. A partir de esta información, el sistema busca detectar anomalías o posibles incidencias de forma temprana, generando métricas y futuras recomendaciones orientativas para el usuario.

La propuesta combina conceptos de:

- Machine Learning
- Deep Learning
- Visión por Computadora
- Análisis temporal
- Ciencia de Datos
- Ingeniería de Software

El sistema fue concebido bajo una arquitectura modular y escalable, permitiendo evolucionar progresivamente desde un prototipo académico hacia una solución más robusta y extensible.

---

# 🎯 Objetivo del proyecto

El objetivo principal de Saulosi App es desarrollar un sistema capaz de analizar automáticamente el comportamiento de peces mediante secuencias de video, permitiendo detectar patrones asociados a posibles alteraciones dentro del ecosistema acuático.

Entre los comportamientos de interés se incluyen:

- cambios bruscos de actividad
- competencia por alimento
- agresividad
- territorialidad
- aislamiento
- estrés
- anomalías de movimiento

El proyecto busca validar la viabilidad de utilizar técnicas modernas de visión por computadora y aprendizaje automático para transformar información visual en indicadores comportamentales cuantificables.

---

# 🧠 Arquitectura del sistema

El sistema se encuentra organizado mediante una arquitectura modular desacoplada, donde cada componente cumple una responsabilidad específica dentro del pipeline general.

La arquitectura lógica se divide en:

- módulo de entrada de datos
- módulo de procesamiento de video
- módulo de detección
- módulo de tracking
- módulo de extracción de features
- módulo de inferencia
- módulo de visualización

Este enfoque favorece:

- mantenibilidad
- reutilización de componentes
- escalabilidad
- depuración del sistema
- evolución independiente de módulos

---

# ⚙️ Pipeline de procesamiento

El flujo principal del sistema sigue la siguiente secuencia:

```text
captura de video
        ↓
preprocesamiento
        ↓
detección de peces
        ↓
tracking multiobjeto
        ↓
extracción de features
        ↓
inferencia
        ↓
visualización de resultados
```

Actualmente el sistema implementa:

- lectura y procesamiento de video mediante OpenCV
- normalización y redimensionamiento de frames
- detección mediante YOLOv8
- tracking persistente utilizando BoT-SORT
- asignación de IDs únicos
- generación de trayectorias históricas
- overlays visuales y métricas en tiempo real
- exportación automática de video procesado

---

# 🛠 Tecnologías utilizadas

## Lenguaje principal

- Python

## Procesamiento de video e imágenes

- OpenCV
- FFmpeg
- NumPy

## Detección de objetos

- Ultralytics YOLOv8
- Roboflow

## Tracking

- BoT-SORT
- ByteTrack (etapas iniciales)

## Ciencia de datos y Machine Learning

- Pandas
- Scikit-learn

## Desarrollo y gestión

- Git
- GitHub

## Tecnologías futuras contempladas

- Streamlit
- PyTorch
- TensorFlow
- Docker
- SQLite / PostgreSQL
- Integración IoT

---

# 📁 Estructura del proyecto

```text
SAULOSI_APP/
│
├── data/
│   ├── raw/
│   │   ├── videos/
│   │   └── annotations/
│   │
│   ├── processed/
│   │
│   └── datasets/
│       └── inference/
│
├── models/
│   └── detection/
│       ├── pretrained/
│       └── trained/
│
├── outputs/
│
├── src/
│   ├── detection/
│   ├── feature_extraction/
│   ├── inference/
│   ├── input/
│   ├── preprocessing/
│   ├── tracking/
│   │   └── botsort/
│   ├── utils/
│   └── visualization/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 📌 Estado actual

## Fases completadas parcialmente

### Fase 1 — Definición y preparación del proyecto

- Definición conceptual del sistema
- Diseño inicial de arquitectura modular
- Investigación sobre visión por computadora y comportamiento de peces
- Planificación general del pipeline

### Fase 2 — Recolección y construcción del dataset

- Recolección colaborativa de videos
- Estandarización de formatos
- Convención estructurada de nombres
- Organización inicial del dataset

### Fase 3 — Preprocesamiento y exploración

- Extracción y procesamiento de frames
- Normalización de resolución
- Limpieza de datos visuales
- Exploración inicial del dataset

### Fase 4 — Detección de objetos

- Etiquetado manual mediante Roboflow
- Entrenamiento personalizado de YOLOv8
- Aplicación de Transfer Learning
- Implementación de Data Augmentation
- Evaluación de métricas de detección

### Fase 5 — Tracking

- Integración inicial con ByteTrack
- Migración y optimización mediante BoT-SORT
- Reducción significativa de ID Switching
- Implementación de trayectorias persistentes
- Visualización de estelas históricas

---

# 🚀 Próximos pasos

Las siguientes etapas del proyecto contemplan:

### Fase 6 — Extracción de features

- cálculo de velocidad
- aceleración
- permanencia espacial
- interacción entre individuos
- métricas temporales

### Fase 7 — Modelado e inferencia

- detección de anomalías
- clasificación comportamental
- modelos predictivos
- análisis temporal avanzado

### Fase 8 — Desarrollo de interfaz

- dashboard interactivo
- visualización de métricas
- carga de videos
- recomendaciones automáticas

### Fase 9 — Evaluación integral

- validación de extremo a extremo
- optimización de rendimiento
- análisis de robustez
- mejora de experiencia de usuario

### Fase 10 — Documentación y presentación

- documentación técnica final
- diagramas y métricas
- presentación académica
- preparación de defensa

---

# ▶️ Instalación

## Clonar el repositorio

```bash
git clone <https://github.com/Mauri4279/saulosi-app>
cd saulosi-app
```

## Crear entorno virtual

```bash
python -m venv venv
```

## Activar entorno virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Descargar modelo entrenado

El archivo `best.pt` no se incluye en el repositorio debido a limitaciones de tamaño.

Descargar manualmente desde:

[https://drive.google.com/drive/folders/10z-bkLrm8DFoyQT_GRFfOYyyK0RU_NWj?usp=sharing]

Luego colocar el archivo en:

models/detection/trained/

---

# ▶️ Uso

Colocar los videos dentro de:

```text
data/raw/videos/
```

Ejecutar el sistema:

```bash
python main.py
```

Los resultados procesados serán exportados automáticamente dentro de:

```text
data/processed/
```

---

# 🛣 Roadmap

## Fase 1 — Definición y preparación
- objetivos y alcance
- arquitectura del sistema
- investigación conceptual

## Fase 2 — Dataset
- recopilación colaborativa
- organización y estandarización
- etiquetado inicial

## Fase 3 — Preprocesamiento
- extracción de frames
- limpieza de datos
- exploración visual

## Fase 4 — Detección
- entrenamiento YOLOv8
- validación
- optimización inicial

## Fase 5 — Tracking
- seguimiento multiobjeto
- reducción de ID Switching
- trayectorias persistentes

## Fase 6 — Features
- velocidad
- aceleración
- proximidad
- permanencia espacial

## Fase 7 — Inferencia
- detección de anomalías
- análisis comportamental
- modelos predictivos

## Fase 8 — Interfaz
- Streamlit
- dashboard visual
- recomendaciones

## Fase 9 — Evaluación
- testing integral
- validación técnica
- optimización

## Fase 10 — Presentación final
- documentación
- defensa académica
- resultados y conclusiones

---

# 👨‍💻 Autores

Guido Di Iorio
Mariela Flores
Mauricio Ruiz 

Proyecto académico y experimental enfocado en:

- Inteligencia Artificial
- Visión por Computadora
- Ciencia de Datos
- Machine Learning
- Sistemas inteligentes
- Análisis automatizado de comportamiento animal
