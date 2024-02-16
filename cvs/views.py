# In views.py
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import CV


def view_pdf(request, cv_id):
    # Retrieve the CV object based on the provided cv_id
    cv = get_object_or_404(CV, id=cv_id)

    # Serve the PDF file associated with the CV object
    if cv.resume:
        # Open the PDF file and return it as the HTTP response
        with open(cv.resume.path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
        return response
    else:
        # Return a message if the PDF file is not found
        return HttpResponse("CV PDF not found")
