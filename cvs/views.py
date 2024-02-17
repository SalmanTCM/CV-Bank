# from django.shortcuts import render, get_object_or_404
# from .models import CV
#
# def view_pdf(request, cv_id):
#     # Retrieve the CV object based on the provided cv_id
#     cv = get_object_or_404(CV, id=cv_id)
#
#     # Serve the PDF file associated with the CV object
#     pdf_url = cv.resume.url
#
#     return render(request, 'cvs/pdf_viewer.html', {'pdf_url': pdf_url})
from django.http import HttpResponse

from .models import CV
def view_pdf(request, cv_id):
    # Query the CV model to check if a CV with the provided ID exists
    try:
        cv = CV.objects.get(id=cv_id)
    except CV.DoesNotExist:
        # Handle the case where the CV with the specified ID does not exist
        return HttpResponse("CV with the provided ID does not exist", status=404)

    # Proceed with serving the PDF file associated with the CV object
    if cv.resume:
        # Open the PDF file and return it as the HTTP response
        with open(cv.resume.path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
        return response
    else:
        # Return a message if the PDF file is not found
        return HttpResponse("CV PDF not found")
