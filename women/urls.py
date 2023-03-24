from django.urls import path, include
from .views import get_home
from .views import WomenAPIList, WomenAPIUpdate, WomenAPIDestroy
from rest_framework import routers


urlpatterns = [
    # path('api/v1/', include(router.urls)),  # 127.0.0.1:8000/api/v1/women/ + {int}/ - для запросов конкретной записи
    path('', get_home, name='home'),
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendestroy/<int:pk>/', WomenAPIDestroy.as_view()),

]
