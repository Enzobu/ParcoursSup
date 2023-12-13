from django.shortcuts import redirect, render, get_object_or_404  

from ParcoursStup.models import School, Formation
from accounts.models import CustomUsers, UserFormation

def index(request):
    return render(request, "ParcoursStup/index.html")


def school_detail(request, slug):
    formations = Formation.objects.all()
    school = get_object_or_404(School, slug=slug)
