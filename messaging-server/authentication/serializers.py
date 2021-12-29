from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)
    username = serializers.CharField(max_length=30, min_length=4)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate(self, attrs):
        """Make sure the data provided to create a user is correct"""
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':  'Email is already taken'}, 400)
        
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username':  'Username is already taken'}, 400)
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        
        