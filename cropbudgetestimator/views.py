from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



from .models import CropBudget, Income_GrossRevenue, Expense_VariableCost, FixedCost, Financing
from .serializers import CropBudgetSerializer, Income_GrossRevenueSerializer, Expense_VariableCostSerializer, FixedCostSerializer, FinancingSerializer


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
                # prepare_data.append(income_gross_revenue)


        return Response({'crop_budget_by_farmers':prepare_data}, status=200)


