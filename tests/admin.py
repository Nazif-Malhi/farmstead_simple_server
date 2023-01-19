from django.contrib import admin
from .models import Test, SimpleCropRecomendation, AdvanceCropRecomendation, FertilizerRecomendation, CropDiseaseDetection, PestDetection
# Register your models here.

admin.site.register(Test)
admin.site.register(SimpleCropRecomendation)
admin.site.register(AdvanceCropRecomendation)
admin.site.register(FertilizerRecomendation)
admin.site.register(CropDiseaseDetection)
admin.site.register(PestDetection)
