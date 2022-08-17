import streamlit as st
from PIL import Image
img = Image.open('Minimalist Initials Logo.png')
st.set_page_config(page_title = "Augius",page_icon = img, layout = 'wide')


from predict_page import show_predict_page
from explore_page import show_explore_page
from path_imaging import show_path_page


st.sidebar.image('1.png', width=300)
st.sidebar.title("DataSpace")
st.sidebar.markdown("Bringing Decision Intelligence To Medical Diagnostics")

menu = st.sidebar.selectbox(
    "",
("Pathology Interpretation","Decision Support", "Data Explorer")
)

def create_page():
    page = RI.create_page()
    return page

if menu =='Pathology Interpretation':
    show_path_page()
elif menu == 'Decision Support':
    show_predict_page()    
elif menu =='Data Explorer':
    show_explore_page()
