import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import nltk

from Helper import summary_poster, load_data

output_graphs = st.container()

df = pd.read_csv("DataSpace.csv")
color_map_df = load_data("sheet.csv")

def show_explore_page():
    st.title("Project Insights")
    df['diagnosis'] = df['Diagnosis'].str.split(',')
    # an empty list
    diseases = [] 

    # extract genres
    for i in df['diagnosis']: 
        diseases.append(i) 

    all = sum(diseases,[])
    len(set(all))

    all_diseases = nltk.FreqDist(all) 

    # create dataframe
    all_diseases_df = pd.DataFrame({'Disease': list(all_diseases.keys()), 'Count': list(all_diseases.values())})

   
    Countries = (
            "Algeria",
            "Botswana",
            "Burundi",
            "Congo",
            "Djibouti",
            "Ethiopia",
            "Ghana",
            "Kenya",
            "Libya",
            "Morocco",
            "Niger",
            "Rwanda",
            "South Africa",
            "Tanzania",
            "Uganda",
            "Zimbabwe"
    )

    County = (
            "Garissa",
            "Kakamega",
            "Kisumu",
            "Kwale",
            "Nairobi",
            "Nakuru",
            "Narok",
            "Machakos",
            "Mombasa",
            "Taita Taveta",
            "Wajir"   

    )
    #Define Country
    select_county_list = []
    select_region_list = []
    select_diagnosis_list = []

    select_county_list = df.County.unique()
    select_county_list.sort()

    county = st.selectbox("Select a county", select_county_list)

    #Generating the list of residences based on the county
    #state = input("Choose a state :")
    df_counties = df[(df.County == county)].copy()
    select_region_list = df_counties.Residence.unique()
    select_region_list.sort()
    
    region = st.selectbox("Select a region", select_region_list)


   # Generating the list of diagnosis 
    df_regions = df[(df.Residence == region)].copy()
    select_diagnosis_list = df_regions.Diagnosis.unique()
    select_diagnosis_list.sort()

    diagnosis = st.selectbox("Select a diagnosis", select_diagnosis_list)
    
    #slider for year 
    Year_list = []
   

    #Generating the list of year 
    df_diagnosis = df[(df.Diagnosis == diagnosis)].copy()
    year_list = df_diagnosis.Year.unique()
    year_list.sort()
    
    year =Year_list.append(st.slider('Year of Diagnosis', 2018,2021, step = 1))

        #slider for age at diagnosis
    Age_list = []
    
    #Generating the list of year 
    df_year = df[(df.Year == year)].copy()
    age_list = df_year.Age.unique()
    age_list.sort()

    age = Age_list.append(st.slider('Age at Diagnosis', 0,20, step =1))

    #Setting up color palette dict
    color_dict = dict(zip(color_map_df['clusters'], color_map_df['colors']))

    fig = (summary_poster(df_diagnosis, color_dict))
    st.write(fig)