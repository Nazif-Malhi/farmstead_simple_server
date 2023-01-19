from django.urls import path

from .views import ReportsList, ReportsDetail, FarmerReports

urlpatterns = [
    path('reports/', ReportsList.as_view()),
    path('reports/<int:pk>/', ReportsDetail.as_view()),
    path('farmer-reports/', FarmerReports.as_view())
]