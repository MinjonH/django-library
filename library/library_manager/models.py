from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django_extensions.db.fields import AutoSlugField

class Student(models.Model):
    student_num = models.IntegerField(unique=True, db_index=True)
    name = models.CharField(max_length=255, blank=False)
    grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(12)])
    book_limit = models.IntegerField(default=3)
    slug = AutoSlugField(populate_from='name') 

    def __str__(self):
        return self.name

class Series(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = AutoSlugField(populate_from='name') 
    
    class Meta:
        verbose_name_plural = 'Series'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255, blank=False)
    author = models.CharField(max_length=255, blank=True)
    copies = models.IntegerField(default=1)
    series = models.ForeignKey(Series, related_name='book', on_delete=models.CASCADE)   
    is_issued = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='title') 

    def __str__(self) -> str:
        return self.title