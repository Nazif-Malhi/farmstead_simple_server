from django.db import models
from authentication.models import MyUser
from tests.models import Test
from cropbudgetestimator.models import CropBudget

class Report(models.Model):
    reports_name = models.CharField(max_length=25)
    farmer = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, blank=True, null=True, on_delete=models.CASCADE)
    crop_budget_estimator = models.ForeignKey(CropBudget, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.test_name




