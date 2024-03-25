import streamlit as st 
import requests

# Set page title
st.title("Product Information")

# Fetch data from API
response = requests.get('http://localhost:5000/output')
data = response.json()
ingredients = data["ingredients"]
nutritional_value = data["nutritional_value"]
personalized_report = data["personalized_report"]
goal = data["how_does_this_product_affect_the_goal_of_the_user"]

# Define CSS styles
section_style = """
    border: 1px solid #E4E4E4;
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 20px;
"""

# Display goal section
st.markdown(f'<div style="{section_style}"><h2>Regarding your Goal</h2><p>{goal}</p></div>', unsafe_allow_html=True)

# Display personalized report section
st.markdown(f'<div style="{section_style}"><h2>Personalised Report</h2><p>{personalized_report}</p></div>', unsafe_allow_html=True)

# Display ingredients section
st.markdown(f'<div style="{section_style}"><h2>Ingredients</h2><p>{ingredients}</p></div>', unsafe_allow_html=True)

# Display nutritional data section
st.markdown(f'<div style="{section_style}"><h2>Nutritional Data</h2><p>{nutritional_value}</p></div>', unsafe_allow_html=True)
