from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women, Category
from .serializers import WomenSerializer
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly


def get_home(request):
    """Заглушка для отображения страницы по адресу localhost:8000/api/"""
    return HttpResponse('<h1>Welcome to start page</h1>')


class WomenAPIList(generics.ListCreateAPIView):
    """ Отвечает за отображение всех записей из таблицы Women и создание новых записей.
    Создавать запись может только авторизованный пользователь, иначе только чтение.
    Доступ только авторизованным по токену пользователям """
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    """ Отвечает за отображение конкретной записи таблицы Women и её обновление.
    Обновлять запись может только авторизованный пользователь, который связан с этой записью, иначе только чтение """
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    """ Отвечает за отображение конкретной записи таблицы Women и её удаление.
    Удалять запись может только авторизованный пользователь с правами superuser, иначе только чтение """
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )
