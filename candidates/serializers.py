# candidates/serializers.py
from rest_framework import serializers
from .models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['url', 'id', 'username', 'first_name', 'last_name', 'email', 'cv']
