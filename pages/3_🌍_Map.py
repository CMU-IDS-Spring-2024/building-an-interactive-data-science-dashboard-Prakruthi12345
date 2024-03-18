import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("Map")
st.markdown("This interactive dashboard supports the exploration of trends of the locations involved in fatal accidental overdoses in Allegheny County.  You can filter by the date of the overdose incident, as well as filter locations by the number of incidents.")


df = pd.read_csv("data/overdose_data_092223.csv")
df.death_date_and_time = pd.to_datetime(df.death_date_and_time)
df.incident_zip = pd.to_numeric(df['incident_zip'], errors='coerce')


#insert filters here

col1, col2 = st.columns([0.1, 0.1],gap="large")

with col1:
    dates = st.slider("Range", min_value=df['death_date_and_time'].min().to_pydatetime(), 
                       max_value=df['death_date_and_time'].max().to_pydatetime(), value=(df['death_date_and_time'].min().to_pydatetime(), df['death_date_and_time'].max().to_pydatetime()))
   


with col2:
    cases = st.slider("How many cases?", min_value=1, 
                       max_value=351, value=(1, 351))
   

min_cases, max_cases = cases

start_date, end_date = dates

filtered_data = df[(df['death_date_and_time'] >= start_date) 
& (df['death_date_and_time'] <= end_date)]

zipcodes_latlon = pd.read_csv("data/zipcodes_latlon.csv")
allegheny_zipcodes = pd.read_csv("data/zipcodes_AlleghenyCounty.csv")

# Filter zip code data for zip codes within Allegheny County
zipcodes_latlon_allegheny = zipcodes_latlon[zipcodes_latlon['ZIP'].isin(allegheny_zipcodes['ZIPCODE'])]

# Count the number of incidents in each zip code
incident_counts = filtered_data['incident_zip'].value_counts().reset_index()

incident_counts.columns = ['ZIP', 'incident_count']

# Merge incident counts with zip code latitude and longitude data
zipcodes_merged = zipcodes_latlon_allegheny.merge(incident_counts, on='ZIP', how='left').fillna(0)

# Filter data by number of cases
zipcodes_merged = zipcodes_merged[(zipcodes_merged['incident_count'] >= min_cases) & (zipcodes_merged['incident_count'] <= max_cases)]

#Scale by 10
zipcodes_merged['incident_count'] = zipcodes_merged['incident_count']*10

# Display scatterplot on top of map
st.map(data=zipcodes_merged,latitude="LAT", longitude="LNG", color="#ff7f7fcc", size= "incident_count",zoom=9)
