import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dataset", page_icon="📦", layout="wide")
st.title("📦 El Dataset")


@st.cache_data
def cargar_datos():
    df = pd.read_csv("data/processed/streaming_users_clean.csv")
    log = pd.read_csv("logs/pipeline_log.csv")
    return df, log


df, log = cargar_datos()

st.markdown("""
### Descripción general

El dataset original contiene registros de usuarios de una plataforma de streaming, con
las siguientes variables: identificador de usuario, edad, plan de suscripción, minutos
de consumo mensual, país, género favorito, fecha de último login y cantidad de tickets
de soporte generados.
""")

col1, col2, col3 = st.columns(3)
col1.metric("Usuarios (dataset final)", f"{len(df):,}")
col2.metric("Columnas", df.shape[1])
col3.metric("Retención tras limpieza", f"{log['Retención (%)'].iloc[-1]}%")

st.markdown("### Resumen breve de calidad")
st.markdown("""
El dataset original presentaba, entre otros problemas: valores faltantes explícitos,
filas y usuarios duplicados, edades y minutos de consumo fuera de rango plausible,
códigos centinela de error (ej. tickets de soporte = 99 o 150), categorías escritas de
formas inconsistentes (mayúsculas, tildes, abreviaturas, inglés) y fechas de login en
múltiples formatos. El detalle completo de la inspección está en
`notebooks/01_inspeccion_inicial.ipynb`.
""")

st.markdown("### Vista previa del dataset procesado")
st.dataframe(df.head(20), use_container_width=True)

st.markdown("### Transformaciones principales aplicadas")
st.dataframe(log[["Paso", "Descripción", "Retención (%)"]], use_container_width=True)

st.caption("Detalle completo y justificación de cada decisión: "
           "`notebooks/02_calidad_y_limpieza.ipynb` y `logs/pipeline_log.csv`.")
