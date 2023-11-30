from django.shortcuts import render

from ParcoursStup.models import School
# Create your views here.

def index(request):
    schools = School.objects.all()

    return render(request, "ParcoursStup/index.html", context={"schools": schools})