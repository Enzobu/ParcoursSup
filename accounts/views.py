from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import redirect, render

User = get_user_model()

def signup(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        password = request.POST.get("password")
        user = User.objects.create_user(username = name,
                                        password = password)
        login(request, user)
        return redirect('index')
    
    return render(request, 'accounts/signup.html')

def login_user(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        password = request.POST.get("password")
        user = authenticate(username = name, 
                            password = password)
        if user:
            login(request, user)
            return redirect('index')
    return render(request, 'accounts/login.html')
        

def logout_user(request):
    logout(request)
    return redirect('index')