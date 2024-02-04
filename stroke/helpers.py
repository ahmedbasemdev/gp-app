import pandas as pd

postive_message = """
Our recent analysis using the cardiovascular
prediction system indicates an elevated risk for
stroke. It's crucial to view this as a proactive
opportunity for early intervention and management.
Sorry, Please schedule a visit with a healthcare
provider for a comprehensive evaluation and
personalized advice.
Get well soon."""

negative_message="""
Good news from your recent health assessment:
your stroke risk is low based on our analysis. It's a
positive sign, but staying on a healthy path is key.
Keep up with balanced eating, exercise, and stress
management.
Best."""


def perform_prediction(sample_input_data, pipeline, model):
    intput_df = pd.DataFrame(sample_input_data, index=[1])
    
    preprocessed_data = pipeline.transform(intput_df)

    prediction = model.predict(preprocessed_data)
    
    if str(prediction[0]) == "1":
        return {"prediction": "1", "Message": postive_message}
    elif str(prediction[0]) == "0":
        return {"prediction": "0", "Message": negative_message}
