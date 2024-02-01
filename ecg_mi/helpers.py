import pandas as pd


def mi_prediction(input_data, pipeline, model):
    intput_df = pd.DataFrame(input_data, index=[0])

    preprocessed_data = pipeline.transform(intput_df)

    prediction = model.predict(preprocessed_data)

    return {"prediction": str(prediction[0])}


def ecg_prediction(input_data, pipeline, model):
    return {"prediction": "1"}


def mi_ecg_prediction():
    pass
