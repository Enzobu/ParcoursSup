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

def formation(request):
    formations = Formation.objects.all()
    userFormations = UserFormation.objects.all()
    return render(request, "ParcoursStup/formation.html", context={"formations": formations,
                                                                   "userFormations": userFormations})

def add_formation(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        description = request.POST.get("description")
        duration = request.POST.get("duration")
        diploma = request.POST.get("diploma")
        skills = request.POST.get("skills")
        cost = request.POST.get("cost")
        school = request.POST.get("school")

        formation = Formation(
            name = name,
            description = description,
            duration = duration,
            diploma = diploma,
            skills = skills,
            cost = cost,
            slug = name,
            school = School.objects.get(name=school)
        )
        formation.save()
        return redirect('formation')
    
    schools = School.objects.all()
    return render(request, "ParcoursStup/add-formation.html", context={"schools": schools})

