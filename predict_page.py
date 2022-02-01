import streamlit as st
import pickle 
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.preprocessing import MultiLabelBinarizer
from numpy import array
def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data
data = load_model()
regressor_loaded = data["model"]
le_sex =data["le_sex"]
le_month= data['le_month']
le_HOB = data['le_HOB']
le_Deh=data['le_Deh'] 
le_CWI=data['le_CWI'] 
le_vomit=data['le_vomit']
le_Sick=data['le_Sick']
binarizer= data['binarizer']
def show_predict_page():
    st.title("Patient Triage")
    
    st.write("""##### Using AI we deliver precision healthcare to patients by asking relevant questions to assist physicians in suspecting  diseases & their complications.""")  
    st.markdown('Kindly fill in your information')
   
    months = (
        "January",
        "February",
        "March",
        "April",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    )
    Sex = (
        "M",
        "F"
    )
    Hotness_of_Body = (
        "Yes",
        "No"
    )
    Dehydration = (
        "Yes",
        "No"
    )
    Chestwall_Indrawing = (
        "Yes",
        "No"
    )
    Vomiting = (
        "Yes",
        "No"
    )
    SickLooking = (
        "Yes",
        "No"
    )
    Months = st.number_input("What month is it?", min_value=1, max_value=12)
    Onset = st.number_input("When was the initial onset of the patient's symptoms?", min_value=0, max_value=14)
    
    Sex = st.selectbox("What is the sex of the patient?", Sex)
    Hotness_of_Body = st.selectbox("Does the patient have hotness of body?", Hotness_of_Body)
    Dehydration = st.selectbox("Does the patient have dehydration?", Dehydration)
    Chestwall_Indrawing = st.selectbox("Does the patient have chestwall Indrawing?", Chestwall_Indrawing)
    Vomiting = st.selectbox(" Is the patient vomiting", Vomiting)
    SickLooking = st.selectbox("Is the patient sicklooking?", SickLooking)
    Age = st.slider("What is the age of the patient?", 0, 18, 3)
    Temperature = st.slider("What is the temperature of the patient?", 36.0, 40.0, 36.9)
    
    ok = st.button("Submit")
    if ok:
        x = np.array([[Age,Sex,Hotness_of_Body,Dehydration,Chestwall_Indrawing,Vomiting,SickLooking,Temperature,Months,Onset]])
        x[:, 1] = le_sex.transform(x[:,1])
        x[:, 2] = le_HOB.transform(x[:,2])
        x[:, 3] = le_Deh.transform(x[:,3])
        x[:, 4] = le_CWI.transform(x[:,4])
        x[:, 5] = le_vomit.transform(x[:,5])
        x[:, 6] = le_Sick.transform(x[:,6])
        x = x.astype(float)    
        
        y_pred= regressor_loaded.predict(x)
        A = binarizer.inverse_transform(y_pred)
        B= '\n'.join([str(x) for t in A for x in t])
        
        st.subheader(f"Suspected Complication: *{B}*")
