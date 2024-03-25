from flask import Flask, request, jsonify, json

app = Flask(__name__)



@app.route('/post_data', methods=['POST'])
def get_data():
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
    print(user_details)
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



@app.route('/output', methods=['GET'])
def output():
    # data = {
    #     'name' : "Girish",
    #     'age' :"20"
    # }
    data ={
    "ingredients": {
        "caffeine": "A stimulant that helps to improve alertness and focus",
        "taurine": "An amino acid that is involved in energy production and antioxidant protection",
        "B vitamins (B2, B3, B5, B6, and B12)": "Vitamins that are involved in energy metabolism, brain function, and cell health",
        "glucuronolactone": "A substance that is involved in energy production and detoxification",
        "simple sugars (sucrose and glucose)": "Sugars that provide a quick source of energy",
        "carbonated water": "Water that has been infused with carbon dioxide gas",
        "sodium bicarbonate and magnesium carbonate (substituted in some flavours with a trisodium citrate/citric acid buffer, each solution providing electrolytes)": "Electrolytes are minerals that help to regulate fluid balance and muscle function",
        "acesulfame K and aspartame or sucralose": "Artificial sweeteners that provide a sweet taste with no calories"
    }
    }
    return data



@app.route('/upload-image', methods = ['POST'])
def upload_image():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        # Save the uploaded file
        uploaded_file.save(uploaded_file.filename)
        return "Image uploaded successfully."
    else:
        return "No Image received."
    


@app.route('/camera-image', methods = ['POST'])
def camera_image():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        # Save the uploaded file
        uploaded_file.save(uploaded_file.filename)
        return "Image uploaded successfully."
    else:
        return "No Image received."
if __name__ == "__main__":
    app.run(debug=True)