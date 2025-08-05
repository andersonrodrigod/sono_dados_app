import streamlit as st
import pandas as pd


st.title("Análise de Dados de Sono")

df = pd.read_csv("sleep.csv")

st.subheader("Visualização de Tabela")
st.dataframe(df)

st.subheader("Resumo Estatístico")
st.write(df.describe())

ocupacoes = df["Occupation"].unique()
ocupacao_selecionada = st.selectbox("Filtrar por ocupação",  ocupacoes)
df_filtrado = df[df["Occupation"] == ocupacao_selecionada]

st.write(f"Exibindo registros da ocupação: {ocupacao_selecionada}")
st.dataframe(df_filtrado)


















