import streamlit as st 
import requests
import webbrowser
def upload_image():
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
    st.header("Upload an image of the product")



    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        st.image(uploaded_file, use_column_width=True)
        if st.button('Check'):
                    # Convert the uploaded file to bytes
            file_bytes = uploaded_file.read()

                    # Prepare the data to send to Flask
            files = {"file": ("image1.jpg", file_bytes, "image/jpeg")}

                    # Make a POST request to Flask app
            response = requests.post("http://127.0.0.1:5000/upload-image", files=files)
            # st.write(response.text)
            if response.status_code == 200:
                st.write("To Check your output.."
                        f'''
                            <a style="" target="_self" href="/output">
                                <button style="border:0px solid black;color:#00ff44;border-radius:10px;padding: 0px 10px; background-color: #0E1117">
                                    <p style="font-size:17px;color:#FF4B4B;"><u>click here</u></p>
                                </button>
                            </a>
                        ''',unsafe_allow_html=True
            )
upload_image()