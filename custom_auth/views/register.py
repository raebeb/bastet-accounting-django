from rest_framework.permissions import AllowAny

from accounting.models import User
from ..serializers.register_serializer import RegisterSerializer
from rest_framework import generics


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer