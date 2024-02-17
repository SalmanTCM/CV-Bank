from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import CV


def view_pdf(request, cv_id):
    try:
        cv = CV.objects.get(id=cv_id)
    except CV.DoesNotExist:
        return HttpResponse("CV with the provided ID does not exist", status=404)

    if cv.resume:
        with open(cv.resume.path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
        return response
    else:
        return HttpResponse("CV PDF not found")


def download_pdf(request, cv_id):
    cv = get_object_or_404(CV, id=cv_id)

    if cv.resume:
        with open(cv.resume.path, 'rb') as f:
            pdf_content = f.read()

        response = HttpResponse(pdf_content, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{cv.resume.name}"'
        return response
    else:
        return HttpResponse("The CV does not have a resume file.", status=404)