import streamlit as st
from PIL import Image
img = Image.open('Minimalist Initials Logo.png')
st.set_page_config(page_title = "DataSpace",page_icon = img, layout = 'wide')


from predict_page import show_predict_page
from explore_page import show_explore_page
from path_imaging import show_path_page


st.sidebar.image('Minimalist Initials Logo.png', width=300)
st.sidebar.title("DataSpace")
st.sidebar.markdown("DataSpace brings Decision Intelligence to medical diagnostics")

menu = st.sidebar.selectbox(
    "",
("Decision Support","Data Explorer", "Pathology Interpretation")
)

def create_page():
    page = RI.create_page()
    return page

if menu == 'Decision Support':
    show_predict_page()
elif menu =='Data Explorer':
    show_explore_page()
elif menu =='Pathology Interpretation':
    show_path_page()

    

