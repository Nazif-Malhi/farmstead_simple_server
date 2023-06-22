from django.urls import path

from .views import CropBudgetList, CropBudgetDetails, Income_GrossRevenueList, Income_GrossRevenueDetails, Expense_VariableCostList, Expense_VariableCostDetails, FixedCostList, FixedCostDetails, FinancingList, FinancingDetails, GetCropBudgetForFarmers, AddCropBudgetForFarmers, UpdateCropBudgetForFarmers, CropBudgetForPrint, DeleteCropBudgetForFarmers, ProfitByMonthView

urlpatterns = [
    path('crop-budget/', CropBudgetList.as_view()),
    path('crop-budget/<int:pk>/', CropBudgetDetails.as_view()),
    path('income-gross-revenue/', Income_GrossRevenueList.as_view()),
    path('income-gross-revenue/<int:pk>/', Income_GrossRevenueDetails.as_view()),
    path('expense-variable-cost/', Expense_VariableCostList.as_view()),
    path('expense-variable-cost/<int:pk>/', Expense_VariableCostDetails.as_view()),
    path('fixed-cost/', FixedCostList.as_view()),
    path('fixed-cost/<int:pk>/', FixedCostDetails.as_view()),
    path('financing/', FinancingList.as_view()),
    path('financing/<int:pk>/', FinancingDetails.as_view()),
    ########################################################
    path('get-crops-budget-for-farmers/', GetCropBudgetForFarmers.as_view()),
    path('add-crops-budget-for-farmers/', AddCropBudgetForFarmers.as_view()),
    path('update-crops-budget-for-farmers/<int:pk>/', UpdateCropBudgetForFarmers.as_view()),
    path('get-crop-budget-for-farmers-by/<int:pk>/',CropBudgetForPrint.as_view()),
    path('delete-crop-budget-for-farmers/<int:pk>/',DeleteCropBudgetForFarmers.as_view()),
    path('monthly-profits/', ProfitByMonthView.as_view(), name='monthly-profits'),


]