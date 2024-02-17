# In urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('admin/cvs/cv/<int:cv_id>/pdf/', views.view_pdf, name='view_pdf'),
    path('admin/cvs/cv/<int:cv_id>/download/', views.download_pdf, name='download_pdf'),
]
