from django.urls import path

from .views import TestList, TestDetail, SimpleCropRecomendationView, SimpleCropRecomendationDetail, AdvanceCropRecomendationView, AdvanceCropRecomendationDetail, FertilizerRecomendationView, FertilizerRecomendationDetail, CropDiseaseDetectionView, CropDiseaseDetectionDetail, PestDetectionView, PestDetectionDetail,GetAllDataForFarmer 

urlpatterns = [
    
    path('test/', TestList.as_view()),
    path('test/<int:pk>/', TestDetail.as_view()),
    path('simplecroprecomendation/', SimpleCropRecomendationView.as_view()),
    path('simplecroprecomendation/<int:pk>/', SimpleCropRecomendationDetail.as_view()),
    path('advancecroprecomendation/', AdvanceCropRecomendationView.as_view()),
    path('advancecroprecomendation/<int:pk>/', AdvanceCropRecomendationDetail.as_view()),
    path('fertilizerrecomendation/', FertilizerRecomendationView.as_view()),
    path('fertilizerrecomendation/<int:pk>/', FertilizerRecomendationDetail.as_view()),
    path('cropdiseasedetection/', CropDiseaseDetectionView.as_view()),
    path('cropdiseasedetection/<int:pk>/', CropDiseaseDetectionDetail.as_view()),
    path('pestdetection/', PestDetectionView.as_view()),
    path('pestdetection/<int:pk>/', PestDetectionDetail.as_view()),
    #############################################################
    path('get-test-for-farmers/', GetAllDataForFarmer.as_view())
]