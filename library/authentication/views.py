from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')  
        role = request.POST.get('role', 0)  

        if not all([email, password, first_name, last_name, middle_name]):
            return render(request, 'register.html', {'error': 'Всі поля повинні бути заповнені.'})

        user = CustomUser.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,  
            role=role
        )
        user.is_active = True  
        user.save()
        login(request, user)
        return redirect('books_list')
    return render(request, 'register.html')


from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('books_list')
    return render(request, 'login.html')


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')

