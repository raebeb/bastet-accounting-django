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


class CompanyViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        return CompanySerializer
    
    def get_queryset(self) -> CompanySerializer:
        """
          Returns the appropriate queryset based on the action being performed.
        """
        if self.action == 'list':
            return Company.objects.all()
        if self.action == 'retrieve':
            pass
        if self.action == 'create':
            pass
        else:
            pass
    
    def create(self, request) -> Response:
        """
        Creates a new company instance using the provided request data.

        Args:
            request (Request): The request object.
        
        Returns:
            Responses:
                successful, returns a 201 CREATED.
                fails, returns a 400 BAD REQUEST.
        
        """
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data, context={'organization': request.user.current_organization()})
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
