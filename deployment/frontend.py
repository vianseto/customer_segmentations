import backend
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Aditya Vianseto FDTS Batch 11",
    page_icon=Image.open('rating.png'),
)   

image = Image.open('AdobeStock_81896794-960x640_photos_v2_x2.jpg')
st.image(image)
colH1, colH2 = st.columns([0.05,10])
colH2.header('Portugal Customer Segmentations Predictor')
colH2.caption('This Application For **Predict** Portugal **Customer Segmentations** by their **Annual Spending** on **Fresh**, **Milk**, **Grocery**, **Frozen**, **Detergents + Paper**, and **Delicatessen** Product Line')
st.write("")

region = st.selectbox('Customer Region',['Lisbon','Oporto','Other'])
channel = st.selectbox('Customer Channel', ['Horeca (Hotel, Restaurant, and Cafe)','Retail'])
fresh = st.number_input('Customer Annual Spending on Fresh Product', value=22925.0)
milk = st.number_input('Customer Annual Spending on Milk Product', value=73498.0)
grocery = st.number_input('Customer Annual Spending on Grocery Product', value=32114.0)
frozen = st.number_input('Customer Annual Spending on Frozen Product', value=987.0)
detergents_paper = st.number_input('Customer Annual Spending on Detergents and Paper Product', value=20070.0)
delicatessen = st.number_input('Customer Annual Spending on Delicatessen Product', value=903.0)

col1, col2, col3 = st.columns([9,10,1])
button = col2.button('Predict')

if button == True:
    st.success(f'He / She is "{backend.predict(channel,region,fresh,milk,grocery,frozen,detergents_paper,delicatessen)}" !')