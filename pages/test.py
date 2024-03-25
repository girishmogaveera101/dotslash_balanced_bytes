import streamlit as st
import webbrowser
import requests
from PIL import Image

st.set_page_config(page_title="Baalanced Bytes - Take an image", page_icon="🌱")
st.markdown("""<style>
    [data-testid="collapsedControl"] {
        display: none}</style>""",
    unsafe_allow_html=True,
)
st.markdown(
    r"""
    <style>
    .stDeployButton {
            visibility: hidden;
        }
    </style>
    """, unsafe_allow_html=True
)


# if st.button("<"):    #back button basic just change the route address
#     back_page = "http://localhost:5001/details"
#     webbrowser.open(back_page)

st.header("Take the image of the ingredients and nutritional table")
camera_image = st.camera_input("")




if camera_image is not None:
    st.image(camera_image, caption='Uploaded Image', use_column_width=True)
    if st.button('Check'):
            # Convert it to the  bytes format 
        file_bytes = camera_image.read()

            # Prepare the data to send to Flask
        files = {"file": ("image2.jpg", file_bytes, "image/jpeg")}

           
        response = requests.post("http://127.0.0.1:5000/camera-image", files=files)
        if response.status_code == 200:
            st.write(response.text)
        else:
            st.write("Couln't send the Image")