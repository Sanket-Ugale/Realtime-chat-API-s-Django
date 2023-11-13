# serializers.py
from rest_framework import serializers
from .models import *

class GrpMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrpMsg
        fields = '__all__'
