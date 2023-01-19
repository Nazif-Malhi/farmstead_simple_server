from django.db import models
from authentication.models import MyUser

class CropBudget(models.Model):
    cropbudget_name = models.CharField(max_length=25)
    farmer = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    
    def __str__(self):
        return self.cropbudget_name

class Income_GrossRevenue(models.Model):
    cash_prize = models.IntegerField()
    expected_yeild = models.SmallIntegerField()
    acres = models.SmallIntegerField()
    govt_payments = models.IntegerField()
    other_income = models.IntegerField()
    cropbudget = models.ForeignKey(CropBudget, on_delete=models.CASCADE)
    
    def cropbudget_name(self):
        return self.cropbudget.cropbudget_name
    def created_at(self):
        return self.cropbudget.created_at
    def updated_at(self):
        return self.cropbudget.updated_at
    def farmer(self):
        return self.cropbudget.farmer.id
    def __str__(self):
        return self.cropbudget

class Expense_VariableCost(models.Model):
    seed = models.IntegerField()
    nitrogen = models.IntegerField()
    phosphorus = models.IntegerField()
    potassium  = models.IntegerField()
    sulfur  = models.IntegerField()
    limestone = models.IntegerField()
    other_fertilizer = models.IntegerField()
    herbicides = models.IntegerField()
    fungicides = models.IntegerField()
    Insecticides = models.IntegerField()
    crop_insurance = models.IntegerField()
    crop_miscellaneous = models.IntegerField()
    suplies = models.IntegerField()
    equipment_fuel = models.IntegerField()
    drying_propane = models.IntegerField()
    repair_machinery = models.IntegerField()
    repair_buildings = models.IntegerField()
    repair_others = models.IntegerField()
    driver_hire = models.IntegerField()
    equipment_hire = models.IntegerField()
    custom_application = models.IntegerField()
    freight_trucking = models.IntegerField()
    storage = models.IntegerField()
    utilities  =models.IntegerField()
    repair = models.IntegerField()
    fuel_electricity = models.IntegerField()
    hired_labour = models.IntegerField()
    intrest_operating = models.IntegerField()
    other = models.IntegerField()
    cropbudget = models.ForeignKey(CropBudget, on_delete=models.CASCADE)

    def cropbudget_name(self):
        return self.cropbudget.cropbudget_name
    def created_at(self):
        return self.cropbudget.created_at
    def updated_at(self):
        return self.cropbudget.updated_at
    def farmer(self):
        return self.cropbudget.farmer.id

    def __str__(self):
        return self.cropbudget

class FixedCost(models.Model):
    farm_insurance = models.IntegerField()
    real_state_taxes  =models.IntegerField()
    land_rent = models.IntegerField()
    interest = models.IntegerField()
    depreciation = models.IntegerField()
    other = models.IntegerField()
    cropbudget = models.ForeignKey(CropBudget, on_delete=models.CASCADE)

    def cropbudget_name(self):
        return self.cropbudget.cropbudget_name
    def created_at(self):
        return self.cropbudget.created_at
    def updated_at(self):
        return self.cropbudget.updated_at
    def farmer(self):
        return self.cropbudget.farmer.id

    def __str__(self):
        return self.cropbudget

class Financing(models.Model):
    income_taxes = models.IntegerField()
    owner_withdrawal = models.IntegerField()
    principle_payment = models.IntegerField()
    other = models.IntegerField()
    cropbudget = models.ForeignKey(CropBudget, on_delete=models.CASCADE)

    def cropbudget_name(self):
        return self.cropbudget.cropbudget_name
    def created_at(self):
        return self.cropbudget.created_at
    def updated_at(self):
        return self.cropbudget.updated_at
    def farmer(self):
        return self.cropbudget.farmer.id

    def __str__(self):
        return self.cropbudget



