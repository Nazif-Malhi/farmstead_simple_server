from rest_framework import generics
from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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

        queryset_simple = SimpleCropRecomendation.objects.filter(test__farmer=data).select_related('test').order_by('-test__updated_at')
        queryset_advance = AdvanceCropRecomendation.objects.filter(test__farmer=data).order_by('-test__updated_at')
        queryset_fertilizer = FertilizerRecomendation.objects.filter(test__farmer=data).order_by('-test__updated_at')
        queryset_disease = CropDiseaseDetection.objects.filter(test__farmer=data).order_by('-test__updated_at')
        queryset_pest = PestDetection.objects.filter(test__farmer=data).order_by('-test__updated_at')

        serializer_class_simple=SimpleCropByFarmer(queryset_simple,many=True)
        serializer_class_advance=AdvanceCropByFarmer(queryset_advance,many=True)
        serializer_class_fertilizer=FertilizerByFarmer(queryset_fertilizer,many=True)
        serializer_class_disease=CropDiseaseByFarmer(queryset_disease,many=True)
        serializer_class_pest=PestByFarmer(queryset_pest,many=True)

        return Response({'simple_crop_recomendation':serializer_class_simple.data, 
        "advance_crop_recomendation":serializer_class_advance.data,
        "fertilizer_recomendation":serializer_class_fertilizer.data,
        "crop_disease_detection":serializer_class_disease.data,
        "crop_pest_detection":serializer_class_pest.data}, status=200)
