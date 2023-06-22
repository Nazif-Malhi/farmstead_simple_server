import datetime
from rest_framework import serializers
from .models import CropBudget, Income_GrossRevenue, Expense_VariableCost, FixedCost, Financing

class CropBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropBudget
        fields  = ('__all__')

class Income_GrossRevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income_GrossRevenue
        fields  = ('__all__')

class Expense_VariableCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense_VariableCost
        fields  = ('__all__')

class FixedCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedCost
        fields  = ('__all__')

class FinancingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financing
        fields  = ('__all__')

class CropSerializer(serializers.Serializer):
    crop_budget = CropBudgetSerializer()
    income_gross = Income_GrossRevenueSerializer()
    expense_variable = Expense_VariableCostSerializer()
    fixed_cost = FixedCostSerializer()
    financing = FinancingSerializer()
    
    class Meta:
        fields = ('crop_budget','income_gross', 'expense_variable', 'fixed_cost', 'financing')

