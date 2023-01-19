from django.contrib import admin
from .models import CropBudget, Income_GrossRevenue, Expense_VariableCost, FixedCost, Financing

# Register your models here.

admin.site.register(CropBudget)
admin.site.register(Income_GrossRevenue)
admin.site.register(Expense_VariableCost)
admin.site.register(FixedCost)
admin.site.register(Financing)


