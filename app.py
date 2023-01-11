import pandas as pd
import plotly.express as px
import streamlit as st

df_escolasSP = pd.read_csv("escolas_2021_SP.csv", sep=',', encoding = "ascii")

st.title('Escolas de São Paulo 2021 :sunglasses:')

tab1, tab2, tab3 = st.tabs(["Desktops", "Comp Portatil", "Matriculas 11-14"])

with tab1:
    st.header("Número de Desktops")
   
    temp1 = df_escolasSP.dropna(subset=['QT_DESKTOP_ALUNO'])
    temp1 = temp1[temp1['QT_DESKTOP_ALUNO']!=88888]
    temp1 = temp1[temp1['QT_DESKTOP_ALUNO']!=0]

    fig1 = px.scatter_mapbox(temp1, lat='Latitude', lon='Longitude', size='QT_DESKTOP_ALUNO',
                        center=dict(lat=-23.55, lon=-46.6), zoom=9.5,
                        mapbox_style="stamen-terrain",  hover_name='NO_ENTIDADE', hover_data=dict(QT_MAT_BAS_11_14=True,
                                    QT_MAT_BAS_15_17=True, 
                                    Latitude=False, 
                                    Longitude=False))
    fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    st.plotly_chart(fig1, use_container_width=True, sharing="streamlit", theme=None)
    st.caption('O mapa mostra a quantidade de desktop que tem cada escola. O tamanho da bolha representa a quantidade de desktops.')
    st.caption('QT_MAT_BAS_11_14 representa o número de Matrículas na Educação Básica entre 11 e 14 anos de idade')
    st.caption('QT_MAT_BAS_15_17 representa o número de Matrículas na Educação Básica entre 15 e 17 anos de idade')

with tab2:
    st.header("Número de Computadores Portateis")
   
    temp2 = df_escolasSP.dropna(subset=['QT_COMP_PORTATIL_ALUNO'])
    temp2 = temp2[temp2['QT_COMP_PORTATIL_ALUNO']!=88888]
    temp2 = temp2[temp2['QT_COMP_PORTATIL_ALUNO']!=0]

    fig2 = px.scatter_mapbox(temp2, lat='Latitude', lon='Longitude', size='QT_COMP_PORTATIL_ALUNO',
                        center=dict(lat=-23.55, lon=-46.6), zoom=9.5,
                        mapbox_style="stamen-terrain",  hover_name='NO_ENTIDADE', hover_data=dict(QT_MAT_BAS_11_14=True,
                                    QT_MAT_BAS_15_17=True, 
                                    Latitude=False, 
                                    Longitude=False))
    fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    st.plotly_chart(fig2, use_container_width=True, sharing="streamlit", theme=None)
    st.caption('O mapa mostra a quantidade de desktop que tem cada escola. O tamanho da bolha representa a quantidade de desktops.')
    st.caption('QT_MAT_BAS_11_14 representa o número de Matrículas na Educação Básica entre 11 e 14 anos de idade')
    st.caption('QT_MAT_BAS_15_17 representa o número de Matrículas na Educação Básica entre 15 e 17 anos de idade')

with tab3:
    st.header("Matriculas 11-14")

    fig3 = px.scatter_mapbox(df_escolasSP, lat='Latitude', lon='Longitude', size='QT_MAT_BAS_11_14',
                        center=dict(lat=-23.55, lon=-46.6), zoom=9.5,
                        mapbox_style="stamen-terrain",  hover_name='NO_ENTIDADE', hover_data=dict(
                                    QT_MAT_BAS_15_17=True, 
                                    Latitude=False, 
                                    Longitude=False))
    fig3.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    st.plotly_chart(fig3, use_container_width=True, sharing="streamlit", theme=None)
    st.caption('O mapa mostra a quantidade de desktop que tem cada escola. O tamanho da bolha representa a quantidade de desktops.')
    st.caption('QT_MAT_BAS_11_14 representa o número de Matrículas na Educação Básica entre 11 e 14 anos de idade')
    st.caption('QT_MAT_BAS_15_17 representa o número de Matrículas na Educação Básica entre 15 e 17 anos de idade')



#st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')
st.text('Dados do Censo Escolar 2021')
df_escolasSP