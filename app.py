import streamlit as st 
from PIL import Image,ImageFilter

st.title("Image Filter")
img = st.file_uploader("Upload Image", type=['jpg','jpeg','png'])
if img:
    img = Image.open(img)
    option = st.selectbox("Select Filter",['Original','GrayScale','Contour','Blur'])
    if option == 'GrayScale':
        img = img.convert('L')  #sortcut fot grayscale
    elif option == 'Contour':
        img = img.filter(ImageFilter.CONTOUR)
    elif option == 'Blur':
        img = img.filter(ImageFilter.BLUR) 
    st.image(img)  
    