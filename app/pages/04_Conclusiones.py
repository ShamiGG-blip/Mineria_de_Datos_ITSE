import streamlit as st

st.set_page_config(page_title="Conclusiones", page_icon="✅", layout="wide")
st.title("✅ Conclusiones")

st.markdown("""
### Hallazgos principales

- El plan de suscripción se asocia, en promedio, a un mayor consumo mensual
  (Básico < Estándar < Premium), aunque con alta dispersión individual dentro de cada
  plan.
- Esa asociación **no está mediada por la edad**: ocurre de forma pareja en todos los
  rangos etarios.
- La cantidad de tickets de soporte no muestra relación clara con el plan ni con la
  edad del usuario.
- El país de origen no presenta diferencias relevantes de consumo.
- Las tres variables numéricas del dataset (edad, consumo, tickets) están
  prácticamente descorrelacionadas entre sí, por lo que PCA no logra una reducción de
  dimensionalidad eficiente (varianza repartida ~33% entre sus 3 componentes).

### Limitaciones

- Los valores imputados por mediana (edad, consumo y tickets fuera de rango) reducen la
  varianza real de esas variables.
- Cerca del 6% de los registros finales no cuentan con fecha de último login válida.
- Ante usuarios duplicados con datos distintos, se conservó el primer registro
  observado, sin evidencia disponible para determinar cuál era el correcto.
- El alcance de las conclusiones está condicionado por la información disponible y por
  las decisiones documentadas durante el proceso.

### Próximos pasos

- Incorporar variables adicionales (antigüedad de cuenta, dispositivo, cantidad de
  perfiles) que ayuden a explicar mejor el comportamiento de uso.
- Explorar un PCA que incluya variables categóricas codificadas.
- Sumar la fecha de alta del usuario para poder analizar retención en el tiempo.

---

📄 Informe técnico completo: `reports/informe_final.pdf`
📓 Notebooks: `notebooks/`
🔗 Repositorio: _[completar enlace público al repositorio]_
""")
