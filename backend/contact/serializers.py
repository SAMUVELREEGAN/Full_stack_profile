from rest_framework import serializers
from .models import MyContact

class MyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyContact
        fields = '__all__'
