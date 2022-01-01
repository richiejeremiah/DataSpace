import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

df = pd.read_csv("DataSpace.csv")

def load_data(filename):
    data_f = pd.read_csv(filename, index_col=0)
    return data_f


def summary_poster(df_diagnosis, color_dict):
    #Scatter Plot
    fig = px.scatter(
                df_diagnosis,
                x ="Diagnosis",
                y= "Outcome",
                size="Age",
                color="Year"
    )
    return fig