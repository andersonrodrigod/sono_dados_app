import altair as alt


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


def line_chart_sleep_quality_stress(df_grouped):
    df_long = df_grouped.melt(
        id_vars=["Age"],
        value_vars=["Sleep Duration", "Quality of Sleep", "Stress Level"],
        var_name="Metric",
        value_name="Value"
    )

    chart = alt.Chart(df_long).mark_line(point=True).encode(
        x = alt.X("Age:Q", title="Idade"),
        y = alt.Y("Value:Q", title="Valor"),
        color= alt.Color("Metric:N", title="Métrica"),
        tooltip=["Age", "Metric", "Value"]
    ).properties(
        title="Evolução de Sono e Estresse por Idade",
        width=600,
        height=400
    )


    return chart


def line_chart_metrics_by_occupation(df_grouped):
    df_long = df_grouped.melt(
        id_vars=["Occupation"],
        value_vars=["Sleep Duration", "Quality of Sleep", "Stress Level"],
        var_name="Metric",
        value_name="Value"
    )

    chart = alt.Chart(df_long).mark_line(point=True).encode(
        x = alt.X("Occupation:N", title="Profissão", axis=alt.Axis(labelAngle=360)),
        y = alt.Y("Value:Q", title="Valor"),
        color = alt.Color("Metric:N", title="Métrica"),
        tooltip= ["Occupation", "Metric", "Value"]
    ).properties(
        title = "Evolução do Sono e Estressse por Profissão",
        height = 400,
        width = 600
    )

    return chart

def line_chart_metrics_by_bmi(df_grouped):
    df_long = df_grouped.melt(
        id_vars=["BMI Category"],
        value_vars=["Sleep Duration", "Quality of Sleep", "Stress Level"],
        var_name="Metric",
        value_name="Value"
    )

    chart = alt.Chart(df_long).mark_line(point=True).encode(
        x = alt.X("BMI Category:N", title="Nível de IMC", axis=alt.Axis(labelAngle=360)),
        y = alt.Y("Value:Q", title="Valor"),
        color = alt.Color("Metric:N", title="Métrica"),
        tooltip = ["BMI Category", "Metric", "Value"]
    ).properties(
        title = "Evolução do Sono e Estresse por Categoria de IMC",
        width = 600,
        height = 400
    )

    return chart