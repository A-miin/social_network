from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserModel
        fields = (
            'email',
            'password',
            'password2',
        )

    def create(self, validated_data):
        user = UserModel.objects.create(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        attrs['password'] = make_password(attrs['password'])

        return attrs
