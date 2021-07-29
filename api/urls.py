from django.conf.urls import include, url
from rest_framework import routers

from api.views.SignUpViewset import SignupViewset
from api.views.SignInViewset import SignInViewset
from api.views.MeViewset import MeViewset


router = routers.DefaultRouter()
router.register(r'signup', SignupViewset)
router.register(r'me', MeViewset)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'signin', SignInViewset.as_view())
]
