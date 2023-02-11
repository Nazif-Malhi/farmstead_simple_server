from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include('authentication.urls')),
    path("tests/", include('tests.urls')),
    path("crop-budget-estimator/", include('cropbudgetestimator.urls')),
    path("reports/", include('reports.urls')),
    path("models/", include('services.urls')),

]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
