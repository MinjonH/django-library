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
            user = form.save()
            user.set_password(user.password)
            is_superuser = True
            is_staff = True
            user.is_superuser = is_superuser
            user.is_staff = is_staff
            user.save()
            login(request, user)
            return HttpResponseRedirect('afterlogin')
    return render(request,'library/admin_signup.html',{'form':form})

def dashboard_view(request):
    return render(request,'library/dashboard.html')

@login_required(login_url='adminlogin')
def view_books(request):
    books = models.Book.objects.all()
    return render(request,'library/view_books.html',{'books':books})

@login_required(login_url='adminlogin')
def view_students(request):
    students = models.Student.objects.all()
    return render(request,'library/view_students.html',{'students':students})