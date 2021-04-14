from rest_framework import fields, serializers
from django.contrib.auth.hashers import make_password

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):
        if len(data['username']) < 3:
            raise serializers.ValidationError({'username':'minimum 3 chars required for username'})
        if len(data['password']) < 7:
            raise serializers.ValidationError({'password':'minimum 3 chars required for password'})
        if len(data['name']) < 3:
            raise serializers.ValidationError({'name':'minimum 3 chars required for name'})
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            password=make_password(validated_data['password']),
            name=validated_data['name']
        )
        return user
        