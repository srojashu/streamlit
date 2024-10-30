import streamlit as st
import pandas as pd

st.title("Análisis de Datos de Educación en Colombia")

uploaded_file = st.file_uploader("Cargar archivo 'educacion.csv'", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Mostrar tabla de datos completa
    st.subheader("Datos Cargados")
    st.dataframe(df)

    # Sidebar para los filtros
    st.sidebar.header("Filtros")

    # Filtros
    nivel_educativo = st.sidebar.multiselect("Nivel educativo", df["Nivel educativo"].unique())
    carrera = st.sidebar.multiselect("Carrera", df["Carrera"].unique())
    institucion = st.sidebar.multiselect("Institución", df["Institución"].unique())

    # Filtrar el DataFrame según los filtros seleccionados
    df_filtrado = df.copy()
    if nivel_educativo:
        df_filtrado = df_filtrado[df_filtrado["Nivel educativo"].isin(nivel_educativo)]
    if carrera:
        df_filtrado = df_filtrado[df_filtrado["Carrera"].isin(carrera)]
    if institucion:
        df_filtrado = df_filtrado[df_filtrado["Institución"].isin(institucion)]

    # Mostrar el DataFrame filtrado
    st.subheader("Datos Filtrados")
    st.dataframe(df_filtrado)

    # Estadísticas descriptivas
    st.subheader("Estadísticas Descriptivas")
    st.write(df_filtrado.describe())

    # Conteo de estudiantes por nivel educativo
    st.subheader("Conteo de Estudiantes por Nivel Educativo")
    st.bar_chart(df_filtrado["Nivel educativo"].value_counts())

    # Distribución de la edad
    st.subheader("Distribución de la Edad")
    st.pyplot(df_filtrado["Edad"], bins=10)