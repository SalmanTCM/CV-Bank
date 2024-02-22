#candidate/router
from rest_framework import routers
from .viewsets import CandidateViewSet, CandidateProfileViewSet

app_name = 'candidates'
router = routers.DefaultRouter()
router.register('candidates', CandidateViewSet)
router.register('candidateprofiles', CandidateProfileViewSet)
