
import streamlit as st
import plotly.express as px
import pandas as pd

# Incorporate data
df = pd.read_csv('canadian_immegration_data.csv')

# App title
st.title('Canadian Immigration Data')

# Horizontal line separator
st.markdown("---")

# Radio button selection
col_chosen = st.radio("Select Data View", options=['Continents', 'Top10Regions', 'Top10Countries'])

# Define the logic for plotting based on the selection
if col_chosen == 'Continents':
    fig = px.histogram(df, x='Continent', y='Total', title='Immigration to Canada by Region', histfunc='avg',
                       category_orders={'Continent': ['Northern America', 'Asia', 'Europe', 'Latin America and the Caribbean', 'Africa', 'Oceania']})

elif col_chosen == 'Top10Regions':
    top10regions = df.groupby('Region')['Total'].sum().sort_values(ascending=False).head(10).reset_index()
    fig = px.bar(top10regions, x='Region', y='Total', title='Immigration to Canada by Region')

else:
    top10countries = df.nlargest(10, 'Total').reset_index()[['Country', 'Total']]
    top10countries.loc[2, 'Country'] = 'United Kingdom'
    fig = px.bar(top10countries, x='Country', y='Total', title='Immigration to Canada by Country')

# Display the plot
st.plotly_chart(fig)
