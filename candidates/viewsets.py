from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import CandidateSerializer,CandidateProfileSerializer
from .permissions import IsUserOwnerOrGetAndPostOnly
from .models import Candidate

class CandidateViewSet(viewsets.ModelViewSet):
    permission_classes = [IsUserOwnerOrGetAndPostOnly]
    queryset = User.objects.all()
    serializer_class = CandidateSerializer

    # def list(self, request, *args, **kwargs):
    #     queryset = User.objects.all()
    #     serializer = CandidateSerializer(queryset, many=True)


class CandidateProfileViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateProfileSerializer