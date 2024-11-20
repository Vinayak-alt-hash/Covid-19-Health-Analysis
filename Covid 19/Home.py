# Terminal -> cd Dashboard -> Enter
# streamlit run Home.py -> Enterimport streamlit as st
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import datetime

st.markdown(
    """
    <div style="
        background-color: Maroon; 
        border: 3px solid white; 
        border-radius: 10px; 
        padding: 10px; 
        text-align: center;
    ">
        <h1 style="color: white; font-weight: bold; margin: 0;">
            Covid-19
        </h1>
    </div>
    """, 
    unsafe_allow_html=True
)

st.image('assets\data_graph__virus_Adobe.jpg')

st.markdown('<h1 style="font-size:40px; font-weight:bold;">DESCRIPTION</h1>', unsafe_allow_html=True)
st.markdown('''Welcome to the COVID-19 Data Dashboard, an interactive platform designed to provide insights into the global impact of the COVID-19 pandemic. This dashboard presents real-time analysis and visualization of critical data points, helping you understand trends, patterns, and regional disparities in the spread and severity of the virus''')

st.markdown('''
            
Global Trends:   Monitor the progression of new cases and deaths worldwide over time.
            
Country Insights:   Identify the top 10 countries with the highest cases, deaths, and mortality rates.
            
Regional Analysis:   Explore COVID-19 statistics by WHO regions, showcasing variations in case distributions and trends.
            
Comparative Metrics:   Analyze relationships between new cases and new deaths globally to understand the pandemics dynamics.
            
Heatmaps & Visual Trends:   Examine the intensity of cases over time and across regions with visually intuitive heatmaps.
            
This project aims to support informed decision-making and awareness by leveraging data to highlight the key aspects of the pandemic. Whether you are a policymaker, researcher, or concerned individual, this dashboard offers valuable insights into the global fight against COVID-19.''')

st.image('assets\mask.jpg')
