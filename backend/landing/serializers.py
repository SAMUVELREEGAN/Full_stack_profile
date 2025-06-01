from rest_framework import serializers
from .models import LandingPara

class LandingParaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingPara
        fields = ['id', 'p1']
