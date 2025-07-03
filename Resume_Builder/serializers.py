from rest_framework import serializers
from .models import CustomResume

class CustomResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomResume
        fields = '__all__'
