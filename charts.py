import altair as alt
import pandas as pd

def bar_chart_mean_sleep_by_occupation(df):
    
    chart = alt.Chart(df).mark_bar().encode(
        x = alt.X("Occupation", title="Occupation", axis=alt.Axis(labelAngle=0, labelFontSize=0)),
        y = alt.Y("Sleep Duration", scale=alt.Scale(domain=[0, 10])),
        color = "Occupation"
    ).properties(
        title = "Média de Horas de Sono por Ocupação",
    ).configure_axis(
        labelFontSize= 20,
        titleFontSize = 20
    ).configure_legend(
        labelFontSize=16,   # Tamanho das opções (ex: profissões)
        titleFontSize=20    # Tamanho do título da legenda (se tiver)     
    ).configure_title(
        fontSize = 20,
        anchor = "start"
    )

    return chart


def bar_chart_mean_stress_level_occupation(df):

    chart = alt.Chart(df).mark_bar().encode(
        x = alt.X("Occupation", title="Occupation", axis=alt.Axis(labelAngle=0, labelFontSize=0)),
        y = alt.Y("Stress Level", scale=alt.Scale(domain=[0, 10])),
        color = "Occupation"
    ).properties(
        title = "Média de Nível de Estresse por Ocupação",
    ).configure_axis(
        labelFontSize= 20,
        titleFontSize = 20
    ).configure_legend(
        labelFontSize = 16,
        titleFontSize = 20
    ).configure_title(
        fontSize = 20,
        anchor = "start"
    )

    return chart

def bar_chart_mean_daily_steps(df):

    chart = alt.Chart(df).mark_bar().encode(
        x = alt.X("Occupation", title="Occupation", axis=alt.Axis(labelAngle=0, labelFontSize=0)),
        y = alt.Y("Daily Steps", scale=alt.Scale(domain=[0, 10000])),
        color = "Occupation"
    ).properties(
        title = "Média de Passos Diários por Ocupação"
    ).configure_axis(
        labelFontSize = 20,
        titleFontSize = 20
    ).configure_legend(
        labelFontSize = 16,
        titleFontSize = 20
    ).configure_title(
        fontSize = 20,
        anchor = "start"
    )

    return chart

def bar_chart_quality_sleep_by_occupation(df):
    
    chart = alt.Chart(df).mark_bar().encode(
        x = alt.X("Occupation", title="Occupation", axis=alt.Axis(labelAngle=0, labelFontSize=0)),
        y = alt.Y("Quality of Sleep", scale=alt.Scale(domain=[1, 10])),
        color = "Occupation"
    ).properties(
        title = "Média de Qualidade de Sono por Ocupação",
        width = 500,  # define uma largura menor para "empurrar" para direita (ajuste conforme necessário)
        padding = {"left": 15}  # define um padding à esquerda (isso nem sempre funciona em Streamlit)
    ).configure_axis(
        labelFontSize = 20,
        titleFontSize = 20
    ).configure_legend(
        labelFontSize = 16,
        titleFontSize = 20
    ).configure_title(
        fontSize = 20,
        anchor = "start"
    )

    return chart