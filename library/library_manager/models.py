from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Student(models.Model):
    name = models.CharField(max_length=255, blank=False)
    grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(12)])
    book_limit = models.IntegerField(default=3)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

class Series(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

class Book(models.Model):
    title = models.CharField(max_length=255, blank=False)
    author = models.CharField(max_length=255, blank=True)
    series = models.ForeignKey(Series, related_name='book', on_delete=models.CASCADE)   
    is_issued = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255)

    def __str__(self) -> str:
        return self.title