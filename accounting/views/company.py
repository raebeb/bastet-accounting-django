from urllib import request

from rest_framework import viewsets
from rest_framework import permissions

from accounting.models import Company
from accounting.serializers.company_serializer import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_serializer_class(self):
        return CompanySerializer
    
    def get_queryset(self):
        if request.action == 'list':
            return Company.objects.all()
        if request.action == 'retrieve':
            return Company.objects.all()
        if request.action == 'create':
            pass
        return Company.objects.all()
    
    def create(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CompanySerializer(data=request.data)

        return


