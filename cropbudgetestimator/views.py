import datetime
from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import transaction
import json
from django.db.models import Sum




from .models import CropBudget, Income_GrossRevenue, Expense_VariableCost, FixedCost, Financing
from .serializers import CropBudgetSerializer, Income_GrossRevenueSerializer, Expense_VariableCostSerializer, FixedCostSerializer, FinancingSerializer, CropSerializer


class CropBudgetList(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = CropBudgetSerializer
    queryset = CropBudget.objects.all()

class CropBudgetDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]

    serializer_class = CropBudgetSerializer
    queryset = CropBudget.objects.all()

class Income_GrossRevenueList(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = Income_GrossRevenueSerializer

    def get_queryset(self):
        queryset = Income_GrossRevenue.objects.all()
        cropbudget = self.request.query_params.get('cropbudget')
        if cropbudget is not None:
            queryset = queryset.filter(cropbudget=cropbudget)
        return queryset

class Income_GrossRevenueDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = Income_GrossRevenueSerializer

    def get_queryset(self):
        queryset = Income_GrossRevenue.objects.all()
        cropbudget = self.request.query_params.get('cropbudget')
        if cropbudget is not None:
            queryset = queryset.filter(cropbudget=cropbudget)
        return queryset


class Expense_VariableCostList(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = Expense_VariableCostSerializer

    def get_queryset(self):
        queryset = Expense_VariableCost.objects.all()
        cropbudget = self.request.query_params.get('cropbudget')
        if cropbudget is not None:
            queryset = queryset.filter(cropbudget=cropbudget)
        return queryset

class Expense_VariableCostDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = Expense_VariableCostSerializer

    def get_queryset(self):
        queryset = Expense_VariableCost.objects.all()
        cropbudget = self.request.query_params.get('cropbudget')
        if cropbudget is not None:
            queryset = queryset.filter(cropbudget=cropbudget)
        return queryset

class FixedCostList(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = FixedCostSerializer

    def get_queryset(self):
        queryset = FixedCost.objects.all()
        cropbudget = self.request.query_params.get('cropbudget')
        if cropbudget is not None:
            queryset = queryset.filter(cropbudget=cropbudget)
        return queryset

class FixedCostDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = FixedCostSerializer

    def get_queryset(self):
        queryset = FixedCost.objects.all()
        cropbudget = self.request.query_params.get('cropbudget')
        if cropbudget is not None:
            queryset = queryset.filter(cropbudget=cropbudget)
        return queryset


class FinancingList(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = FinancingSerializer

    def get_queryset(self):
        queryset = Financing.objects.all()
        cropbudget = self.request.query_params.get('cropbudget')
        if cropbudget is not None:
            queryset = queryset.filter(cropbudget=cropbudget)
        return queryset

class FinancingDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = FinancingSerializer

    def get_queryset(self):
        queryset = Financing.objects.all()
        cropbudget = self.request.query_params.get('cropbudget')
        if cropbudget is not None:
            queryset = queryset.filter(cropbudget=cropbudget)
        return queryset

class GetCropBudgetForFarmers(views.APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, pk=None):
        farmer = request.user.id
        queryset = CropBudget.objects.filter(farmer = farmer).values()

        print(len(queryset))
        prepare_data = []
        if len(queryset) > 0:
            for items in queryset:
                income_gross_revenue = Income_GrossRevenue.objects.filter(cropbudget = items['id']).select_related('cropbudget').values()
                expense_variable_cost = Expense_VariableCost.objects.filter(cropbudget = items['id']).select_related('cropbudget').values()
                fixed_cost =FixedCost.objects.filter(cropbudget = items['id']).select_related('cropbudget').values()
                financing = Financing.objects.filter(cropbudget = items['id']).select_related('cropbudget').values()
                prepare_data.append(
                    [
                    {"crop_budget":items},
                    {"income_gross_revenue":income_gross_revenue},
                    {"expense_variable_cost":expense_variable_cost},
                    {"fixed_cost":fixed_cost},
                    {"financing":financing}
                    ]
                )
                # prepare _ data . append ( income_gross_revenue )


        return Response({'crop_budget_by_farmers':prepare_data}, status=200)

class AddCropBudgetForFarmers(views.APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request, pk=None):
        try:
            with transaction.atomic():
                crop_budget_name = request.data['crop_budget']['cropbudget_name']
                crop_budget_obj = {
                    "cropbudget_name":crop_budget_name,
                    "farmer":request.user
                }
                crop_budget_obj = CropBudget.objects.create(**crop_budget_obj)
                crop_budget_obj.save()
                income_gross_req = request.data['income_gross']
                income_gross_table_data = {
                    'cash_prize':income_gross_req['cash_prize'],
                    'expected_yeild':income_gross_req['expected_yeild'],
                    'acres':income_gross_req['acres'],
                    'govt_payments':income_gross_req['govt_payments'],
                    'other_income':income_gross_req['other_income'],
                    'cropbudget':crop_budget_obj,
                }
                income_gross_obj = Income_GrossRevenue(**income_gross_table_data)
                income_gross_obj.save()

                expense_variable_obj = request.data['expense_variable']
                expense_variable_table_data = {
                    'seed' : expense_variable_obj['seed'],
                    "nitrogen" : expense_variable_obj['nitrogen'],
                    "phosphorus" : expense_variable_obj['phosphorus'],
                    "potassium":   expense_variable_obj['potassium'],
                    "sulfur"  : expense_variable_obj['sulfur'],
                    "limestone" : expense_variable_obj['limestone'],
                    "other_fertilizer" : expense_variable_obj['other_fertilizer'],
                    "herbicides" : expense_variable_obj['herbicides'],
                    "fungicides" : expense_variable_obj['fungicides'],
                    "Insecticides" : expense_variable_obj['Insecticides'],
                    "crop_insurance" : expense_variable_obj['crop_insurance'],
                    "crop_miscellaneous" : expense_variable_obj['crop_miscellaneous'],
                    "suplies" : expense_variable_obj['suplies'],
                    "equipment_fuel" : expense_variable_obj['equipment_fuel'],
                    "drying_propane" : expense_variable_obj['drying_propane'],
                    "repair_machinery" : expense_variable_obj['repair_machinery'],
                    "repair_buildings" : expense_variable_obj['repair_buildings'],
                    "repair_others" : expense_variable_obj['repair_others'],
                    "driver_hire" : expense_variable_obj['driver_hire'],
                    "equipment_hire" : expense_variable_obj['equipment_hire'],
                    "custom_application" : expense_variable_obj['custom_application'],
                    "freight_trucking" : expense_variable_obj['freight_trucking'],
                    "storage" : expense_variable_obj['storage'],
                    "utilities"  : expense_variable_obj['utilities'],
                    "repair" : expense_variable_obj['repair'],
                    "fuel_electricity" : expense_variable_obj['fuel_electricity'],
                    "hired_labour" : expense_variable_obj['hired_labour'],
                    "intrest_operating" : expense_variable_obj['intrest_operating'],
                    "other" : expense_variable_obj['other'],
                    'cropbudget':crop_budget_obj,
                }
                expense_variable_obj  = Expense_VariableCost(**expense_variable_table_data)
                expense_variable_obj.save()

                fixed_cost_obj =  request.data['fixed_cost']
                fixed_cost_table_data = {
                    "farm_insurance" : fixed_cost_obj['farm_insurance'],
                    "real_state_taxes" : fixed_cost_obj['real_state_taxes'],
                    "land_rent"  : fixed_cost_obj['land_rent'],
                    "interest" : fixed_cost_obj['interest'],
                    "depreciation" : fixed_cost_obj['depreciation'],
                    "other" : fixed_cost_obj['other'],
                    'cropbudget':crop_budget_obj,
                }
                fixed_cost_obj = FixedCost(**fixed_cost_table_data)
                fixed_cost_obj.save()

                financing_obj = request.data['financing']
                financing_data_table = {
                    "income_taxes" : financing_obj['income_taxes'],
                    "owner_withdrawal" : financing_obj['owner_withdrawal'],
                    "principle_payment" : financing_obj['principle_payment'],
                    "other" : financing_obj['other'],
                    'cropbudget':crop_budget_obj,
                }
                financing_obj = Financing(**financing_data_table)
                financing_obj.save()
                serializer_class = CropSerializer(data=request.data)
                serializer_class.is_valid()
                return Response({"data":serializer_class.data}, status=200)
        except Exception as e: 
            print(e)
            return Response({"error":"Transaction Roll back account. Following Error !"+str(e)})

class UpdateCropBudgetForFarmers(views.APIView):
    permission_classes=[IsAuthenticated]
    def put(self, request, pk):
        data = request.data

        try:
            with transaction.atomic():
                crop_budget_obj = CropBudget.objects.select_for_update().get(pk = pk)
                income_gross_obj = Income_GrossRevenue.objects.select_for_update().get(cropbudget = pk)
                expense_variable_obj = Expense_VariableCost.objects.select_for_update().get(cropbudget = pk)
                fixed_cost_obj = FixedCost.objects.select_for_update().get(cropbudget = pk)
                financing_obj = Financing.objects.select_for_update().get(cropbudget = pk)

                crop_budget_obj.cropbudget_name = data['crop_budget']['cropbudget_name']
                crop_budget_obj.save()
                income_gross_obj.cash_prize=data['income_gross']['cash_prize']
                income_gross_obj.expected_yeild=data['income_gross']['expected_yeild']
                income_gross_obj.acres=data['income_gross']['acres']
                income_gross_obj.govt_payments=data['income_gross']['govt_payments']
                income_gross_obj.other_income=data['income_gross']['other_income']
                income_gross_obj.save()
                expense_variable_obj.seed = data['expense_variable']['seed']
                expense_variable_obj.nitrogen = data['expense_variable']['nitrogen']
                expense_variable_obj.phosphorus = data['expense_variable']['phosphorus']
                expense_variable_obj.potassium =   data['expense_variable']['potassium']
                expense_variable_obj.sulfur = data['expense_variable']['sulfur']
                expense_variable_obj.limestone = data['expense_variable']['limestone']
                expense_variable_obj.other_fertilizer = data['expense_variable']['other_fertilizer']
                expense_variable_obj.herbicides = data['expense_variable']['herbicides']
                expense_variable_obj.fungicides = data['expense_variable']['fungicides']
                expense_variable_obj.Insecticides = data['expense_variable']['Insecticides']
                expense_variable_obj.crop_insurance = data['expense_variable']['crop_insurance']
                expense_variable_obj.crop_miscellaneous = data['expense_variable']['crop_miscellaneous']
                expense_variable_obj.suplies = data['expense_variable']['suplies']
                expense_variable_obj.equipment_fuel = data['expense_variable']['equipment_fuel']
                expense_variable_obj.drying_propane = data['expense_variable']['drying_propane']
                expense_variable_obj.repair_machinery = data['expense_variable']['repair_machinery']
                expense_variable_obj.repair_buildings = data['expense_variable']['repair_buildings']
                expense_variable_obj.repair_others = data['expense_variable']['repair_others']
                expense_variable_obj.driver_hire = data['expense_variable']['driver_hire']
                expense_variable_obj.equipment_hire = data['expense_variable']['equipment_hire']
                expense_variable_obj.custom_application = data['expense_variable']['custom_application']
                expense_variable_obj.freight_trucking = data['expense_variable']['freight_trucking']
                expense_variable_obj.storage = data['expense_variable']['storage']
                expense_variable_obj.utilities = data['expense_variable']['utilities']
                expense_variable_obj.repair = data['expense_variable']['repair']
                expense_variable_obj.fuel_electricity = data['expense_variable']['fuel_electricity']
                expense_variable_obj.hired_labour = data['expense_variable']['hired_labour']
                expense_variable_obj.intrest_operating = data['expense_variable']['intrest_operating']
                expense_variable_obj.other = data['expense_variable']['other']
                expense_variable_obj.save()
                fixed_cost_obj.farm_insurance = data['fixed_cost']['farm_insurance']
                fixed_cost_obj.real_state_taxes = data['fixed_cost']['real_state_taxes']
                fixed_cost_obj.land_rent = data['fixed_cost']['land_rent']
                fixed_cost_obj.interest = data['fixed_cost']['interest']
                fixed_cost_obj.depreciation = data['fixed_cost']['depreciation']
                fixed_cost_obj.other = data['fixed_cost']['other']
                fixed_cost_obj.save()
                financing_obj.income_taxes =  data['financing']['income_taxes']
                financing_obj.owner_withdrawal =  data['financing']['owner_withdrawal']
                financing_obj.principle_payment = data['financing']['principle_payment']
                financing_obj.other =  data['financing']['other']
                financing_obj.save()
                #response
                crop_budget = CropBudget.objects.filter(pk = pk).values()
                income_gross = Income_GrossRevenue.objects.filter(cropbudget = pk).values()
                expense_variable = Expense_VariableCost.objects.filter(cropbudget = pk).values()
                fixed_cost = FixedCost.objects.filter(cropbudget = pk).values()
                financing = Financing.objects.filter(cropbudget = pk).values()
                
                response_data = []
                response_data.append(
                    [
                                    {"crop_budget":crop_budget},
                                    {"income_gross_revenue":income_gross},
                                    {"expense_variable_cost":expense_variable},
                                    {"fixed_cost":fixed_cost},
                                    {"financing":financing}
                                    ]
                )
                return Response({"Success":response_data})


        except Exception as e:
            return Response({'error':str(e)})

class DeleteCropBudgetForFarmers(views.APIView):
    permission_classes=[IsAuthenticated]
    def delete(self, request, pk):
        crop_budget_valid = CropBudget.objects.filter(pk = pk).values()
        if crop_budget_valid:
            print(crop_budget_valid)
            try:
                with transaction.atomic():
                    income_gross = Income_GrossRevenue.objects.filter(cropbudget = pk).delete()
                    expense_variable = Expense_VariableCost.objects.filter(cropbudget = pk).delete()
                    fixed_cost = FixedCost.objects.filter(cropbudget = pk).delete()
                    financing = Financing.objects.filter(cropbudget = pk).delete()
                    crop_budget = CropBudget.objects.filter(pk = pk).delete()
                    return Response({"Message":"Deleted Successfully"}, status=200)
            except Exception as e: 
                return Response({"error":"Transaction Roll back account. Following Error !"+str(e)})
        else:
            return Response({"Error":"Data Not Found"})

class CropBudgetForPrint(views.APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, pk):
        crop_budget = CropBudget.objects.filter(pk = pk).values()
        if crop_budget:
            income_gross = Income_GrossRevenue.objects.filter(cropbudget = pk).values()
            expense_variable = Expense_VariableCost.objects.filter(cropbudget = pk).values()
            fixed_cost = FixedCost.objects.filter(cropbudget = pk).values()
            financing = Financing.objects.filter(cropbudget = pk).values()
            
            response_data = []
            response_data.append(
                [
                                {"crop_budget":crop_budget},
                                {"income_gross_revenue":income_gross},
                                {"expense_variable_cost":expense_variable},
                                {"fixed_cost":fixed_cost},
                                {"financing":financing}
                                ]
            )
            return Response({"Success":response_data})
        else:
            return Response({"Error":"Data Not Found"})

class ProfitByMonthView(views.APIView):
    def get(self, request, *args, **kwargs):
        profit_by_month = {}

        # Retrieve all crop budgets
        crop_budgets = CropBudget.objects.all()

        # Iterate over each crop budget
        for crop_budget in crop_budgets:
            # Calculate the total income for the crop budget
            total_income = Income_GrossRevenue.objects.filter(cropbudget=crop_budget).aggregate(Sum('cash_prize'))['cash_prize__sum'] or 0

            # Get the variable costs for the crop budget
            variable_costs = Expense_VariableCost.objects.filter(cropbudget=crop_budget)

            # Calculate the total variable costs for the crop budget
            variable_cost_fields = [
                'seed', 'nitrogen', 'phosphorus', 'potassium', 'sulfur', 'limestone',
                'other_fertilizer', 'herbicides', 'fungicides', 'Insecticides',
                'crop_insurance', 'crop_miscellaneous', 'suplies', 'equipment_fuel',
                'drying_propane', 'repair_machinery', 'repair_buildings', 'repair_others',
                'driver_hire', 'equipment_hire', 'custom_application', 'freight_trucking',
                'storage', 'utilities', 'repair', 'fuel_electricity', 'hired_labour',
                'intrest_operating', 'other'
            ]
            total_variable_costs = sum(
                variable_costs.aggregate(Sum(field)).get(field + "__sum") or 0
                for field in variable_cost_fields
            )

            # Get the fixed costs for the crop budget
            fixed_costs = FixedCost.objects.filter(cropbudget=crop_budget)

            # Calculate the total fixed costs for the crop budget
            fixed_cost_fields = ['farm_insurance', 'real_state_taxes', 'land_rent', 'interest', 'depreciation', 'other']
            total_fixed_costs = sum(
                fixed_costs.aggregate(Sum(field)).get(field + "__sum") or 0
                for field in fixed_cost_fields
            )

            # Get the financing costs for the crop budget
            financing_costs = Financing.objects.filter(cropbudget=crop_budget)

            # Calculate the total financing costs for the crop budget
            financing_cost_fields = ['income_taxes', 'owner_withdrawal', 'principle_payment', 'other']
            total_financing_costs = sum(
                financing_costs.aggregate(Sum(field)).get(field + "__sum") or 0
                for field in financing_cost_fields
            )

            # Calculate the total expenses for the crop budget
            total_expenses = total_variable_costs + total_fixed_costs + total_financing_costs

            # Calculate the profit for the crop budget
            total_profit = total_income - total_expenses

            # Get the month and year of the crop budget's creation date
            month = crop_budget.created_at.month
            year = crop_budget.created_at.year

            # Append the profit to the corresponding month and year in the dictionary
            month_year_key = f"{month}-{year}"
            profit_by_month.setdefault(month_year_key, 0)
            profit_by_month[month_year_key] += total_profit

        return Response(profit_by_month)
    