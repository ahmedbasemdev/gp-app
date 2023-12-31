
def perform_prediction(input_data, pipeline, model):
    import pandas as pd
    from sklearn.decomposition import PCA
    intput_df = pd.DataFrame(input_data, index=[0])

    ### Transformations ###
    ## 1
    pca = PCA(n_components=1)
    pca_result = pca.fit_transform(intput_df[['sysBP', 'diaBP']])
    intput_df['sys_dia'] = pca_result

    ## 2


    # preprocessed_data = pipeline.transform(intput_df)
    #
    # prediction = model.predict(preprocessed_data)

    return {"prediction": 1}