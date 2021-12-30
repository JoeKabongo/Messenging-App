from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import status


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, min_length=8, max_length=60)
    email = serializers.EmailField(max_length=255)
    username = serializers.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate(self, attrs):
        """Make sure the data provided to create a user is correct"""

        email = attrs.get('email', '')
        username = attrs.get('username', '')
        errors = []
        if User.objects.filter(email=email).exists():
            errors.append({'error': 'Duplicate data',
                          'message':  'Email is already taken'})

        if User.objects.filter(username=username).exists():
            errors.append({'error': 'Duplicate data',
                          'message':  'Username is already taken'})

        if errors:
            raise serializers.ValidationError(
                {"errors": errors})

        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
