# candidates/serializers.py
from rest_framework import serializers
from .models import Candidate
from django.contrib.auth.models import User


class CandidateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=False)
    # username = serializers.CharField(write_only=True, required=False)
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user


    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'first_name', 'last_name', 'password']

