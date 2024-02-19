from rest_framework import routers
from .viewsets import CandidateViewSet

app_name = 'candidates'
router = routers.DefaultRouter()
router.register('candidates', CandidateViewSet)
