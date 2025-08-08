import streamlit as st
from data import load_data, mean_sleep_by_occupation, mean_stress_by_occupation, mean_daily_steps_by_occupation, mean_quality_sleep_by_occupation
from charts import bar_chart_mean_sleep_by_occupation, bar_chart_mean_stress_level_occupation, bar_chart_mean_daily_steps, bar_chart_quality_sleep_by_occupation


st.set_page_config(layout="wide")

st.title("Análise de Dados de Sono")

df = load_data("sleep.csv")



pagina = st.sidebar.selectbox("Escolha o tipo de gráfico", [
    "Gráfico de Barra",
    "Gráfico de Linha",
    "Gráficos de Dispersão",
    "Gráficos de Pizza"
])

if pagina == "Gráfico de Barra":
    st.title("Gráficos de Barra")

    media_sono = mean_sleep_by_occupation(df)
    media_stress = mean_stress_by_occupation(df)
    media_daily_steps = mean_daily_steps_by_occupation(df)
    media_quality_sleep = mean_quality_sleep_by_occupation(df)

    chart_media_stress = bar_chart_mean_stress_level_occupation(media_stress)
    chart_media_sono = bar_chart_mean_sleep_by_occupation(media_sono) 
    chart_media_daily_steps = bar_chart_mean_daily_steps(media_daily_steps)
    chart_media_quality_sleep = bar_chart_quality_sleep_by_occupation(media_quality_sleep)

    col1, spacer, col2 = st.columns([1, 0.1, 1])

    with col1:
        st.altair_chart(chart_media_sono, use_container_width=True)
        st.altair_chart(chart_media_quality_sleep, use_container_width=True)

    with col2:
        st.altair_chart(chart_media_stress, use_container_width=True)
        st.altair_chart(chart_media_daily_steps, use_container_width=True)
        
    
    st.dataframe(media_sono, use_container_width=True)


"""st.subheader("Visualização de Tabela")
st.dataframe(df)

st.subheader("Resumo Estatístico")
st.write(df.describe())

ocupacoes = df["Occupation"].unique()
ocupacao_selecionada = st.selectbox("Filtrar por ocupação",  ocupacoes)
df_filtrado = df[df["Occupation"] == ocupacao_selecionada]

st.write(f"Exibindo registros da ocupação: {ocupacao_selecionada}")
st.dataframe(df_filtrado)

"""
















