import pandas as pd
import plotly.express as px
import streamlit as st

df_escolasSP = pd.read_csv("escolas_2021_SP.csv", sep=',', encoding = "ascii")

st.title('Escolas de São Paulo 2021 :sunglasses:')

tab1, tab2, tab3 = st.tabs(["Desktops", "Comp Portatil", "Matriculas 11-14"])

with tab1:
   st.header("Número de Desktops")
   
temp = df_escolasSP.dropna(subset=['QT_DESKTOP_ALUNO'])
temp = temp[temp['QT_DESKTOP_ALUNO']!=88888]
temp = temp[temp['QT_DESKTOP_ALUNO']!=0]

fig = px.scatter_mapbox(temp, lat='Latitude', lon='Longitude', size='QT_DESKTOP_ALUNO',
                        center=dict(lat=-23.55, lon=-46.6), zoom=9.5,
                        mapbox_style="stamen-terrain",  hover_name='NO_ENTIDADE', hover_data=dict(QT_MAT_BAS_11_14=True,
                                    QT_MAT_BAS_15_17=True, 
                                    Latitude=False, 
                                    Longitude=False))
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme=None)
st.caption('O mapa mostra a quantidade de desktop que tem cada escola. O tamanho da bolha representa a quantidade de desktops.')
st.caption('QT_MAT_BAS_11_14 representa o número de Matrículas na Educação Básica entre 11 e 14 anos de idade')
st.caption('QT_MAT_BAS_15_17 representa o número de Matrículas na Educação Básica entre 15 e 17 anos de idade')

with tab2:
   st.header("Número de Computadores Portateis")
   
temp = df_escolasSP.dropna(subset=['QT_COMP_PORTATIL_ALUNO'])
temp = temp[temp['QT_COMP_PORTATIL_ALUNO']!=88888]
temp = temp[temp['QT_COMP_PORTATIL_ALUNO']!=0]

fig = px.scatter_mapbox(temp, lat='Latitude', lon='Longitude', size='QT_COMP_PORTATIL_ALUNO',
                        center=dict(lat=-23.55, lon=-46.6), zoom=9.5,
                        mapbox_style="stamen-terrain",  hover_name='NO_ENTIDADE', hover_data=dict(QT_MAT_BAS_11_14=True,
                                    QT_MAT_BAS_15_17=True, 
                                    Latitude=False, 
                                    Longitude=False))
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme=None)
st.caption('O mapa mostra a quantidade de desktop que tem cada escola. O tamanho da bolha representa a quantidade de desktops.')
st.caption('QT_MAT_BAS_11_14 representa o número de Matrículas na Educação Básica entre 11 e 14 anos de idade')
st.caption('QT_MAT_BAS_15_17 representa o número de Matrículas na Educação Básica entre 15 e 17 anos de idade')

with tab3:
   st.header("Matriculas 11-14")

fig = px.scatter_mapbox(df_escolasSP, lat='Latitude', lon='Longitude', size='QT_MAT_BAS_11_14',
                        center=dict(lat=-23.55, lon=-46.6), zoom=9.5,
                        mapbox_style="stamen-terrain",  hover_name='NO_ENTIDADE', hover_data=dict(QT_MAT_BAS_11_14=True,
                                    QT_MAT_BAS_15_17=True, 
                                    Latitude=False, 
                                    Longitude=False))
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme=None)
st.caption('O mapa mostra a quantidade de desktop que tem cada escola. O tamanho da bolha representa a quantidade de desktops.')
st.caption('QT_MAT_BAS_11_14 representa o número de Matrículas na Educação Básica entre 11 e 14 anos de idade')
st.caption('QT_MAT_BAS_15_17 representa o número de Matrículas na Educação Básica entre 15 e 17 anos de idade')



#st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')


st.text('Dados do Censo Escolar 2021')
df_escolasSP