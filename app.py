import pandas as pd
from flask import Flask, render_template, request, url_for, jsonify
import joblib
from ChatBot import ChatBotManager
import chd
import stroke

app = Flask(__name__)

#chatbot = ChatBotManager()



@app.route("/")
def home():
    return render_template("home.html")


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




@app.route("/stroke", methods=["GET"])
def stroke_prediction():
    if request.method == "GET":
        data = request.json
        pipeline = joblib.load("stroke/pipeline.joblib")
        model = joblib.load("stroke/model.joblib")

        prediction = stroke.perform_prediction(data, pipeline, model)
        return prediction
    else:
        return {"Wrong Method "}


@app.route("/chd", methods=["GET"])
def chd_prediction():
    if request.method == "GET":
        data = request.args.to_dict(flat=False)
        print(data)
        #data = request.json

        pipeline = joblib.load("chd/pipeline.joblib")
        model = joblib.load("chd/model.joblib")

        prediction = chd.perform_prediction(data, pipeline, model)
        return prediction
    else:
        return "Wrong Method"


if __name__ == "__main__":
    app.run(debug=True)

