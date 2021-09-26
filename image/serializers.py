from rest_framework import serializers
from .models import *

class CategrySerializer(serializers.ModelSerializer):
  class Meta:
    model = CategoryImage
    fields  = '__all__'

class ProductSeriallize(serializers.ModelSerializer):
  class Meta:
    model = ProductImage
    fields  = '__all__'

class AvatarSeriallize(serializers.ModelSerializer):
  class Meta:
    model = AvatarImage
    fields  = '__all__'