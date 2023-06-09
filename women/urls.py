from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import get_home
from .views import WomenAPIList, WomenAPIUpdate, WomenAPIDestroy
from rest_framework import routers


urlpatterns = [
    path('', get_home, name='home'),
    path('v1/auth-drf/', include('rest_framework.urls')),
    path('v1/women/', WomenAPIList.as_view()),
    path('v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('v1/womendestroy/<int:pk>/', WomenAPIDestroy.as_view()),
    path('v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
