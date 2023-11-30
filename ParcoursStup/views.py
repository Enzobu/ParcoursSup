from django.shortcuts import render, get_object_or_404

from ParcoursStup.models import School
# Create your views here.

def index(request):
    schools = School.objects.all()

    return render(request, "ParcoursStup/index.html", context={"schools": schools})

def school_detail(request, slug):
    school = get_object_or_404(School, slug=slug)
    return render(request, "ParcoursStup/school-detail.html", context={"school": school})
    # return HttpResponse(f"{school.name}; {school.description}")
