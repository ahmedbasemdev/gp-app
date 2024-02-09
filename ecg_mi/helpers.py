import pandas as pd
from skimage import measure, color, io
from skimage.filters import threshold_otsu, gaussian
from skimage.transform import resize
from sklearn.preprocessing import MinMaxScaler
import messages
from cv2 import imread


def process_ecg_image(image_path):
    # Read the image
    image = imread(image_path)

    # Defining the leads coordinates
    Lead_1 = image[300:600, 150:643]
    Lead_2 = image[300:600, 646:1135]
    Lead_3 = image[300:600, 1140:1625]
    Lead_4 = image[300:600, 1630:2125]
    Lead_5 = image[600:900, 150:643]
    Lead_6 = image[600:900, 646:1135]
    Lead_7 = image[600:900, 1140:1625]
    Lead_8 = image[600:900, 1630:2125]
    Lead_9 = image[900:1200, 150:643]
    Lead_10 = image[900:1200, 646:1135]
    Lead_11 = image[900:1200, 1140:1625]
    Lead_12 = image[900:1200, 1630:2125]
    Lead_13 = image[1250:1480, 150:2125]           # Lead 3 prolonged

    Leads=[Lead_1,Lead_2,Lead_3,Lead_4,Lead_5,Lead_6,Lead_7,Lead_8,Lead_9,Lead_10,Lead_11,Lead_12,Lead_13]

    flattened_leads_data = []

    #looping through image list containg all the 12 leads
    for x,y in enumerate(Leads[:len(Leads)-1]):
        # Convert image to grayscale_image
        grayscale_image = color.rgb2gray(y)

        # Apply Gaussian filtering to smooth the image
        blurred_image = gaussian(grayscale_image, sigma=0.8)

        # Apply Otsu's thresholding to distinguish foreground and background
        global_threshold = threshold_otsu(blurred_image)
        binary_image = blurred_image < global_threshold

        # Resize the binary image
        binary_image = resize(binary_image, (300, 450))

        # Finding the contours
        contours = measure.find_contours(binary_image, 0.8)

        # Sorting contours by shape and selecting the largest one
        contours_shape = sorted([x.shape for x in contours])[::-1][0:1]

        # Resizing counters
        for contour in contours:
            if contour.shape in contours_shape:
                resized_contour = resize(contour, (255, 2))

        # Applying scaling on the data with Min Max Normalization
        lead_no = x
        scaler = MinMaxScaler()
        fit_transformed_data = scaler.fit_transform(resized_contour)
        Normalized_Scaled=pd.DataFrame(fit_transformed_data[:,0], columns = ['X'])
        Normalized_Scaled=Normalized_Scaled.T

        flattened_data = Normalized_Scaled.values.flatten()  # Flatten the DataFrame to a 1D array
        flattened_leads_data.extend(flattened_data)  # Extend the list with this array

    # Convert the list of all lead data into a single-row DataFrame
    resized_contour_final = pd.DataFrame([flattened_leads_data])

    # Return the final DataFrame
    return resized_contour_final


def mi_prediction(input_data, pipeline, model):
    intput_df = pd.DataFrame(input_data, index=[0])

    preprocessed_data = pipeline.transform(intput_df)

    prediction = model.predict(preprocessed_data)[0]

    return prediction


def ecg_prediction(image_path, model):
    processed_image = process_ecg_image(image_path)
    prediction = model.predict(processed_image)[0]
    return prediction


def mi_ecg_prediction(input_data, mi_pipeline, mi_model, image_path, ecg_model):
    mi_ouput = mi_prediction(input_data, mi_pipeline,mi_model)
    ecg_ouput = ecg_prediction(image_path, ecg_model)
    print(mi_ouput, ecg_ouput, "s")
    if mi_ouput == 1:
        if ecg_ouput == 0:
            return {"prediction": "1", "Message": messages.m_1_hb}
        if ecg_ouput == 1:
            return {"prediction": "1", "Message": messages.m_1_mi}
        if ecg_ouput == 3:
            return {"prediction": "1", "Message": messages.m_1_pm}
    else:
        if ecg_ouput == 0:
            return {"prediction": "1", "Message": messages.m_0_hb}
        if ecg_ouput == 1:
            return {"prediction": "1", "Message": messages.m_0_mi}
        if ecg_ouput == 2:
            return {"prediction": "0", "Message": messages.m_0_no}

        

