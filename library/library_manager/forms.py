from django import forms
from django.contrib.auth.models import User
from . import models

class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class StudentForm(forms.ModelForm):
    class Meta:
        model=models.Student
        fields=['student_num', 'first_name', 'last_name', 'grade']

class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=['title','author', 'copies']    
