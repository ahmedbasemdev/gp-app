import pandas as pd
from flask import Flask, render_template, request, url_for, jsonify
from dotenv import load_dotenv, find_dotenv
import os
import json
import joblib
from QA import *
import chd
import stroke

load_dotenv(find_dotenv(), override=True)
app = Flask(__name__)
index_name = 'ask-document'
vector_store = insert_of_fetch_embeddings(index_name)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/chat", methods=['GET'])
def chat():
    if request.method == "GET":
        question = request.form["question"]
        answer = ask_get_answer(vector_store, question)
        return {"answer": answer}


@app.route("/chd", methods=["GET"])
def chd_prediction():
    if request.method == "GET":
        data = request.json

        pipeline = joblib.load("chd/pipeline.joblib")
        model = joblib.load("chd/best_model.joblib")

        prediction = chd.perform_prediction(data, pipeline, model)
        return prediction


@app.route("/get_doctors", methods=["GET"])
def det_doctors():
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






@app.route("/stroke", methods=["GET"])
def stroke_prediction():
    if request.method == "GET":
        data = request.json
        pipeline = joblib.load("chd/pipeline.joblib")
        model = joblib.load("chd/best_model.joblib")

        prediction = stroke.perform_prediction(data, pipeline, model)
        return prediction

@app.route("/hello")
def say_hello():
    return {"anser": "hello"}


if __name__ == "__main__":
    app.run(debug=True)
    # print("Loading Data..")
    # data = load_from_wikipedia("استراتيجيات للوقاية من مرض القلب", 'ar')
    # print("Chunk Data ..")
    # chunks = chunk_data(data)
    # delete_index("all")
    # index_name = 'ask-document'
    # vector_store = insert_of_fetch_embeddings(index_name)
