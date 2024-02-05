import pandas as pd
from flask import Flask, render_template, request, url_for, jsonify
import joblib
from ChatBot import ChatBotManager
import chd
import ecg_mi
import stroke
import os

app = Flask(__name__)
#chatbot = ChatBotManager()
app.config['UPLOAD_FOLDER'] = "ecg_mi/images"





@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=['GET'])
def chat():
    try:
        question = request.form["question"]
        answer = chatbot.generate_answer(question)
        return {"answer": answer}
    except Exception as e:
        return {"error" :str(e)}


@app.route("/get_doctors", methods=["GET"])
def get_doctors():
    if request.method == "GET":
        user_city = request.form["city"]
        doctor_data = pd.read_excel('doctors.xlsx')
        custom_data = doctor_data[doctor_data.city == user_city]
        data_list = []
        for i in range(len(custom_data)):
            row_data = custom_data.iloc[i]
            dict_data = {"name": str(row_data[0]), "image": row_data.image,
                         "location": row_data.location, "price": row_data.price}
            data_list.append(dict_data)

        return jsonify(data_list)


@app.route("/cities", methods=["GET"])
def get_cities():
    doctor_data = pd.read_excel('doctors.xlsx')
    cities = doctor_data.city

    return list(cities.unique())




@app.route("/stroke", methods=["POST","GET"])
def stroke_prediction():
    if request.method == "POST":
        data = {
        "age": int(request.form.get('age')),
        "hypertension": int(request.form.get('hypertension')),
        "heart_disease": int(request.form.get('heart_disease')),
        "avg_glucose_level": int(request.form.get('avg_glucose_level')),
        "bmi": int(request.form.get('bmi')),
        "gender": int(request.form.get('gender')),
        "ever_married":int( request.form.get('ever_married')),
        "work_type":int( request.form.get('work_type')),
        "Residence_type": int(request.form.get('Residence_type')),
        "smoking_status": int(request.form.get('smoking_status'))
        }
        pipeline = joblib.load("stroke/pipeline.joblib")
        model = joblib.load("stroke/model.joblib")
        prediction = stroke.perform_prediction(data, pipeline, model)
        return render_template("stroke.html", 
                               result = prediction['prediction'], message=prediction['Message'])
    else:
        return render_template("stroke.html")


@app.route("/chd", methods=["POST","GET"])
def chd_prediction():
    if request.method == "POST":
        data = request.args.to_dict(flat=False)
        print(data)
        #data = request.json

        pipeline = joblib.load("chd/pipeline.joblib")
        model = joblib.load("chd/model.joblib")

        prediction = chd.perform_prediction(data, pipeline, model)
        return render_template("chd.html",
                               result = prediction['prediction'], message=prediction['Message'])
    else:
        return render_template("chd.html")
    
@app.route("/ecg_mi", methods=["POST","GET"])
def ecg_mi_prediction():
    if request.method == "POST":
        data = {
            "Age":int(request.form.get("Age")),
            "CK-MB":int(request.form.get("CK-MB")),
            "Troponin":float(request.form.get("Troponin"))}
        #uploaded_file = request.files['file']
        #file_path = os.path.join(
        #app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        #uploaded_file.save(file_path)
        file_path = "ecg_mi/images/mi1.jpg"
        pipeline = joblib.load("ecg_mi/mi_pipeline.joblib")
        model = joblib.load("ecg_mi/mi_model.joblib")
        ecg_model = joblib.load('ecg_mi/RF_model_ecg.pkl')
        
        prediction = ecg_mi.mi_ecg_prediction(data, pipeline, model, file_path, ecg_model)

        return render_template("ecg.html",
                               result = prediction['s'], message=prediction['s'])
    else:
        return render_template("ecg.html")
    

    
@app.route("/stroke_analysis")
def stroke_analysis():
    return render_template("stroke_analysis.html")

@app.route("/chd_analysis")
def chd_anlaysis():
    return render_template("chd_analysis.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)






