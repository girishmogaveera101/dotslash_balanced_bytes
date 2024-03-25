import streamlit as st
import requests

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Balanced Bytes - Check Your Diet",
        page_icon='🌱',
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Define title
    st.title("Balanced Bytes")

    # Create columns for input fields
    col1, col2 = st.columns(2)
    
    # Input fields for personal details
    with col1:
        st.subheader("Personal Details")
        name_val = st.text_input("Name", "")
        weight_val = st.number_input("Weight (kg)", value=0)
    with col2:
        st.subheader("")
        age_val = st.number_input("Age", value=0)
        height_val = st.number_input("Height (cm)", value=0)

    # Activity level selection
    st.subheader("Activity Level")
    activity_level_val = st.radio("", ['Lightly Active', 'Moderately Active', 'Very Active'])

    # Dietary preferences and habits
    st.subheader("Dietary Preferences and Habits")
    gender_val = st.selectbox("Gender", ['Male', 'Female'])
    food_allergies_val = st.multiselect("Food Allergies", ['Gluten Intolerance', 'Lactose Intolerance', 'Peanut Allergy', 'Others'])
    eating_habits_val = st.selectbox("Eating Habits", ['Eats Out Frequently', 'Cooks at Home', 'Skips Meals'])
    goal_val = st.selectbox("Goals", ['Weight Loss', 'Weight Maintenance', 'Muscle Gain', 'Improved Energy Levels'])
    diet_plan_val = st.selectbox("Diet Plan", ['Vegan', 'Non-Vegan', 'Paleo'])
    water_consump_val = st.selectbox("Water Consumption", ['Less', '1 Litre', '1.5 Litres', '2 Litres', 'More'])
    supplements_val = st.checkbox("Take Dietary Supplements")

    # Pregnancy/Breastfeeding
    pregnant_val = st.checkbox("Pregnant/Breastfeeding")

    # Health problems
    st.subheader("Health Problems")
    health_problems_val = st.multiselect("Health Problems", ['Diabetes', 'Hypertension', 'Digestive Issues'])

    # Submit button
    if st.button("Submit", key="submit_button"):
        if name_val:
            response = requests.post(
                'http://127.0.0.1:5000/post_data', 
                json={
                    'name': name_val, 
                    'age': age_val, 
                    'height': height_val, 
                    'weight': weight_val,
                    'gender': gender_val,
                    'activity_level': activity_level_val,
                    'food_allergies': food_allergies_val,
                    'eating_habits': eating_habits_val,
                    'goal': goal_val,
                    'water_consump': water_consump_val,
                    'pregnant': pregnant_val,
                    'diet_plan': diet_plan_val,
                    'health_problems': health_problems_val,
                    'supplements': supplements_val
                }
            )
            if response.status_code == 200:
                st.success("Data uploaded successfully! 🎉")
            else:
                st.error("Failed to upload data...")
        else:
            st.warning("Name cannot be empty!")
        st.write("To check a product?"
                        f'''
                            <a style="" target="_self" href="/options">
                                <button style="border:0px solid black;color:;border-radius:10px;padding: 0px 10px; background-color: #0E1117">
                                    <p style="font-size:20px;color:#FF4B4B;"><u>click here</u></p>
                            </button>
                            </a>
                        ''',unsafe_allow_html=True
        )


if __name__ == "__main__":
    main()