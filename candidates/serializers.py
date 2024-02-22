from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Candidate


class CandidateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['url', 'id', 'user', 'profile_picture']


class CandidateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=False)
    old_password = serializers.CharField(write_only=True, required=False)
    username = serializers.CharField(read_only=True)

    def validate(self, data):
        request_method = self.context['request'].method
        password = data.get('password', None)
        if request_method == 'POST':
            if password == None:
                raise serializers.ValidationError({"info": "Please provide a password"})
        elif request_method == 'PUT' or request_method == 'PATCH':
            old_password = data.get('old_password', None)
            if password is not None and old_password is None:
                raise serializers.ValidationError({"info": "Please provide the old password"})
        return data  # Return validated data here

    def create(self, validated_data):
        password = validated_data.pop('password')
        username = validated_data.pop('username', None)
        user = User.objects.create_user(username=username, **validated_data)
        user.set_password(password)
        user.save()

        return user

    def update(self, instance, validated_data):
        try:
            user = instance
            password = validated_data.pop('password')
            old_password = validated_data.pop('old_password')
            if user.check_password(old_password):
                user.set_password(password)
            else:
                raise Exception("Passwords don't match")
            user.save()
        except Exception as err:
            raise serializers.ValidationError("info", err)
        return super(CandidateSerializer, self).update(instance, validated_data)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'first_name', 'last_name', 'password', 'old_password',]
