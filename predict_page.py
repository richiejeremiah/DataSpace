import streamlit as st
import pickle 
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.preprocessing import MultiLabelBinarizer
from numpy import array
from datetime import date
import pdfkit
from streamlit.components.v1 import iframe
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader


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

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("template.html")

def show_predict_page():

    st.title("Clinical Case Analysis")
    
    st.write("""##### DataSpace's decision support tool assists physicians in making  real-time data driven decisions through the use of artificial intelligence technology.""")  

    st.markdown('Kindly fill in details of your clinical case for analysis')
   
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

    form = st.form("my_form")
    name = form.text_input("Full name")
    Months = form.number_input("Month", min_value=1, max_value=12)
    Onset = form.number_input("Onset of Disease", min_value=0, max_value=14)
    
    Sex = form.selectbox("Sex", Sex)
    Hotness_of_Body = form.selectbox("Hotness of Body", Hotness_of_Body)
    Dehydration = form.selectbox("Dehydration", Dehydration)
    Chestwall_Indrawing = form.selectbox("Chestwall Indrawing", Chestwall_Indrawing)
    Vomiting = form.selectbox("Vomiting", Vomiting)
    SickLooking = form.selectbox("SickLooking", SickLooking)

    Age = form.slider("Age", 0, 18, 3)
    Temperature = form.slider("Temperature", 36.0, 40.0, 36.9)

    ok = form.form_submit_button("Submit")
    if ok:
        x = np.array([[Age,Sex,Hotness_of_Body,Dehydration,Chestwall_Indrawing,Vomiting,SickLooking,Temperature,Months,Onset]])
        x[:, 1] = le_sex.transform(x[:,1])
        x[:, 2] = le_HOB.transform(x[:,2])
        x[:, 3] = le_Deh.transform(x[:,3])
        x[:, 4] = le_CWI.transform(x[:,4])
        x[:, 5] = le_vomit.transform(x[:,5])
        x[:, 6] = le_Sick.transform(x[:,6])
        x = x.astype(float)        


        y_pred=regressor_loaded.predict(x)
        A = binarizer.inverse_transform(y_pred)
        B= '\n'.join([str(x) for t in A for x in t])
        
    agree = st.checkbox('I consent to providing my confidential patient information for research and planning purposes')
    
    if ok:
        html = template.render(
            date=date.today().strftime("%B %d, %Y"),
            name =name,
            age=Age,
            sex=Sex,
            diagnosis= B,
            temperature=Temperature,
            Onset=Onset,
        )
        pdf = pdfkit.from_string(html, False)

        st.success("Form submitted!")
        st.download_button(
            "⬇️ Download PDF",
            data=pdf,
            file_name="Patient Form.pdf",
            mime="application/octet-stream",
        )

       
