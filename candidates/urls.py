# candidates/urls.py
from django.urls import path
from .views import CandidateRegisterView

urlpatterns = [
    path('register/', CandidateRegisterView.as_view(), name='candidate-register'),
]
