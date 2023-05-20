from rest_framework import serializers
from .models import Test, SimpleCropRecomendation, AdvanceCropRecomendation, FertilizerRecomendation, CropDiseaseDetection, PestDetection

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields  = ('__all__')

class SimpleCropRecomendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleCropRecomendation
        fields  = ('__all__')
        

class AdvanceCropRecomendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvanceCropRecomendation
        fields  = ('__all__')

class FertilizerRecomendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FertilizerRecomendation
        fields  = ('__all__')


class CropDiseaseDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropDiseaseDetection
        fields  = ('__all__')


class PestDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PestDetection
        fields  = ('__all__')


#################################################################
class SimpleCropByFarmer(serializers.ModelSerializer):
    class Meta:
        model=SimpleCropRecomendation
        fields=['soil_type','temprature','humidity','ph','rain',
        'test','test_name','created_at','updated_at', 'farmer', 'result']

class AdvanceCropByFarmer(serializers.ModelSerializer):
    class Meta:
        model=AdvanceCropRecomendation
        fields=["nitrogen_val", 'phosphorus_val', 'potassium_val', 
        'soil_type','temprature','humidity','ph','rain',
        'test','test_name','created_at','updated_at', 'farmer', 'result']

class FertilizerByFarmer(serializers.ModelSerializer):
    class Meta:
        model=FertilizerRecomendation
        fields=['soil_type','temprature','humidity','moisture',
        'crop_type','nitrogen_val','phosphorus_val','potassium_val',
        'test','test_name','created_at','updated_at', 'farmer', 'result']

class CropDiseaseByFarmer(serializers.ModelSerializer):
    class Meta:
        model=CropDiseaseDetection
        fields=['crop_desease_image',
        'test','test_name','created_at','updated_at', 'farmer', 'result']

class PestByFarmer(serializers.ModelSerializer):
    class Meta:
        model=PestDetection
        fields=['pest_image',
        'test','test_name','created_at','updated_at', 'farmer', 'result']
