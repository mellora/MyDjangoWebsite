from django.shortcuts import render
import django
from .models import Experience, Education, LicensesAndCertifications


# Create your views here.
def homepage(request):
    return render(request=request, template_name='resume/home.html', context={})


def about(request):
    django_version = django.get_version()
    return render(request=request, template_name='resume/about.html', context={'version': django_version})


def resume(request):
    return render(request=request,
                  template_name='resume/resume.html',
                  context={
                      'experience': Experience.objects.all,
                      'education': Education.objects.all,
                      'certs': LicensesAndCertifications.objects.all
                  })
