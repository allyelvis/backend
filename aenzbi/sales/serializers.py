from rest_framework import serializers
from .models import *

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = <YourModel>
        fields = '__all__'
