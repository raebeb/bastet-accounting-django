from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from accounting.views.company import CompanyViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)