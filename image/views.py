from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from rest_framework.parsers import MultiPartParser
from .models import *
class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = CategoryImage.objects.all()
    serializer_class = CategrySerializer
    pagination_class= None
    parser_classes= [MultiPartParser, ]
class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductSeriallize
    pagination_class= None
    parser_classes= [MultiPartParser, ]
class AvatarModelViewSet(viewsets.ModelViewSet):
    queryset = AvatarImage.objects.all()
    serializer_class = AvatarSeriallize
    pagination_class= None
    parser_classes= [MultiPartParser, ]