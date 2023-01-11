import pandas as pd
import plotly.express as px
import streamlit as st

df_escolasSP = pd.read_csv("escolas_2021_SP.csv", sep=',', encoding = "ascii")

st.title('Escolas de São Paulo color:green[2021] :sunglasses:')

temp = df_escolasSP.dropna(subset=['QT_DESKTOP_ALUNO'])
temp = temp[temp['QT_DESKTOP_ALUNO']!=88888]
temp = temp[temp['QT_DESKTOP_ALUNO']!=0]

fig = px.scatter_mapbox(temp, lat='Latitude', lon='Longitude', size='QT_DESKTOP_ALUNO',
                        center=dict(lat=-23.55, lon=-46.6), zoom=9.5,
                        mapbox_style="stamen-terrain", hoverinfo='text', hover_name='NO_ENTIDADE', hover_data=['QT_MAT_BAS_11_14','QT_MAT_BAS_15_17'])


st.plotly_chart(fig, use_container_width=False, sharing="streamlit", theme="streamlit")
st.caption('O mapa mostra a quantidade de desktop que tem cada escola. O tamanho da bolha representa a quantidade de desktops.')
st.caption('QT_MAT_BAS_11_14 representa o número de Matrículas na Educação Básica entre 11 e 14 anos de idade')
st.caption('QT_MAT_BAS_15_17 representa o número de Matrículas na Educação Básica entre 15 e 17 anos de idade')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')


st.text('Dados do Censo Escolar 2021')
df_escolasSP