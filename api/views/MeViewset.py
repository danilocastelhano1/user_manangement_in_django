from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from api.models.User import User
from api.serializers.MeSerializer import MeSerializer


class MeViewset(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = MeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        q = self.queryset.filter(pk=self.request.user.pk)
        return q



