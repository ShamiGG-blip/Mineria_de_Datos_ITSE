# PI_Mineria_Datos_1

## Información general

Proyecto Integrador de la materia Minería de Datos 1. Análisis reproducible sobre un
dataset de usuarios de una plataforma de streaming, desde la inspección inicial hasta
las conclusiones, comunicado mediante una aplicación en Streamlit y un informe final.

**Integrantes:** [Gonzalez Shamira] — [Serrano Yonathan]
**Comisión:** [Turno mañana-Nueva Esperanza]
**Fecha:** 4 de Julio 2026

## Objetivo del proyecto

Aplicar los contenidos de Minería de Datos 1 sobre el dataset de usuarios de streaming,
mediante un proceso ordenado de exploración, preparación, análisis exploratorio y
reducción de dimensionalidad (PCA). Las decisiones de cada etapa se justifican con
evidencia observada en los datos, no con la aplicación automática de técnicas. El
alcance no incluye modelado predictivo ni despliegue de modelos, sino comprensión,
preparación y comunicación clara de resultados para un público técnico y general.

## Dataset

Fuente: `data/raw/streaming_users_dirty.json`, provisto por la cátedra (8160 registros).
Variables: `user_id`, `age`, `subscription_plan`, `monthly_watch_time_mins`, `country`,
`favorite_genre`, `last_login_date`, `customer_support_tickets`.

El dataset original presenta nulos, filas y usuarios duplicados, valores fuera de rango
(edades y consumo negativos, códigos centinela en tickets de soporte), categorías con
grafías inconsistentes y fechas en múltiples formatos. El detalle de la inspección está
en `notebooks/01_inspeccion_inicial.ipynb`, y el dataset final utilizado en el análisis
en `data/processed/streaming_users_clean.csv`.

## Estructura del repositorio

```
PI_Mineria_Datos_1/
├── README.md
├── requirements.txt
├── data/{raw,processed}/
├── notebooks/01_inspeccion_inicial.ipynb ... 05_conclusiones.ipynb
├── app/Home.py + app/pages/01_Dataset.py ... 04_Conclusiones.py
├── reports/informe_final.pdf
└── logs/pipeline_log.csv
```

## Preparación y calidad de datos

Las decisiones de limpieza se desarrollan y justifican en
`notebooks/02_calidad_y_limpieza.ipynb`, con trazabilidad completa en
`logs/pipeline_log.csv`. En síntesis: se eliminaron 126 filas duplicadas y 34 `user_id`
repetidos adicionales; se marcaron como faltantes y se imputaron con mediana los valores
fuera de rango de `age`, `monthly_watch_time_mins` y `customer_support_tickets`
(incluyendo códigos centinela como 99999 y 99/150); se normalizaron las categorías de
`subscription_plan`, `country` y `favorite_genre` a valores canónicos; y se parsearon
las fechas de `last_login_date` probando los formatos detectados, dejando como faltante
lo no resoluble sin ambigüedad. El dataset original se preservó sin modificar en
`data/raw/`.

## Resumen del análisis exploratorio

Desarrollado en `notebooks/03_eda.ipynb` y resumido en la app (`app/pages/02_EDA.py`).
Hallazgos principales: la edad se concentra entre 25 y 45 años; el consumo mensual tiene
distribución asimétrica; existe una asociación agregada entre plan de suscripción y
consumo (medianas crecientes de Básico a Premium), no mediada por la edad; los tickets
de soporte no se relacionan con plan ni edad; y el país de origen no muestra diferencias
relevantes de consumo. Las variables numéricas presentan correlación cercana a 0 entre
sí, lo cual anticipa los resultados de la etapa de PCA.

## Reducción de dimensionalidad

Desarrollada en `notebooks/04_pca.ipynb`. Se aplicó `StandardScaler` sobre `age`,
`monthly_watch_time_mins` y `customer_support_tickets`, y luego PCA. Las 3 componentes
explican una proporción casi idéntica de varianza (~33% cada una), reflejo directo de la
baja correlación entre las variables originales. Conclusión: no conviene reducir
dimensionalidad en este subconjunto de variables sin incorporar información adicional,
ya que se perdería información sin ganar interpretabilidad ni compacidad.

## Visualización interactiva

La aplicación pública en Streamlit (`app/`) comunica los resultados para público
general: descripción y calidad del dataset, 5 visualizaciones de EDA interpretadas,
resultados de PCA y conclusiones. No reemplaza la evidencia técnica de los notebooks.

**Enlace público:** [completar enlace de Streamlit Cloud]

## Cómo ejecutar localmente

```bash
git clone [completar URL del repositorio]
cd PI_Mineria_Datos_1
pip install -r requirements.txt
streamlit run app/Home.py
```

Para revisar el análisis técnico, abrir los notebooks de `notebooks/` en orden con
Jupyter (`jupyter notebook`) o VS Code.

## Conclusiones

El plan de suscripción se asocia a un mayor consumo mensual (Básico < Estándar <
Premium), sin que la edad medie esa relación; los tickets de soporte y el país no
resultan relevantes para explicar el consumo. Las variables numéricas disponibles están
descorrelacionadas entre sí, por lo que PCA no logra una reducción de dimensionalidad
eficiente. El alcance de estas conclusiones está condicionado por las decisiones de
limpieza documentadas (imputación por mediana, fechas no resueltas). Detalle completo y
diferenciado entre evidencia, interpretación y conclusión en
`notebooks/05_conclusiones.ipynb` y en `reports/informe_final.pdf`.
