from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import redirect, render

from ParcoursStup.models import School

User = get_user_model()

def signup(request):
    if request.method == 'POST':
        user_type = request.POST.get("user_type")
        if user_type == 'student':
            username = request.POST.get("username")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            password = request.POST.get("password")
            birthday = request.POST.get("birthday")
            report_card = request.POST.get("report_card")

            user = User.objects.create_user(user_type = user_type,
                                            username = username,
                                            first_name = first_name,
                                            last_name = last_name,
                                            email = email,
                                            password = password,
                                            birthday = birthday,
                                            report_card = report_card)

        elif user_type == 'school':            
            name = request.POST.get("name")
            description = request.POST.get("description")
            slug = request.POST.get("name")
            mail = request.POST.get("email")
            address = request.POST.get("address")
            city = request.POST.get("city")
            region = request.POST.get("region")
            department = request.POST.get("department")
            zipCode = request.POST.get("zipCode")
            picture = request.POST.get("picture")
            # picture = request.FILES["picture"]
            
            school = School( name = name,
                            description = description,
                            slug = slug,
                            mail = mail,
                            address = address,
                            city = city,
                            region = region,
                            department = department,
                            zipCode = zipCode,
                            picture = picture)
            school.save()
        
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = User.objects.create_user(school = school,
                                            user_type = user_type,
                                            username = username,
                                            password = password,)
            user.save()

        login(request, user)

        return redirect('index')
    return render(request, 'accounts/signup.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username,
                            password = password)
        print(f"email : {username}, password : {password}")
        if user:
            login(request, user)
            return redirect('index')
    return render(request, 'accounts/login.html')
        

def logout_user(request):
    logout(request)
    return redirect('index')