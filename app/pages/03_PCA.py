import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

st.set_page_config(page_title="PCA", page_icon="🧭", layout="wide")
st.title("🧭 Escalamiento y PCA")


@st.cache_data
def cargar_y_calcular():
    df = pd.read_csv("data/processed/streaming_users_clean.csv")
    num_cols = ["age", "monthly_watch_time_mins", "customer_support_tickets"]
    X = df[num_cols]
    X_esc = StandardScaler().fit_transform(X)
    pca = PCA()
    componentes = pca.fit_transform(X_esc)
    return df, num_cols, pca, componentes


df, num_cols, pca, componentes = cargar_y_calcular()
varianza = pca.explained_variance_ratio_

st.markdown(f"""
**Variables utilizadas:** {", ".join(f"`{c}`" for c in num_cols)}.

**Escalamiento aplicado:** `StandardScaler` (media 0, desvío 1), necesario porque las
variables originales tienen unidades y rangos muy distintos.
""")

st.subheader("Varianza explicada por componente")
fig, ax = plt.subplots(figsize=(6, 3.5))
ax.bar([f"PC{i+1}" for i in range(len(varianza))], varianza, color="#4C72B0")
ax.set_ylabel("Proporción de varianza explicada")
st.pyplot(fig)

col1, col2, col3 = st.columns(3)
for i, col in enumerate([col1, col2, col3]):
    col.metric(f"PC{i+1}", f"{varianza[i]*100:.1f}%")

st.markdown("""**Interpretación:** las 3 componentes explican una proporción casi
idéntica de la varianza total (~33% cada una). Esto ocurre porque `age`,
`monthly_watch_time_mins` y `customer_support_tickets` están prácticamente
descorrelacionadas entre sí (ver notebook de EDA): cuando las variables originales son
independientes, PCA no logra concentrar la varianza en pocas componentes.""")

st.subheader("Usuarios proyectados en PC1 vs PC2")
fig, ax = plt.subplots(figsize=(7, 4.5))
colores = {"Básico": "#4C72B0", "Estándar": "#DD8452", "Premium": "#55A868"}
for plan, color in colores.items():
    mask = (df["subscription_plan"] == plan).values
    ax.scatter(componentes[mask, 0], componentes[mask, 1],
               alpha=0.3, s=10, label=plan, color=color)
ax.set_xlabel(f"PC1 ({varianza[0]*100:.1f}% var.)")
ax.set_ylabel(f"PC2 ({varianza[1]*100:.1f}% var.)")
ax.legend(title="Plan")
st.pyplot(fig)

st.markdown("""**Interpretación:** no se observan agrupamientos por plan de suscripción
en el espacio reducido. **Conclusión:** con estas 3 variables numéricas no conviene
reducir dimensionalidad — se necesitan las 3 componentes para conservar el 100% de la
información, un hallazgo válido en sí mismo del proyecto.""")
