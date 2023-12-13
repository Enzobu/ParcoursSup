from django.shortcuts import redirect, render, get_object_or_404  

from ParcoursStup.models import School
# Create your views here.

def index(request):
    schools = School.objects.all()

    return render(request, "ParcoursStup/index.html", context={"schools": schools})

def school_detail(request, slug):
    formations = Formation.objects.all()
    school = get_object_or_404(School, slug=slug)
