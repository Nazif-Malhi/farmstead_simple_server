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