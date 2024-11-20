import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import datetime

df = pd.read_csv("Covid Data.csv")

st.title("Covid-19 Dashboard")

# Ensure Date_reported is in datetime format
df['Date_reported'] = pd.to_datetime(df['Date_reported'], format='mixed')

fig1 = px.line(
    df.groupby('Date_reported', as_index=False)['New_cases'].sum(),
    x='Date_reported',
    y='New_cases',
    title='Global Trends of New Cases Over Time',
    labels={'New_cases': 'New Cases', 'Date_reported': 'Date'}
)
st.plotly_chart(fig1)
st.markdown('''Global Trends of New Cases:

This line chart shows the progression of new COVID-19 cases globally over time. It highlights major spikes or declines, reflecting changes in the pandemic's intensity due to events like public health measures, variants, or vaccination campaigns''')
top_countries = df.groupby('Country', as_index=False)['Cumulative_cases'].max().nlargest(10, 'Cumulative_cases')
fig2 = px.bar(
    top_countries,
    x='Cumulative_cases',
    y='Country',
    orientation='h',
    title='Top 10 Countries by Cumulative Cases',
    labels={'Cumulative_cases': 'Cumulative Cases', 'Country': 'Country'}
)
st.plotly_chart(fig2)
st.markdown('''Countries by Cumulative Cases:

A bar chart ranking the 10 countries with the highest cumulative COVID-19 cases. It emphasizes the countries most impacted by the pandemic in terms of total reported infections.''')

fig3 = px.scatter(
    df,
    x='New_cases',
    y='New_deaths',
    title='New Cases vs. New Deaths Globally',
    labels={'New_cases': 'New Cases', 'New_deaths': 'New Deaths'},
    hover_name='Country',
    color='WHO_region'
)
st.plotly_chart(fig3)
st.markdown('''New Cases vs. New Deaths Globally:

A scatter plot comparing the daily new cases and deaths across countries. It reveals the relationship between infection rates and mortality, with trends differing based on healthcare infrastructure, demographics, and pandemic stages.''')

fig4 = px.area(
    df.groupby('Date_reported', as_index=False)['Cumulative_deaths'].sum(),
    x='Date_reported',
    y='Cumulative_deaths',
    title='Cumulative Deaths Over Time',
    labels={'Cumulative_deaths': 'Cumulative Deaths', 'Date_reported': 'Date'}
)
st.plotly_chart(fig4)
st.markdown('''Cumulative Deaths Over Time:

This line chart illustrates the cumulative COVID-19 deaths globally, showing how mortality numbers have grown over time, often paralleling infection surges.''')

region_data = df.groupby('WHO_region', as_index=False)['Cumulative_cases'].sum()
fig5 = px.pie(
    region_data,
    names='WHO_region',
    values='Cumulative_cases',
    title='Distribution of Cases by WHO Region',
    labels={'Cumulative_cases': 'Cumulative Cases'}
)
st.plotly_chart(fig5)
st.markdown('''Distribution of Cases by WHO Region:

A pie or bar chart displaying the proportion of cases attributed to each WHO region. It provides insights into regional disparities in COVID-19 impact.''')

top_countries_cases = df.groupby('Country', as_index=False)['Cumulative_cases'].max().nlargest(5, 'Cumulative_cases')
filtered_data = df[df['Country'].isin(top_countries_cases['Country'])]
fig6 = px.line(
    filtered_data,
    x='Date_reported',
    y='New_cases',
    color='Country',
    title='Country-Wise Trend of New Cases',
    labels={'New_cases': 'New Cases', 'Date_reported': 'Date'}
)
st.plotly_chart(fig6)
st.markdown('''Country-Wise Trend of New Cases
A multi-line chart that tracks daily new cases for specific countries, allowing comparisons of infection trends and pandemic management strategies across nations.''')


df['Mortality_rate'] = (df['Cumulative_deaths'] / df['Cumulative_cases']) * 100
mortality_data = df.groupby('Country', as_index=False)['Mortality_rate'].max().nlargest(10, 'Mortality_rate')
fig7 = px.bar(
    mortality_data,
    x='Mortality_rate',
    y='Country',
    orientation='h',
    title='Top 10 Countries by Mortality Rate',
    labels={'Mortality_rate': 'Mortality Rate (%)', 'Country': 'Country'}
)
st.plotly_chart(fig7)
st.markdown('''Top 10 Countries by Mortality Rate:

A bar chart showing the 10 countries with the highest COVID-19 mortality rates (cumulative deaths per cumulative cases). It underscores the severity of the pandemic in terms of fatality in different regions.''')

heatmap_data = df.groupby(['Date_reported', 'WHO_region'], as_index=False)['New_cases'].sum()
fig8 = px.density_heatmap(
    heatmap_data,
    x='Date_reported',
    y='WHO_region',
    z='New_cases',
    title='Heatmap of Cases by Date and WHO Region',
    labels={'New_cases': 'New Cases', 'Date_reported': 'Date', 'WHO_region': 'WHO Region'},
    color_continuous_scale='Viridis'
)
st.plotly_chart(fig8)
st.markdown('''Heatmap of Cases by Date and WHO Region
A heatmap visualizing the intensity of new COVID-19 cases by date and WHO region. It provides a clear picture of when and where the pandemic peaked.''')

latest_date = df['Date_reported'].max()
latest_data = df[df['Date_reported'] == latest_date]
top_new_cases = latest_data.nlargest(10, 'New_cases')
fig9 = px.bar(
    top_new_cases,
    x='New_cases',
    y='Country',
    orientation='h',
    title='Top 10 Countries by New Cases',
    labels={'New_cases': 'New Cases', 'Country': 'Country'}
)
st.plotly_chart(fig9)
st.markdown('''Top 10 Countries by New Cases
A bar chart ranking the 10 countries reporting the highest daily new cases on a particular day, spotlighting the most immediate hotspots of the pandemic.''')

global_data = df.groupby('Date_reported', as_index=False).sum()
fig10 = go.Figure()
fig10.add_trace(go.Scatter(x=global_data['Date_reported'], y=global_data['Cumulative_cases'], mode='lines', name='Cumulative Cases'))
fig10.add_trace(go.Scatter(x=global_data['Date_reported'], y=global_data['Cumulative_deaths'], mode='lines', name='Cumulative Deaths'))
fig10.update_layout(
    title='Global Cumulative Cases vs. Cumulative Deaths',
    xaxis_title='Date',
    yaxis_title='Count',
    legend_title='Metric'
)
st.plotly_chart(fig10)
st.markdown('''Global Cumulative Cases vs. Cumulative Deaths
A dual-axis line chart comparing global cumulative cases and deaths over time, illustrating the pandemic's overall trajectory and highlighting the case fatality rate.''')

st.sidebar.header("Filter options")

selected_date = st.sidebar.slider( 'Select Date Range', int(df['Date_reported'].min(), int(df['Date_reported'].max())))

