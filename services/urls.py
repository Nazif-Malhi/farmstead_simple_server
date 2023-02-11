from django.urls import path
from .views import *

urlpatterns = [
    path('pest-detection/', PestDetection.as_view()),
    path('crop-disease-detection/', CropDiseaseDetection.as_view()),
    path('simple-crop-prediction/', SimpleCropPrediction.as_view()),
    path('advance-crop-prediction/', AdvanceCropPrediction.as_view()),
    path('fertilizer-prediction/', FertilizerPrediction.as_view()),

]