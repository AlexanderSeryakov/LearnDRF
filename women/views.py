from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women, Category
from .serializers import WomenSerializer


def get_home(request):
    return HttpResponse('<h1>Welcome to start page</h1>')


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

# # Класс - представление созданный на основе ModelViewSet
# class WomenViewSet(viewsets.ModelViewSet):
#     """Класс-представления связанный с моделью Women, использует WomenSerializer - сериализатор
#         Имеет полный функционал для чтения, обновления, создания и удаления записи.
#     """
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly, )
#
#     @action(methods=['get'], detail=False)
#     def get_all_category(self, request):
#         """Метод позволяет получить все категории(записи) из таблицы Category"""
#         cats = Category.objects.all()
#         return Response({'cats': [cat.name for cat in cats]})
#
#     @action(methods=['get'], detail=True)
#     def get_one_category(self, request, pk=None):
#         """Метод позволяет получить одну конкретную категорию(запись) из таблицы Category"""
#         if pk is None:
#             return Response({'failed': 'please, enter correct pk(id)'})
#         try:
#             cat = Category.objects.get(pk=pk)
#         except Exception:
#             return Response({'failed': 'please, enter correct pk(id)'})
#         return Response({'cat': cat.name})
