from rest_framework import viewsets
from rest_framework import permissions

from accounting.models import Company

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    # serializer_class = CompanySerializer

    def get_serializer_class(self):
        return CompanySerializer
    
    def get_queryset(self):
        return Company.objects.all()
    
    def create(self, request, *args, **kwargs):
        pass
