from django.shortcuts import redirect, render, get_object_or_404  

from ParcoursStup.models import School, Formation
from accounts.models import CustomUsers, UserFormation

def index(request):
    return render(request, "ParcoursStup/index.html")

def school_list(request):
    schools = School.objects.all()
    return render(request, "ParcoursStup/school-list.html", context={"schools": schools})

def school_detail(request, slug):
    formations = Formation.objects.all()
    school = get_object_or_404(School, slug=slug)
    return render(request, "ParcoursStup/school-detail.html", context={
        "school": school,
        "formations" : formations})

def postuler(request, slug, formation):
    schools = School.objects.all()  
    # school = get_object_or_404(School, slug=slug)
    # return render(request, "ParcoursStup/school-detail.html", context={"school": school})
    return render(request, "ParcoursStup/postuler.html", context={"schools": schools})

