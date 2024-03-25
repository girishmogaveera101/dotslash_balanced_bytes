from flask import Flask, request, jsonify, json
from PIL import Image
from LLM import gemini_output, get_llm_response
# import pytesseract

app = Flask(__name__)



user_details = {}
print("out",user_details)
@app.route('/post_data', methods=['POST'])
def get_data():
    global user_details
    data = request.json
    name_val = data['name']
    age_val = data['age']
    height_val = data['height']
    weight_val = data['weight']
    gender_val = data['gender']
    supplements_val = str(data['supplements'])
    activity_level_val = data['activity_level']
    food_allergies_val = data['food_allergies']
    eating_habits_val = data['eating_habits']
    goal_val = data['goal']
    water_consump_val = data['water_consump']
    pregnant_val = str(data['pregnant'])
    diet_plan_val = data['diet_plan']
    health_problems_val = data['health_problems']
    user_details = {
        'name': name_val,
        'age': age_val,
        'height':height_val,
        'weight':weight_val,
        'gender':gender_val,
        'activity level':activity_level_val,
        'food allergies':food_allergies_val,
        'eating habits':eating_habits_val,
        'goal':goal_val,
        'water consumption':water_consump_val,
        'pregnant':pregnant_val,
        'diet plans':diet_plan_val,
        'health problems':health_problems_val,
        'supplements consumption':supplements_val
    }
    print("in post",user_details)
    return("success")

@app.route('/signin', methods=['POST'])
def signin():
    data = request.json
    email_val = data['email']
    mobile_val = data['mobile']
    password_val = data['password']
    signin_details = {
        'email':email_val,
        'mobile': mobile_val,
        'password':password_val
    }
    print(signin_details)
    return("success")


@app.route('/upload-image', methods = ['POST'])
def upload_image():
    global user_details
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        # Save the uploaded file
        uploaded_file.save(uploaded_file.filename)
        print("in camera",user_details)
        system_prompt =  """
                You are a specialist in nutritional facts.
                Input images in the form of wrappers of packaged good will be provided to you,
                and your task is to respond with the text document of all the ingredients present in it give it in a list format.
                take the nutritional facts table part and return how much quantity of the specific nutrients present in that food
             """
        user_prompt = "Give me the information about it"
        extracted_text = gemini_output(uploaded_file.filename,system_prompt,user_prompt)
        llm_response = get_llm_response(extracted_text,user_details)



        global llm 
        llm= llm_response.split("```json")[1].strip()
        llm = llm.strip("`")

        return "Image uploaded successfully."
    else:
        return "No Image received."
    


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email_val = data['email']
    password_val = data['password']
    login_details = {
        'email':email_val,
        'password':password_val
    }
    print(login_details)
    return("success")


@app.route('/camera-image', methods = ['POST'])
def camera_image():
    global user_details
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        # Save the uploaded file
        uploaded_file.save(uploaded_file.filename)
        print("in camera",user_details)

        return "Image uploaded successfully."
    else:
        return "No Image received."
    

@app.route('/output', methods=['GET'])
def output():
    return llm


print(user_details)
if __name__ == "__main__":
    app.run(debug=True)

