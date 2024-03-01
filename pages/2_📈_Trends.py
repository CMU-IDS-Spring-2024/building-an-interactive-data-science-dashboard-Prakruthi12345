import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

df = pd.read_csv("Downloads/overdose_data_092223.csv")
df.death_date_and_time = pd.to_datetime(df.death_date_and_time)

st.title("Trends")
st.markdown("This interactive dashboard supports the exploration of trends of the primary drugs involved in fatal accidental overdoses in Allegheny County.  You can filter by the date of the overdose incident, as well as select the number of top ranked primary drugs to show.")


data = df

#insert filters here

col1, col2 = st.columns([0.1, 0.1],gap="large")

with col1:
    dates = st.slider("Range", min_value=data['death_date_and_time'].min().to_pydatetime(), 
                       max_value=data['death_date_and_time'].max().to_pydatetime(), value=(data['death_date_and_time'].min().to_pydatetime(), data['death_date_and_time'].max().to_pydatetime()))
   


with col2:
    num_output = st.number_input("How many top drugs?", min_value=1, max_value=15, value=8)

start_date, end_date = dates
filtered_data = data[(data['death_date_and_time'] >= start_date) 
& (data['death_date_and_time'] <= end_date)]

# Calculate count of incidents for each drug for each year

drug_counts = filtered_data.groupby(['case_year', 'combined_od1']).size().reset_index(name='count')

# Find top drugs

drug_list = drug_counts.groupby('combined_od1')['count'].sum().nlargest(num_output).index

# Filter the data for the top drugs
top_drugs = drug_counts[drug_counts['combined_od1'].isin(drug_list)]

sorted_data = top_drugs.sort_values(by='count', ascending=False)


first = alt.Chart(sorted_data).mark_area().encode(
    x=alt.X('case_year:O', title='Fatal Overdoses per Year'),
    y=alt.Y('count:Q', title=''),
    color=alt.Color('combined_od1:N', title='Primary Drug Involved',legend=None)
).properties(
    width=600,
    height=50
)

final = first.encode(
    row=alt.Row(
        'combined_od1:N',
        title="Primary Drug Involved",sort=drug_list.tolist() 
    )
)

st.altair_chart(final, use_container_width=True)
