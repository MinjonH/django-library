from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.models import Group
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from library_manager import forms, models


# shows the homepage
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'library/dashboard.html')

def admin_signup(request):
    form=forms.AdminSigupForm()
    if request.method=='POST':
        form=forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()


            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)

            return HttpResponseRedirect('adminlogin')
    return render(request,'library/admin_signup.html',{'form':form})

def dashboard_view(request):
    return render(request,'library/dashboard.html')
