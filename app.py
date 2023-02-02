import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

df_escolasSP = pd.read_csv("escolas_2021_SP.csv", sep=',', encoding = "utf-8")

st.title('Escolas de São Paulo 2021 :sunglasses:')

tab1, tab2, tab3 = st.tabs(["Comps/Aluno", "Comp Portatil", "Matriculas 11-14"])

with tab1:
    st.header("Número de Computadores por Aluno")
    
    temp1 = df_escolasSP.dropna(subset=['STUDENTS_11_17'])
    temp1 = temp1[temp1['STUDENTS_11_17']!=0]

    mapbox_access_token = open("TUMO.mapbox_token").read()

    fig1 = go.Figure(
                go.Scattermapbox(
                lat=temp1["Latitude"],
                lon = temp1['Longitude'],
                mode='markers',
                text=temp1['NO_ENTIDADE'],
                showlegend=False,
                customdata= temp1['STUDENTS_11_17'],
                hovertemplate='Escola:  %{text} <br>' +
                            'Alunos: %{customdata} <br>' +
                            'Comps/Aluno: %{marker.color:.00%}' + '<extra></extra>',
                marker=go.scattermapbox.Marker(
                sizemode='area',
                sizemin=3,
                sizeref=2.*temp1['STUDENTS_11_17'].max()/(35.**2),
                size=temp1['STUDENTS_11_17'],
                color=temp1['COMPS_PER_STUDENT'],
                cmax=1,
                cmin=0,
                colorbar=dict(
                title="Comp/Aluno"
            ),
            colorscale="portland")
        
            ))


    fig1.update_layout(mapbox=dict(
            accesstoken=mapbox_access_token,
            style="outdoors",
            center=dict(
                lat=-23.55,
                lon=-46.6), zoom=10),margin={"r":0,"t":0,"l":0,"b":0},)

    fig1.add_trace(go.Scattermapbox(
            lat=[-23.557162590546906, -23.559738635227205],
            lon=[-46.68954674702313, -46.69842457794723],
            mode='markers+text',
            showlegend=False,
            marker={'size':10, 'symbol':['star','star']},
            text = ["42", "TUMO",],textposition = "bottom right"
            
    ))


    st.plotly_chart(fig1, use_container_width=True, sharing="streamlit", theme=None)
    st.caption('O mapa mostra a quantidade de desktop que tem cada escola. O tamanho da bolha representa a quantidade de desktops.')
    st.caption('Comps/Aluno é o total de (Desktops + Tablets) divido por matrículas na Educação Básica entre 11 e 17 anos de idade')
    

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
    temp3 = df_escolasSP.dropna(subset=['QT_MAT_BAS_15_17'])

    mapbox_access_token = open("TUMO.mapbox_token").read()

    fig3 = go.Figure(
                go.Scattermapbox(
                lat=temp3["Latitude"],
                lon = temp3['Longitude'],
                showlegend=False,
                mode='markers',
                marker=go.scattermapbox.Marker(
                size=temp3['QT_MAT_BAS_15_17']*25/(temp3['QT_MAT_BAS_15_17'].max())
            ),
    ))


    fig3.update_layout(mapbox=dict(
            accesstoken=mapbox_access_token,
            center=dict(
                lat=-23.55,
                lon=-46.6), zoom=10))

    fig3.add_trace(go.Scattermapbox(
            lat=[-23.557162590546906, -23.559738635227205],
            lon=[-46.68954674702313, -46.69842457794723],
            showlegend=False,
            mode='markers+text',
            marker={'size':10, 'symbol':['star','star']},
            text = ["42", "TUMO",],textposition = "bottom right"
            
    ))
    
    fig3.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    st.plotly_chart(fig3, use_container_width=True, sharing="streamlit", theme=None)
    st.caption('O mapa mostra a quantidade de desktop que tem cada escola. O tamanho da bolha representa a quantidade de desktops.')
    st.caption('QT_MAT_BAS_11_14 representa o número de Matrículas na Educação Básica entre 11 e 14 anos de idade')
    st.caption('QT_MAT_BAS_15_17 representa o número de Matrículas na Educação Básica entre 15 e 17 anos de idade')

    # st.header("Matriculas 11-14")

    # temp3 = df_escolasSP.dropna(subset=['QT_MAT_BAS_11_14'])
    
    # fig3 = px.scatter_mapbox(temp3, lat='Latitude', lon='Longitude', size='QT_MAT_BAS_11_14',
    #                     center=dict(lat=-23.55, lon=-46.6), zoom=9.5,
    #                     mapbox_style="stamen-terrain",  hover_name='NO_ENTIDADE', hover_data=dict(
    #                                 QT_MAT_BAS_15_17=True, 
    #                                 Latitude=False, 
    #                                 Longitude=False))
    # fig3.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    # st.plotly_chart(fig3, use_container_width=True, sharing="streamlit", theme=None)
    # st.caption('O mapa mostra a quantidade de desktop que tem cada escola. O tamanho da bolha representa a quantidade de desktops.')
    # st.caption('QT_MAT_BAS_11_14 representa o número de Matrículas na Educação Básica entre 11 e 14 anos de idade')
    # st.caption('QT_MAT_BAS_15_17 representa o número de Matrículas na Educação Básica entre 15 e 17 anos de idade')



#st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')



st.text('Dados do Censo Escolar 2021')
df_escolasSP