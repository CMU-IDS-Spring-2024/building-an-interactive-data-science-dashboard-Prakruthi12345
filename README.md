# hw3-template

In this assignment, you will adopt the persona of being a data scientist for Allegheny County’s Health Department.  Your goal is to build data science tools to make it easier for the health department to understand trends of an ongoing health crisis:  fatal accidental overdoses from a variety of drugs in the county.  The Western Pennsylvania Regional Data Center publishes a monthly dataset that describes fatal accidental overdose incidents in Allegheny County, denoting age, gender, race, drugs present, zip code of incident and zip code of residence.

This data, downloaded as of September 22, 2023, is located in [data/overdose_data_092223.csv](data/overdose_data_092223.csv)

Through a series of assignments, you will build out a dashboard to support the interactive exploration and analysis of the dataset.  You will use this same repository for Assignments 3a, 3b, and 3c.  

- [ ] For Assignment 3a, Update the provided Streamlit python file, `pages/1_👥_Demographics.py`
- [ ] For Assignment 3b, Update the provided Streamlit python file, `pages/2_📈_Trends.py`
- [ ] For Assignment 3c, Update the provided Streamlit python file, `pages/3_🌍_Map.py`
- [ ] In addition, submit your Github repository URL on Canvas for each of the three assignments.

## Running the Streamlit app

You can execute the Streamlit app by running `streamlit run County_Dashboard.py`

## Questions 

3a:

1. Did you notice any interesting patterns or trends in the dataset?

I noticed that the number of fatal overdoses increased steadily from 2006 to 2018 with a spike from 2016 to 2018 and a decrease in the number of fatal overdoses from 2018 to 2024, with a spike from 2020 to 2022. I noticed that the highest number of overdoses were in the 30 to 50 age range and that men and white people had higher counts of overdoses compared to their female and black counterparts.
 

2. Was it possible to understand how the dataset was different in the earlier years versus the more recent years?
   
  - If so, what were some differences?  
  - If not, how would you suggest changing the dashboard to make differences easier to find?

   Yes, I noticed that the number of fatal overdoses was quite low prior to around 2016 and spiked around that time, after which it decreased in more recent years, but is still higher than it was in the early 2000's. It has only significantly reduced in 2023.


3. Did you discover any filters that demonstrated big differences from the overall dataset among the demographics (such as age, race, or gender)?

Heroin overdoses were very high in the 25-30 age range compared to overall, where the highest overdoses were in the 30 to 50 age range. I also discovered that in more recent years, the age range of people with the highest count of overdoses is younger than it was earlier. For example, from 2007 to 2012, the age group of 45 to 55 had the highest count, as opposed to 2017 to 2023, which has 30 to 40 year olds having the highest number of fatal overdoses.

   
4. Are there any other features you wish were present in your dashboard to either make discovery easier or to explore alternative aspects of the dataset?

I would like to have explored the distribution of fatal overdoses with respect to zipcode as well, as this would allow us to identiy high-risk areas where we could potentially intervene and start programs to aid those who are addicted to deadly drugs.


3b:

1. Did you notice any interesting patterns or trends in the dataset?

I observed that for nearly all of the drugs, there were much fewer incidents prior to 2013 when compared to more recent years. Many drugs including Alcohol and Cocaine saw spikes around 2016 to 2017. Additionally, Fentanyl saw a significant increase in incidents from 2018 to 2023. 

2. Was it possible to understand how the dataset was different in the earlier years versus the more recent years?
   
 - If so, what were some differences?  

 - If not, how would you suggest changing the dashboard to make differences easier to find?

Like I mentioned previously, for nearly all of the drugs, there were much fewer incidents prior to 2013 when compared to more recent years. Additionally, I observed that from 2007 and 2012, the top drug was consistently cocaine. However, when the date/time range was extended until 2020, Alcohol became the top drug, and when extended until 2023, Fentanyl became the most prevalent drug in the incidents.

3. Are there any other features you wish were present in your dashboard to either make discovery easier or to explore alternative aspects of the dataset?

I feel that perhaps the time of day at which the incident occured could have been explored. This would help us better understand whether there are certain times of the day when fatal accidental overdoses occur more frequently and if there are preventative measures that we as a society can put in place during those peak hours specifically.


3c:

1. Did you notice any interesting patterns or trends in the dataset?

I observed that the number of incidents in each location was in general much lower in the years prior to 2013, when compared to the more recent years. Additionally, when considering all the years, only around 10 locations had a number of incidents more than 150, with a majority of the locations having a number of incidents less than 100.

2. Was it possible to understand how the dataset was different in the earlier years versus the more recent years? 
 a. If so, what were some differences?  
 b. If not, how would you suggest changing the dashboard to make differences easier to find?

Yes, the number of incidents in each location was in general much lower in the years prior to 2013, when compared to the more recent years. The areas surrounding Pittsburgh in particular had a much higher incident rate in recent years.

3. Are there any other features you wish were present in your dashboard to either make discovery easier or to explore alternative aspects of the dataset?

I wish I could also explore how the specific time of day varies affects the incident count. As I mentioned earlier, we could have an additional filter and chart for time of day to better understand whether there are certain times of the day when fatal accidental overdoses occur more frequently.


