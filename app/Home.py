import streamlit as st

st.set_page_config(
    page_title="Streaming Users — Proyecto Integrador",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Análisis de Usuarios de una Plataforma de Streaming")

st.markdown("""
### Proyecto Integrador — Minería de Datos 1

**Integrantes:** _[Nombre Apellido 1] — [Nombre Apellido 2]_
**Comisión:** _[completar comisión]_
**Fecha:** Julio 2026

---

### Contexto

Esta aplicación comunica, para público general, los resultados del análisis realizado
sobre un dataset de usuarios de una plataforma de streaming (`streaming_users_dirty.json`),
que incluye edad, plan de suscripción, tiempo de consumo mensual, país, género favorito,
fecha de último login y tickets de soporte.

El análisis técnico completo — inspección, limpieza documentada, análisis exploratorio y
reducción de dimensionalidad (PCA) — se encuentra en los notebooks del repositorio.
Esta app resume esos resultados con un enfoque visual e interactivo, sin reemplazar la
evidencia técnica.

**Navegá las secciones desde el menú de la izquierda:**
- **Dataset:** de qué se trata el dataset y qué tan "limpio" estaba.
- **EDA:** principales patrones encontrados en el análisis exploratorio.
- **PCA:** resultado del escalamiento y la reducción de dimensionalidad.
- **Conclusiones:** hallazgos, limitaciones y próximos pasos.

---

🔗 **Repositorio de GitHub:** _[completar enlace público al repositorio]_
""")
