import os
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit

df_escolasSP = pd.read_csv("escolas_2021_SP.csv", sep=',', encoding = "ascii")

df_escolasSP