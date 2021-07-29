from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from api.models.User import User

from api.serializers.UserSerializer import UserSerializer


class SignupViewset(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

