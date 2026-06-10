# 🐠 Saulosi App

> Sistema experimental de **Visión por Computadora e Inteligencia Artificial** para el análisis automatizado del comportamiento de peces ornamentales mediante detección, tracking multiobjeto y extracción de métricas etológicas.

Saulosi transforma secuencias de video en información estructurada, permitiendo analizar comportamientos e interacciones sociales con el objetivo de contribuir al bienestar animal y brindar una herramienta de apoyo para la investigación.

---

# ✨ Características

* Detección automática de peces mediante **YOLOv8**
* Tracking persistente utilizando **BoT-SORT**
* Asignación de IDs únicos para cada individuo
* Visualización mediante Bounding Boxes
* Extracción de métricas cinéticas y espaciales
* Análisis de interacciones etológicas
* Base para futuros modelos de inferencia comportamental
* Arquitectura modular y escalable
* Exportación automática de videos procesados y resultados

---

# 🎯 Objetivo

El objetivo de Saulosi es desarrollar un sistema capaz de interpretar automáticamente el comportamiento de peces ornamentales mediante técnicas modernas de Visión por Computadora e Inteligencia Artificial.

A partir de secuencias de video, el sistema genera información estructurada que permitirá detectar patrones asociados a:

* actividad y movimiento
* territorialidad
* competencia por alimento
* agresividad
* aislamiento
* estrés
* anomalías comportamentales

La propuesta busca validar la utilización de modelos de Deep Learning para convertir información visual en indicadores cuantificables de comportamiento animal.

---

# 🏛 Arquitectura

El sistema fue diseñado siguiendo una arquitectura modular desacoplada, permitiendo la evolución independiente de cada componente del pipeline.

```text
Entrada de video
        │
        ▼
Preprocesamiento
        │
        ▼
Detección (YOLOv8)
        │
        ▼
Tracking (BoT-SORT)
        │
        ▼
Extracción de métricas
        │
        ▼
Motor de inferencia
        │
        ▼
Visualización y exportación
```

Este enfoque favorece:

* mantenibilidad
* reutilización de componentes
* escalabilidad
* facilidad de testing
* evolución progresiva del sistema

---

# ⚙️ Pipeline implementado

Actualmente Saulosi es capaz de realizar:

* lectura y procesamiento de video mediante OpenCV
* normalización de frames
* detección automática de peces
* tracking multiobjeto con IDs persistentes
* generación de trayectorias históricas
* overlays visuales en tiempo real
* extracción de métricas comportamentales
* exportación automática de resultados

---

# 🛠 Tecnologías

## Lenguaje

* Python

## Visión por Computadora

* OpenCV
* Ultralytics YOLOv8
* FFmpeg

## Tracking

* BoT-SORT
* ByteTrack (implementación inicial)

## Ciencia de Datos

* NumPy
* Pandas
* Scikit-learn

## Desarrollo

* Git
* GitHub

## Tecnologías contempladas para futuras versiones

* PyTorch
* TensorFlow
* Streamlit
* Docker
* SQLite / PostgreSQL
* Integración IoT

---

# 📁 Estructura del proyecto

```text
SAULOSI_APP/
│
├── data/
│   ├── raw/
│   │   ├── videos/
│   │   └── annotations/
│   ├── processed/
│   └── datasets/
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
│   ├── utils/
│   └── visualization/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 🚀 Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/Mauri4279/saulosi-app.git

cd saulosi-app
```

---

## 2. Crear un entorno virtual (recomendado)

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4. Descargar el modelo entrenado

Debido al tamaño del archivo, el modelo entrenado (`best.pt`) no forma parte del repositorio.

Descargar manualmente desde:

[https://drive.google.com/drive/folders/10z-bkLrm8DFoyQT_GRFfOYyyK0RU_NWj?usp=sharing]

Una vez descargado, ubicarlo en:

```text
models/
└── detection/
    └── trained/
        └── best.pt
```

---

## 5. Agregar videos

Colocar los videos a procesar dentro de:

```text
data/
└── raw/
    └── videos/
```

---

## 6. Ejecutar la aplicación

```bash
python main.py
```

---

## 7. Resultados

Los videos procesados y las métricas generadas serán exportados automáticamente dentro de la carpeta /outputs

# 🔬 Roadmap

## ✅ Implementado

* Detección mediante YOLOv8
* Tracking multiobjeto con BoT-SORT
* IDs persistentes
* Bounding Boxes
* Trayectorias históricas
* Extracción de métricas comportamentales
* Exportación automática de resultados

## 🚧 En desarrollo

* Motor de inferencia basado en métricas
* Clasificación automática de comportamientos
* Detección de anomalías

## ⏳ Próximas funcionalidades

* Dashboard interactivo
* Visualización estadística
* Reportes automáticos
* Recomendaciones orientadas al bienestar animal
* Integración con dispositivos IoT

---

# 👥 Autores

* Guido Di Iorio
* Mariela Flores
* Mauricio Ruiz

---

# 📚 Áreas de aplicación

* Inteligencia Artificial
* Visión por Computadora
* Deep Learning
* Machine Learning
* Ciencia de Datos
* Sistemas Inteligentes
* Análisis automatizado de comportamiento animal

---

# ⭐ Proyecto

Saulosi es un proyecto académico y experimental desarrollado con el objetivo de explorar la aplicación de técnicas modernas de Inteligencia Artificial al análisis comportamental de peces ornamentales.

Su diseño modular permite continuar incorporando nuevos algoritmos, métricas y modelos de inferencia, evolucionando progresivamente hacia una plataforma integral de análisis para investigación y apoyo al bienestar animal.

