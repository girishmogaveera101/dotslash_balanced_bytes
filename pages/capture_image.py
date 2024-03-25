import streamlit as st 
import requests
import webbrowser
def capture_image():
    st.set_page_config(initial_sidebar_state="collapsed")

    st.markdown(
        r"""
        <style>
        .stDeployButton {
                visibility: hidden;
            }
        </style>
        """, unsafe_allow_html=True
    )
    st.markdown("""<style>
        [data-testid="collapsedControl"] {
            display: none}</style>""",
        unsafe_allow_html=True,
    )



    st.title("IMAGE PROCESSOR")
    st.divider()
    st.header("Take an image of the product")

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
            if response.status_code == 200:
                st.write("To Check your output.."
                        f'''
                            <a style="" target="_self" href="/output">
                                <button style="border:0px solid black;color:#00ff44;border-radius:10px;padding: 0px 10px; background-color: white">
                                    <p style="font-size:17px;color:#007DFF;"><u>click here</u></p>
                                </button>
                            </a>
                        ''',unsafe_allow_html=True
                )

capture_image()