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
    cash_prize = models.IntegerField(blank=True, null=True)
    expected_yeild = models.SmallIntegerField(blank=True, null=True)
    acres = models.SmallIntegerField(blank=True, null=True)
    govt_payments = models.IntegerField(blank=True, null=True)
    other_income = models.IntegerField(blank=True, null=True)
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
        return self.cropbudget.cropbudget_name

class Expense_VariableCost(models.Model):
    seed = models.IntegerField(blank=True, null=True)
    nitrogen = models.IntegerField(blank=True, null=True)
    phosphorus = models.IntegerField(blank=True, null=True)
    potassium  = models.IntegerField(blank=True, null=True)
    sulfur  = models.IntegerField(blank=True, null=True)
    limestone = models.IntegerField(blank=True, null=True)
    other_fertilizer = models.IntegerField(blank=True, null=True)
    herbicides = models.IntegerField(blank=True, null=True)
    fungicides = models.IntegerField(blank=True, null=True)
    Insecticides = models.IntegerField(blank=True, null=True)
    crop_insurance = models.IntegerField(blank=True, null=True)
    crop_miscellaneous = models.IntegerField(blank=True, null=True)
    suplies = models.IntegerField(blank=True, null=True)
    equipment_fuel = models.IntegerField(blank=True, null=True)
    drying_propane = models.IntegerField(blank=True, null=True)
    repair_machinery = models.IntegerField(blank=True, null=True)
    repair_buildings = models.IntegerField(blank=True, null=True)
    repair_others = models.IntegerField(blank=True, null=True)
    driver_hire = models.IntegerField(blank=True, null=True)
    equipment_hire = models.IntegerField(blank=True, null=True)
    custom_application = models.IntegerField(blank=True, null=True)
    freight_trucking = models.IntegerField(blank=True, null=True)
    storage = models.IntegerField(blank=True, null=True)
    utilities  =models.IntegerField(blank=True, null=True)
    repair = models.IntegerField(blank=True, null=True)
    fuel_electricity = models.IntegerField(blank=True, null=True)
    hired_labour = models.IntegerField(blank=True, null=True)
    intrest_operating = models.IntegerField(blank=True, null=True)
    other = models.IntegerField(blank=True, null=True)
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
        return self.cropbudget.cropbudget_name

class FixedCost(models.Model):
    farm_insurance = models.IntegerField(blank=True, null=True)
    real_state_taxes  =models.IntegerField(blank=True, null=True)
    land_rent = models.IntegerField(blank=True, null=True)
    interest = models.IntegerField(blank=True, null=True)
    depreciation = models.IntegerField(blank=True, null=True)
    other = models.IntegerField(blank=True, null=True)
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
        return self.cropbudget.cropbudget_name

class Financing(models.Model):
    income_taxes = models.IntegerField(blank=True, null=True)
    owner_withdrawal = models.IntegerField(blank=True, null=True)
    principle_payment = models.IntegerField(blank=True, null=True)
    other = models.IntegerField(blank=True, null=True)
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
        return self.cropbudget.cropbudget_name



