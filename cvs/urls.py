# In urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('admin/cvs/cv/<int:cv_id>/pdf/', views.view_pdf, name='view_pdf'),
]
