import pandas as pd


def perform_prediction(sample_input_data, pipeline, model):
    intput_df = pd.DataFrame(sample_input_data, index=[0])

    preprocessed_data = pipeline.transform(intput_df)

    prediction = model.predict(preprocessed_data)

    return {"prediction": str(prediction[0]), "Message": "Hello From Stoke"}
