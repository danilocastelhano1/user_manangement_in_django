from rest_framework_jwt.views import JSONWebTokenAPIView

from api.serializers.SignInSerializer import SignInSerializer


class SignInViewset(JSONWebTokenAPIView):
    serializer_class = SignInSerializer

    def post(self, request, *args, **kwargs):
        return super(SignInViewset, self).post(request, *args, **kwargs)
