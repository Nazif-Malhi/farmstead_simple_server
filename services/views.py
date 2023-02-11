from rest_framework import views
from authentication.models import MyUser
from rest_framework.response import Response
from .modelfunctions import *
# Create your views here.

class PestDetection(views.APIView):
    def get(self, request, pk=None):
        farmer_id = request.user.id
        queryset = MyUser.objects.filter(id = farmer_id).values()
        fileObj = request.FILES['upload']
        pest_obj = PestModel(fileObj)
        return Response({'result': pest_obj.predict()}, status=200)

class CropDiseaseDetection(views.APIView):
    def get(self, request, pk=None):
        farmer_id = request.user.id
        queryset = MyUser.objects.filter(id = farmer_id).values()
        fileObj = request.FILES['upload']
        crop_disease_obj = CropDiseaseModel(fileObj)
        return Response({'result': crop_disease_obj.predict()}, status=200)

class SimpleCropPrediction(views.APIView):
    def get(self, request, pk=None):
        farmer_id = request.user.id
        queryset = MyUser.objects.filter(id = farmer_id).values()
        data = json.loads(request.body)
        simple_crop_obj = SimpleCropModel(data)
        return Response({'result': simple_crop_obj.predict()}, status=200)
    
class AdvanceCropPrediction(views.APIView):
    def get(self, request, pk=None):
        farmer_id = request.user.id
        queryset = MyUser.objects.filter(id = farmer_id).values()
        data = json.loads(request.body)
        advance_crop_obj = AdvanceCropModel(data)
        return Response({'result': advance_crop_obj.predict()}, status=200)

class FertilizerPrediction(views.APIView):
    def get(self, request, pk=None):
        data = json.loads(request.body)
        fert_obj = FertilizerModel(data)
        return Response({'result': fert_obj.predict()}, status=200)
