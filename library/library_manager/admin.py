from django.contrib import admin
from .models import Book, Student, Series

# Register your models here.
admin.site.register(Book)
admin.site.register(Series)
admin.site.register(Student)
