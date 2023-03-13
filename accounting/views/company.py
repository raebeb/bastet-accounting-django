from urllib import request

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from accounting.models import Company
from accounting.serializers.company_serializer import CompanySerializer


import pdb # for debugging


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        return CompanySerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()

        if self.action == 'list':
            return Company.objects.all()
        if self.action == 'retrieve':
            pass
        if self.action == 'create':
            pass
        else:
            pass
    
    def create(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            print('new_company saved')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('new_company not saved')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)