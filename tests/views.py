from rest_framework import generics
from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import transaction
from authentication.models import MyUser


# Create your views here.

from .models import Test, SimpleCropRecomendation, AdvanceCropRecomendation, FertilizerRecomendation, CropDiseaseDetection, PestDetection
from .serializers import TestSerializer, SimpleCropRecomendationSerializer, AdvanceCropRecomendationSerializer, FertilizerRecomendationSerializer , CropDiseaseDetectionSerializer, PestDetectionSerializer,SimpleCropByFarmer, AdvanceCropByFarmer, FertilizerByFarmer, CropDiseaseByFarmer, PestByFarmer

class TestList(generics.ListCreateAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()

class TestDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()

class SimpleCropRecomendationView(generics.ListCreateAPIView):
    serializer_class = SimpleCropRecomendationSerializer
    
    def get_queryset(self):
        queryset = SimpleCropRecomendation.objects.all()
        test = self.request.query_params.get('test')
        if test is not None:
            queryset = queryset.filter(test=test)
        return queryset

class SimpleCropRecomendationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SimpleCropRecomendationSerializer
    queryset = SimpleCropRecomendation.objects.all()

class AdvanceCropRecomendationView(generics.ListCreateAPIView):
    serializer_class = AdvanceCropRecomendationSerializer

    def get_queryset(self):
        queryset = AdvanceCropRecomendation.objects.all()
        test = self.request.query_params.get('test')
        if test is not None:
            queryset = queryset.filter(test=test)
        return queryset

class AdvanceCropRecomendationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AdvanceCropRecomendationSerializer
    queryset = AdvanceCropRecomendation.objects.all()

class FertilizerRecomendationView(generics.ListCreateAPIView):
    serializer_class = FertilizerRecomendationSerializer

    def get_queryset(self):
        queryset = FertilizerRecomendation.objects.all()
        test = self.request.query_params.get('test')
        if test is not None:
            queryset = queryset.filter(test=test)
        return queryset

class FertilizerRecomendationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FertilizerRecomendationSerializer
    queryset = FertilizerRecomendation.objects.all()

class CropDiseaseDetectionView(generics.ListCreateAPIView):
    serializer_class = CropDiseaseDetectionSerializer

    def get_queryset(self):
        queryset = CropDiseaseDetection.objects.all()
        test = self.request.query_params.get('test')
        if test is not None:
            queryset = queryset.filter(test=test)
        return queryset

class CropDiseaseDetectionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CropDiseaseDetectionSerializer
    queryset = CropDiseaseDetection.objects.all()

class PestDetectionView(generics.ListCreateAPIView):
    serializer_class = PestDetectionSerializer

    def get_queryset(self):
        queryset = PestDetection.objects.all()
        test = self.request.query_params.get('test')
        if test is not None:
            queryset = queryset.filter(test=test)
        return queryset

class PestDetectionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PestDetectionSerializer
    queryset = PestDetection.objects.all()





#########################################################################

class GetAllDataForFarmer(views.APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, pk=None):
        data = request.user.id
        queryset_simple = SimpleCropRecomendation.objects.filter(test__farmer=data)
        queryset_advance = AdvanceCropRecomendation.objects.filter(test__farmer=data)
        queryset_fertilizer = FertilizerRecomendation.objects.filter(test__farmer=data)
        queryset_disease = CropDiseaseDetection.objects.filter(test__farmer=data)
        queryset_pest = PestDetection.objects.filter(test__farmer=data)
        
        serializer_class_simple=SimpleCropByFarmer(queryset_simple,many=True)
        serializer_class_advance=AdvanceCropByFarmer(queryset_advance,many=True)
        serializer_class_fertilizer=FertilizerByFarmer(queryset_fertilizer,many=True)
        serializer_class_disease=CropDiseaseByFarmer(queryset_disease,many=True)
        serializer_class_pest=PestByFarmer(queryset_pest,many=True)
        
        result_list = []
        
        result_list.extend(serializer_class_simple.data)
        result_list.extend(serializer_class_advance.data)
        result_list.extend(serializer_class_fertilizer.data)
        result_list.extend(serializer_class_disease.data)
        result_list.extend(serializer_class_pest.data)
        result_list = sorted(result_list, key=lambda x: x['created_at'], reverse=True)

        return Response(result_list, status=200)


class AddDataForFarmers(views.APIView):
    def post(self, request, pk=None):
        try:
            with transaction.atomic():
                test = request.data['test_name']
                
                farmer_id = request.user.is_anonymous
                
                if farmer_id:
                    farmer_id = MyUser.objects.get(email = 'anonymous@gmail.com')
                else:
                    farmer_id = request.user
                
                test_obj = {
                    "test_name":test,
                    "farmer":farmer_id
                }
                test_obj = Test.objects.create(**test_obj)
                test_obj.save()
                
                if test == 'simple-crop-recomendation':

                #SimpleCropRecomendation
                    simple_crop_obj = {
                            'soil_type':request.data['soil_type'],
                            'temprature':request.data['temprature'],
                            'humidity':request.data['humidity'],
                            'ph':request.data['ph'],
                            'rain':request.data['rain'],
                            'result':request.data['result'],
                            'test':test_obj,
                        }
                    simple_crop_obj = SimpleCropRecomendation(**simple_crop_obj)
                    simple_crop_obj.save()
                #AdvanceCropRecomendation
                    
                elif test == "advance-crop-recomendation":
                    print(test)
                    print(request.data['nitrogen_val'])
                    adv_crop_obj = {
                        'nitrogen_val':request.data['nitrogen_val'],
                        'phosphorus_val':request.data['phosphorus_val'],
                        'potassium_val':request.data['potassium_val'],
                        'soil_type' : request.data['soil_type'],
                        'temprature' : request.data['temprature'],
                        'humidity' : request.data['humidity'],
                        'ph' : request.data['ph'],
                        'rain' : request.data['rain'],
                        'result':request.data['result'],
                        'test':test_obj,
                    }
                    adv_crop_obj = AdvanceCropRecomendation(**adv_crop_obj)
                    adv_crop_obj.save()
                #FertilizerRecomendation
                elif test == "fertilizer-recomendation":
                    fertilizer_obj = {
                        'temprature' : request.data['temprature'],
                        'humidity' : request.data['humidity'],
                        'moisture' : request.data['moisture'],
                        'soil_type': request.data['soil_type'],
                        'crop_type': request.data['crop_type'],
                        'nitrogen_val' : request.data['nitrogen_val'],
                        'phosphorus_val' :  request.data['phosphorus_val'],
                        'potassium_val' :  request.data['potassium_val'],
                        'result':request.data['result'],
                        'test':test_obj,
                    }
                    fertilizer_obj = FertilizerRecomendation(**fertilizer_obj)
                    fertilizer_obj.save()
                #PestDetection
                elif test == 'pest-detection':
                    pest_obj  = {
                        'pest_image':request.data['pest_image'],
                         'result':request.data['result'],
                        'test':test_obj,
                    }
                    pest_obj = PestDetection(**pest_obj)
                    pest_obj.save()
                #CropDiseaseDetection
                elif test == "crop-disease-detection":
                    crop_desease_obj = {
                        'crop_desease_image':request.data['crop_desease_image'],
                        'result':request.data['result'],
                        'test':test_obj,
                    }
                    crop_desease_obj = CropDiseaseDetection(**crop_desease_obj)
                    crop_desease_obj.save()
                return Response({"data":test}, status=200)
        except Exception as e:
            print(e)
            return Response({"error":"Transaction Rollback error"})