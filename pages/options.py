import streamlit as st 

st.title("Select the IMAGE method")
st.divider()

st.subheader("To upload an image")
st.write(f'''
            <a style="" target="_self" href="/upload_image">
                <button style="border:0px solid #007DFF;color:#007DFF;border-radius:10px;padding: 0px 10px; background-color: #0E1117">
                    <p style="font-size:25px;color:#FF4B4B;"><u>click here</u></p>
                </button>
            </a>
        ''',unsafe_allow_html=True
)

st.divider()

st.subheader("To captute an image")
st.write(f'''
            <a style="" target="_self" href="/capture_image">
                <button style="border:0px solid #007DFF;color:#007DFF;border-radius:10px;padding: 0px 10px; background-color: #0E1117">
                    <p style="font-size:25px;color:#FF4B4B;"><u>click here</u></p>
                </button>
            </a>
        ''',unsafe_allow_html=True
)