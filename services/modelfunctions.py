import os
import json
import pickle
import numpy as np
import pandas as pd
import keras.utils as image
from django.conf import settings
from sklearn import preprocessing

from keras.models import load_model

from django.core.files.storage import FileSystemStorage

# Deifned Values
model_dir = settings.MODELS_ROOT


class PestModel():
    def __init__(self, fileObj):
        self.fileObj = fileObj
        self.pest_img_height, self.pest_img_width = 180, 180
        pest_detection_model_path = os.path.join(
        model_dir, str('pest_detection_model.h5'))
        self.pest_model = load_model(pest_detection_model_path)
        self.pest_class_names = ['aphids', 'armyworm', 'beetle', 'bollworm',
                        'grasshopper', 'mites', 'mosquito', 'sawfly', 'stem_borer']

    def predict_image(self,img):
        prediction = self.pest_model.predict(img)[0]
        pred = {self.pest_class_names[i]: float(prediction[i]) for i in range(9)}
        max_value = max(pred, key=pred.get)
        return max_value

    def predict(self):
        fs = FileSystemStorage()
        filePathName = fs.save(self.fileObj.name, self.fileObj)
        deletePathName = filePathName
        filePathName = fs.url(filePathName)
        pred_img = '.'+filePathName
        img = image.load_img(pred_img, target_size=(
            self.pest_img_height, self.pest_img_width))
        x = image.img_to_array(img)
        x = x/255
        x = x.reshape(-1, self.pest_img_height, self.pest_img_width, 3)
        result =self.predict_image(x)
        print(deletePathName)
        fs.delete(deletePathName)
        return result

class CropDiseaseModel():
    def __init__(self, fileObj):
        self.fileObj = fileObj
        self.crop_des_height, self.crop_des_width = 40, 40
        crop_disease_model_path = os.path.join(model_dir, str('crop_disease_model.h5'))
        self.crop_disease_model = load_model(crop_disease_model_path)

        # save in another file
        self.crop_disease_class_names = ['Corn_(maize)___healthy',
                            'Corn___Cercospora_leaf-spot Gray_Leaf_Spot',
                            'Corn___Common_Rust',
                            'Corn___Leaf_Blight',
                            'Cotton__bacterial_blight',
                            'Cotton__curl_virus',
                            'Cotton__fussarium_wilt',
                            'Cotton__healthy',
                            'Rice__Bacterial leaf blight',
                            'Rice__Brown spot',
                            'Rice__Leaf smut',
                            'Rice___Healthy',
                            'Rice___Hispa',
                            'Rice___Leaf_Blast',
                            'Sugarcane__Bacterial Blight',
                            'Sugarcane__Healthy',
                            'Sugarcane__RedRot',
                            'Sugarcane__RedRust',
                            'Wheat__Healthy',
                            'Wheat___Brown_Rust',
                            'Wheat___Yellow_Rust',
                            'Wheat__septoria',
                            'Wheat__stripe_rust']
    
    def crop_predict_image(self,img):
        prediction = self.crop_disease_model.predict(img)[0]
        pred = {self.crop_disease_class_names[i]: float(
            prediction[i]) for i in range(23)}
        max_value = max(pred, key=pred.get)
        return max_value

    def predict(self):
        fs = FileSystemStorage()
        filePathName = fs.save(self.fileObj.name, self.fileObj)
        deletePathName = filePathName
        filePathName = fs.url(filePathName)
        crop_disease_img = '.'+filePathName
        img = image.load_img(crop_disease_img, target_size=(
            self.crop_des_height, self.crop_des_width))
        x = image.img_to_array(img)
        x = x/255
        x = x.reshape(-1, self.crop_des_height, self.crop_des_width, 3)
        result = self.crop_predict_image(x)
        fs.delete(deletePathName)
        return result
    
class SimpleCropModel():

    def __init__(self, data):
        self.data = data
        file_path_crop1 = os.path.join(model_dir, str('crops_recomendation_model1.pickle'))
        crop1_pickle_in = open(file_path_crop1, 'rb')
        self.crops_recomendation_model1 = pickle.load(crop1_pickle_in)
        self.crops_with_soil_df1 = pd.read_csv(
        "https://raw.githubusercontent.com/Nazif-Malhi/Farmstead_Models/main/ML%20Models%20Farmstead/Dataset/Crops/Crop_with_soil%20(i).csv")




    def predict(self):
        le1 = preprocessing.LabelEncoder()
        self.crops_with_soil_df1['soil'] = le1.fit_transform(self.crops_with_soil_df1['soil'])

        convertedLabel = le1.transform([self.data['soil_type']])
        prepare_data = np.array([[float(convertedLabel), float(self.data['temp']), float(self.data['humi']), float(self.data['ph']), float(self.data['rain'])]])
        prediction_crop1 = self.crops_recomendation_model1.predict(prepare_data)
        return prediction_crop1[0]

class AdvanceCropModel():

    def __init__(self, data):
        self.data = data
        file_path_crop2 = os.path.join(model_dir, str('crops_recomendation_model2.pickle'))
        crop2_pickle_in = open(file_path_crop2, 'rb')
        self.crops_recomendation_model2 = pickle.load(crop2_pickle_in)
        self.crops_with_soil_df2 = pd.read_csv(
        "https://raw.githubusercontent.com/Nazif-Malhi/Farmstead_Models/main/ML%20Models%20Farmstead/Dataset/Crops/Crop_with_soil%20(ii).csv")
    
    def predict(self):
        le2 = preprocessing.LabelEncoder()
        self.crops_with_soil_df2['soil'] = le2.fit_transform(self.crops_with_soil_df2['soil'])

        convertedLabel = le2.transform([self.data['soil_type']])
        prepare_data = np.array(
            [[float(self.data['nitrogen']), float(self.data['phosphorus']), float(self.data['potassium']), float(convertedLabel), float(self.data['temp']), float(self.data['humi']), float(self.data['ph']), float(self.data['rain'])]])
        prediction_crop = self.crops_recomendation_model2.predict(prepare_data)
        return prediction_crop[0]

class FertilizerModel():
    def __init__(self, data):
        self.data = data
        file_path_fertilizer = os.path.join(model_dir, str('fertilizer_recomendation_model.pickle'))
        fertilizer_pickle_in = open(file_path_fertilizer, 'rb')
        self.fertilizer_recomendation_model = pickle.load(fertilizer_pickle_in)
        self.fertilizer_df = pd.read_csv(
        "https://raw.githubusercontent.com/Nazif-Malhi/Farmstead_Models/main/ML%20Models%20Farmstead/Dataset/Fertilizer/Fertilizer%20Prediction.csv")

    def predict(self):
        le_soil = preprocessing.LabelEncoder()
        le_crop = preprocessing.LabelEncoder()
        self.fertilizer_df['Soil Type'] = le_soil.fit_transform(self.fertilizer_df['Soil Type'])
        self.fertilizer_df['Crop Type'] = le_crop.fit_transform(self.fertilizer_df['Crop Type'])
        convertedLabelSoil = le_soil.transform([self.data['soil']])
        convertedLabelCrop = le_crop.transform([self.data['crop']])
        pred_data = np.array([[float(self.data['temp']), float(self.data['humi']), float(self.data['moisture']), float(convertedLabelSoil),
                        float(convertedLabelCrop), float(self.data['nitrogen']), float(self.data['phosphorus']), float(self.data['potassium'])]])
        prediction_fertilizer = self.fertilizer_recomendation_model.predict(pred_data)
        return prediction_fertilizer[0]