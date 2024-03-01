import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


st.title("Demographics")
st.markdown("This interactive dashboard supports the exploration of the demographics (age, gender, and race) of the people involved in fatal accidental overdoses in Allegheny County.  You can filter by the year of the overdose incident, as well as the primary drug present in the incident.")

df = pd.read_csv("data/overdose_data_092223.csv")
df.death_date_and_time = pd.to_datetime(df.death_date_and_time)

# to make the visualizations more meaningful, we unabbreviate the race and sex columns

df['race'] = df['race'].str.replace('W','White')
df['race'] = df['race'].str.replace('B','Black')
df['race'] = df['race'].str.replace('H|A|I|M|O|U','Other', regex=True) #there are very few non-white/back decedents in this dataset, so we merge the remaining categories to 'other'
df.dropna(subset = ['race'], inplace=True)  #get rid of nulls

df['sex'] = df['sex'].str.replace('M','Male')
df['sex'] = df['sex'].str.replace('F','Female')


st.subheader("Filters")

#insert filters here

col1, col2 = st.columns([0.1, 0.1],gap="large")

with col1:
    year = st.slider('Filter by year:', 2007, 2023, (2007,2023))

drugs = df["combined_od1"].unique()

with col2:
    drug = st.multiselect(
        'Filter by the primary drug present:',
        drugs,)

if year:
    df_year = df[df["case_year"].between(year[0], year[1])]


if drug:
    df_year_drug = df_year.loc[df_year["combined_od1"].isin(drug)]

else:
    df_year_drug = df_year

st.subheader("Visualizations")

#insert visualizations here
hist_year = alt.Chart(df_year_drug).mark_bar().encode(x=alt.X('case_year:O', title="Year",bin=False) , y=alt.Y('count()', title="Count of Fatal Overdoses"))


st.altair_chart(hist_year, use_container_width=True)

hist_age = alt.Chart(df_year_drug, title="Age").mark_bar().encode(x=alt.X('count()', title="Count of Fatal Overdoses") , y=alt.Y('age', title="")).properties(height=400,width=200)

bar_gender = alt.Chart(df_year_drug, title="Gender").mark_bar().encode(x=alt.X('count()', title="Count of Fatal Overdoses") , y=alt.Y('sex', title="")).properties(height=400,width=200)

bar_race = alt.Chart(df_year_drug, title="Race").mark_bar().encode(x=alt.X('count()', title="Count of Fatal Overdoses") , y=alt.Y('race', title="")).properties(height=400,width=200)

st.altair_chart(hist_age | bar_gender | bar_race, use_container_width=True)

