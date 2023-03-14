from urllib import request

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from accounting.models import Company
from accounting.serializers.company_serializer import CompanySerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)


import pdb # for debugging


class CompanyViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        return CompanySerializer
    
    def get_queryset(self):

        if self.action == 'list':
            return Company.objects.all()
        if self.action == 'retrieve':
            pass
        if self.action == 'create':
            pass
        else:
            pass
    
    def create(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




        ### This is ur code
        # serializer = CompanySerializer(data=request.data)
        # if serializer.is_valid():
        #     print(f'REQUEST DATA {request.data}')
        #     body = request.data
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     print('new_company not saved')
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=queryset, many=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)