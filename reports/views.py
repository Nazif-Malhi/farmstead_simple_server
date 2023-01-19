from rest_framework import generics
from rest_framework import views
from .models import Report
from .serializers import ReportsSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.

class ReportsList(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]

    serializer_class = ReportsSerializers
    queryset = Report.objects.all()

class ReportsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]

    serializer_class = ReportsSerializers
    queryset = Report.objects.all()

class FarmerReports(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        farmer = request.user.id
        queryset = Report.objects.filter(farmer = farmer).order_by('updated_at')
        serializer_class = ReportsSerializers(queryset, many=True)
        return Response({'result': serializer_class.data}, status=200)

