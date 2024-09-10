from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'name', 'nickname', 'birthday', 'gender', 'bio']

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if user and user.is_active:
            data['user'] = user
            return data
        raise serializers.ValidationError("Invalid credentials.")

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'nickname', 'birthday', 'gender', 'bio']


# from rest_framework import serializers
# from .models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'name', 'nickname', 'birthday','gender', 'memo']  