from django.shortcuts import render,redirect
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from mainapp.forms import PostsForm
from .models import Posts
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from django.core.files.storage import default_storage
@login_required(login_url='/login')
def home(req):
    if req.method == "POST":
        form = PostsForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostsForm()
        objects = Posts.objects.all()
    return render(req,"index.html",{"form":form,"posts":objects})
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
@login_required(login_url="/login")
def profile(req):
    user = {
        'firstName':req.user.first_name,
        'lastName':req.user.last_name,
        'email':req.user.email,
        'username':req.user.username,
        'image':''
    }
    image_filename = f"{req.user.username}.jpg" 
    image_path = os.path.join('profiles', image_filename)
    if default_storage.exists(image_path):
        user['image'] = settings.MEDIA_URL + image_path
    return render(req,'profile.html',{'user':user})
def checkImage(req):
    if req.user.is_authenticated:
        image_filename = f"{req.user.username}.jpg" 
        image_path = os.path.join('profiles', image_filename)
        if default_storage.exists(image_path):
            path = settings.MEDIA_URL + image_path
        else:
            path = ""
    else:
        path=""
    return path
def profileUpload(req):
    if req.user.is_authenticated:
        if req.method == 'POST' and 'image' in req.FILES:
            image = req.FILES['image']
            fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'profiles'))
            filename = f"{req.user.username}.jpg"
            image_path = os.path.join(settings.MEDIA_ROOT, 'profiles', filename)
            if os.path.isfile(image_path):
                os.remove(image_path)
            fs.save(filename, image)
        return redirect('/profile')
    else:
        return redirect('/login')
def profileDelete(req):
    if req.user.is_authenticated:
        filename = f"{req.user.username}.jpg"
        image_path = os.path.join(settings.MEDIA_ROOT, 'profiles', filename)
        if os.path.isfile(image_path):
            os.remove(image_path)
        return redirect('/profile')
    else:
        return redirect('/login')
