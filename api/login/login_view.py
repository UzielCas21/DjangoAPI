from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# View for Login
def login_view(request):
    template_name = "html/auth-login-basic.html" 
    
        # Verifica si el usuario ya esta autenticado
    if request.user.is_authenticated and request.user.is_active:
            return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
    return render(request,template_name)

# View for Regiser
def register_view(request):
    template_name = "html/auth-register-basic.html"
    
    # Verifica si el usuario ya esta autenticado
    if request.user.is_authenticated and request.user.is_active:
            return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, template_name)
        
        if User.objects.filter(username=username).exists():
            messages.error(request,'El usuario ya existe')
            return render(request,template_name)
        
        if User.objects.filter(email=email).exists():
            messages.error(request,'email ya existe')
            return render(request,template_name)
            
        user = User(
            username=username,
            email=email,
            password=make_password(password),
            is_active = 1
        )
        user.save()
        messages.success(request,'Cuenta creada existosamente')
    return render(request,template_name)

# View for forgot the password
def forgot_view(request):
    template_name = "html/auth-forgot-password-basic.html"
    return render(request,template_name)

# View for logout 
def logout_view(request):
    logout(request)
    return redirect('login_vista')