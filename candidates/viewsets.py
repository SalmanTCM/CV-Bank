from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import CandidateSerializer
# from .permissions import IsUserOwnerOrGetAndPostOnly

class CandidateViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsUserOwnerOrGetAndPostOnly]
    queryset = User.objects.all()
    serializer_class = CandidateSerializer

    # def list(self, request, *args, **kwargs):
    #     queryset = User.objects.all()
    #     serializer = CandidateSerializer(queryset, many=True)

