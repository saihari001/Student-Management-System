from django.shortcuts import redirect, render, HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser
def BASE(request):
    return render(request, 'base.html', locals())

def Login(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    if request.method=='POST':
        user=EmailBackEnd.authenticate(request, username=email, password=password)
        if user!=None:
            login(request, user)
            user_type=user.user_type
            if user_type=='1':
                return redirect('hod_home')
            elif user_type=='2':
                return redirect('Staff_Home')
            elif user_type=='3':
                return redirect("Student_Home")
            else:
                messages.error(request, "Email and Password are invalid.")
                return redirect('Login')
        else:
            messages.error(request, "Email and Password are invalid.")
            return redirect('Login')
    return render(request, "login.html", locals())

def Logout(request):
    logout(request)
    return redirect('Login')

@login_required(login_url='/')
def Profile(request):
    user=CustomUser.objects.get(id = request.user.id)
    return render(request, "profile.html", locals())

@login_required(login_url='/')
def Profile_Update(request):
    try:
        if request.method == 'POST':
            profile_pic=request.FILES.get("profile_pic")
            first_name=request.POST.get("first_name")
            last_name=request.POST.get("last_name")
            password=request.POST.get("password")
            user=CustomUser.objects.get(id=request.user.id)
            user.first_name=first_name
            user.last_name=last_name
            if profile_pic!=None and profile_pic!='':
                user.profile_pic=profile_pic
            if password!=None and password!='':
                user.set_password(password)
            user.save()
            messages.success(request, "Your Profile Updated Successfully.")
            return redirect('Profile')
    except:
        messages.error(request, "Failed to Update your Profile.")
    return render(request, "profile.html", locals())
