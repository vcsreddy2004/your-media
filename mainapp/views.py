from django.shortcuts import render,redirect
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

@login_required(login_url='/login')
def home(req):
    return render(req,"index.html")
def loginPage(req):
    errors = [] 
    if req.method == "POST":
        username = req.POST.get('username','').strip()
        password = req.POST.get('password','').strip()
        if username=="":
            errors.append("Username can not left empty")
        elif password=="":
            errors.append("Password can not left empty")
        else:
            if not User.objects.filter(username=username).exists():
                errors.append("User name not exist")
            else:
                user = authenticate(username=username,password=password)
                if user is None:
                    errors.append("invalid password")
                else:
                    login(req,user)
                    return redirect('/')
    return render(req,"login.html",{'errors':errors})
def userLogOut(req):
    logout(req)
    return redirect('/')
def register(req):
    errors = []
    if req.method == "POST":
        first_name = req.POST.get('firstName', '').strip()
        last_name = req.POST.get('lastName', '').strip()
        email = req.POST.get('email', '').strip()
        username = req.POST.get('username', '').strip()
        password = req.POST.get('password', '')
        confirm_password = req.POST.get('confirmPassword', '')
        if not first_name:
            errors.append("First name is required.")
        if not last_name:
            errors.append("Last name is required.")
        if not email:
            errors.append("Email is required.")
        else:
            try:
                validate_email(email)
            except ValidationError:
                errors.append("Invalid email format.")
        
        if not username:
            errors.append("Username is required.")
        if not password:
            errors.append("Password is required.")
        if not confirm_password:
            errors.append("Confirm password is required.")
        if password and confirm_password and password != confirm_password:
            errors.append("Passwords do not match.")
        if not errors:
            if User.objects.filter(username=username).exists():
                errors.append("Username is already taken.")
            elif User.objects.filter(email=email).exists():
                errors.append("Email is already registered.")
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                return redirect('/login') 
    return render(req, "register.html", {'errors': errors})