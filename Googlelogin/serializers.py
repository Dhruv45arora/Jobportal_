from rest_framework import serializers
from .models import CustomUser
from .models import PostedJob,Save_post_By_user

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:#this is the metadata class
        model = CustomUser
        fields = ['id', 'name', 'email', 'phone', 'photo', 'workStatus', 'resume', 'password']
        read_only_fields = ['id']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)  
        user.save()
        return user
    
    
    



class PostedJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostedJob
        fields = '__all__'
        read_only_fields = ['job_id', 'date']



class SavedpostbyuserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Save_post_By_user
        fields='__all__'
        