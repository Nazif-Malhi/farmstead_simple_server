from django.db import models
from authentication.models import MyUser

class Test(models.Model):
    test_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    farmer = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.test_name

class SimpleCropRecomendation(models.Model):
    soil_type = models.CharField(max_length=25)
    temprature = models.CharField(max_length=25)
    humidity = models.CharField(max_length=25)
    ph = models.CharField(max_length=25)
    rain = models.CharField(max_length=25)
    result = models.CharField(max_length=25)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def test_name(self):
        return self.test.test_name
    def created_at(self):
        return self.test.created_at
    def updated_at(self):
        return self.test.updated_at
    def farmer(self):
        return self.test.farmer.id

    def __str__(self):
        return self.test.test_name

class AdvanceCropRecomendation(models.Model):
    nitrogen_val = models.CharField(max_length=25)
    phosphorus_val = models.CharField(max_length=25)
    potassium_val = models.CharField(max_length=25)
    soil_type = models.CharField(max_length=25)
    temprature = models.CharField(max_length=25)
    humidity = models.CharField(max_length=25)
    ph = models.CharField(max_length=25)
    rain = models.CharField(max_length=25)
    result = models.CharField(max_length=25)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def test_name(self):
        return self.test.test_name
    def created_at(self):
        return self.test.created_at
    def updated_at(self):
        return self.test.updated_at
    def farmer(self):
        return self.test.farmer.id


    def __str__(self):
        return self.test.test_name
class FertilizerRecomendation(models.Model):
    temprature = models.CharField(max_length=25)
    humidity = models.CharField(max_length=25)
    moisture = models.CharField(max_length=25)
    soil_type = models.CharField(max_length=25)
    crop_type = models.CharField(max_length=25)
    nitrogen_val = models.CharField(max_length=25)
    phosphorus_val = models.CharField(max_length=25)
    potassium_val = models.CharField(max_length=25)
    result = models.CharField(max_length=25)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def test_name(self):
        return self.test.test_name
    def created_at(self):
        return self.test.created_at
    def updated_at(self):
        return self.test.updated_at
    def farmer(self):
        return self.test.farmer.id

    def __str__(self):
        return self.test.test_name

class PestDetection(models.Model):
    pest_image = models.ImageField(upload_to="pest_detection")
    result = models.CharField(max_length=25)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def test_name(self):
        return self.test.test_name
    def created_at(self):
        return self.test.created_at
    def updated_at(self):
        return self.test.updated_at
    def farmer(self):
        return self.test.farmer.id

    def __str__(self):
        return self.test.test_name

class CropDiseaseDetection(models.Model):
    crop_desease_image = models.ImageField(upload_to="crop_desease_detection")
    result = models.CharField(max_length=25)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def test_name(self):
        return self.test.test_name
    def created_at(self):
        return self.test.created_at
    def updated_at(self):
        return self.test.updated_at
    def farmer(self):
        return self.test.farmer.id

    def __str__(self):
        return self.test.test_name
