import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="EDA", page_icon="📊", layout="wide")
st.title("📊 Análisis Exploratorio")

st.markdown("""
Se muestran a continuación **5 visualizaciones** (2 univariadas, 2 bivariadas y 1
multivariada), cada una con su interpretación. El desarrollo completo, con preguntas de
análisis y más detalle, está en `notebooks/03_eda.ipynb`.
""")


@st.cache_data
def cargar_datos():
    df = pd.read_csv("data/processed/streaming_users_clean.csv")
    df["last_login_date"] = pd.to_datetime(df["last_login_date"], errors="coerce")
    return df


df = cargar_datos()

# ---------- Univariado 1 ----------
st.header("1️⃣ Univariado — Distribución de la edad")
fig, ax = plt.subplots(figsize=(7, 3.5))
ax.hist(df["age"], bins=30, color="#4C72B0", edgecolor="white")
ax.set_xlabel("Edad")
ax.set_ylabel("Cantidad de usuarios")
st.pyplot(fig)
st.markdown("""**Interpretación:** la mayoría de los usuarios tiene entre 25 y 45 años.
La base de usuarios está compuesta principalmente por adultos jóvenes y de mediana edad.""")

# ---------- Univariado 2 ----------
st.header("2️⃣ Univariado — Distribución del consumo mensual")
fig, ax = plt.subplots(figsize=(7, 3.5))
ax.hist(df["monthly_watch_time_mins"], bins=40, color="#DD8452", edgecolor="white")
ax.set_xlabel("Minutos por mes")
ax.set_ylabel("Cantidad de usuarios")
st.pyplot(fig)
st.markdown("""**Interpretación:** el consumo mensual tiene una distribución asimétrica
hacia la derecha — la mayoría consume un rango moderado de minutos, pero hay un grupo de
usuarios con consumo muy por encima del resto.""")

# ---------- Bivariado 1 ----------
st.header("3️⃣ Bivariado — Consumo mensual según plan de suscripción")
fig, ax = plt.subplots(figsize=(7, 4))
data_por_plan = [df.loc[df["subscription_plan"] == p, "monthly_watch_time_mins"]
                 for p in ["Básico", "Estándar", "Premium"]]
ax.boxplot(data_por_plan, labels=["Básico", "Estándar", "Premium"])
ax.set_ylabel("Minutos por mes")
st.pyplot(fig)
medianas = df.groupby("subscription_plan")["monthly_watch_time_mins"].median().reindex(
    ["Básico", "Estándar", "Premium"])
st.markdown(f"""**Interpretación:** las medianas de consumo crecen con el nivel del
plan (Básico {medianas['Básico']:.0f} min, Estándar {medianas['Estándar']:.0f} min,
Premium {medianas['Premium']:.0f} min). Existe una asociación agregada entre plan y
consumo, aunque con alta dispersión dentro de cada plan.""")

# ---------- Bivariado 2 ----------
st.header("4️⃣ Bivariado — Consumo promedio según país")
consumo_pais = df.groupby("country")["monthly_watch_time_mins"].mean().sort_values(ascending=False)
consumo_pais = consumo_pais[consumo_pais.index != "Desconocido"]
fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(consumo_pais.index, consumo_pais.values, color="#64B5CD")
ax.set_ylabel("Minutos por mes (promedio)")
plt.xticks(rotation=30)
st.pyplot(fig)
st.markdown("""**Interpretación:** el consumo promedio es relativamente homogéneo entre
países (sin un país que se destaque marcadamente), lo que sugiere que la geografía no es
un factor determinante del nivel de consumo en esta base de usuarios.""")

# ---------- Multivariado ----------
st.header("5️⃣ Multivariado — Edad vs. consumo, por plan de suscripción")
fig, ax = plt.subplots(figsize=(7, 4.5))
colores = {"Básico": "#4C72B0", "Estándar": "#DD8452", "Premium": "#55A868"}
for plan, color in colores.items():
    subset = df[df["subscription_plan"] == plan]
    ax.scatter(subset["age"], subset["monthly_watch_time_mins"],
               alpha=0.3, s=10, label=plan, color=color)
ax.set_xlabel("Edad")
ax.set_ylabel("Minutos de consumo mensual")
ax.legend(title="Plan")
st.pyplot(fig)
st.markdown("""**Interpretación:** dentro de cada rango de edad los tres planes están
mezclados, es decir, la asociación plan–consumo encontrada arriba **no está mediada por
la edad**: ocurre de forma pareja en todos los rangos etarios.""")
