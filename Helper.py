import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots

df = pd.read_csv("DataSpace.csv")
color_map_df = pd.read_csv("sheet.csv")

def load_data(filename):
    data_f = pd.read_csv(filename, index_col=0)
    return data_f


def summary_poster(gion_df, color_dict):
    color_map_df = pd.read_csv("sheet.csv")
    fig = make_subplots(
        rows=2, cols=2, 
        column_widths=[0.4, 0.6],
        specs=[[{"type": "Sunburst"}, {"type": "bar"}], 
            [{"type":"scatter", "colspan": 2}, None]],
            subplot_titles=('Age at Diagnosis', 
                            'Temperature Distribution ', 
                            'Scatter Plot'),
            vertical_spacing=0.1, horizontal_spacing= 0.09)

    #PIE
    #data for pie
    pie_data = gion_df.groupby('Age')['Sex'].count()

    fig.add_trace(go.Pie(labels = pie_data.index,
                            values = pie_data.values,
                            hole = 0.4,
                            legendgroup = 'grp1',
                            showlegend=False),
                row = 1, col = 1)
    fig.update_traces(hoverinfo = 'label+percent',
                        textinfo = 'value+percent',
                        textfont_color = 'white',
                        marker = dict(colors = pie_data.index.map(color_dict),
                                    line=dict(color='white', width=1)),
                        row = 1, col = 1)

    #plot params
    fig.add_trace(go.Bar(x=gion_df['Month'],
                    y= gion_df['Highest Temperature'],
                    marker_color='rgb(55, 83, 109)'),                         
                    row = 1, col = 2)
    
    fig.update_yaxes(title_text = 'Count',linecolor = 'grey', mirror = True, 
                        title_standoff = 0, gridcolor = 'grey', gridwidth = 0.1,
                        zeroline = False,)
    #SCATTER
    fig.add_trace(go.Scatter(
                x=gion_df['Age'],
                y=gion_df['Highest Temperature'],
                mode = 'markers',
                marker=dict(color="DarkOrange"),
                ),
                row = 2, col = 1
                )

    fig.update_layout( # customize font and margins
                        width=1200,
                        height=800,
                        margin = dict(l = 40, t = 40, r = 40, b = 40)
                    )
    
    return fig
