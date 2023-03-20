from datetime import datetime,timedelta
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Student(models.Model):
    student_num = models.IntegerField(unique=True, db_index=True)
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(12)])
    book_limit = models.IntegerField(default=3)
    issued_books = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + " - " + str(self.student_num)


class Book(models.Model):
    title = models.CharField(max_length=255, blank=False)
    author = models.CharField(max_length=255, blank=True)
    copies = models.IntegerField(default=1)
    is_issued = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

def get_expiry():
    return datetime.today() + timedelta(days=7)
 
class IssueBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(default=get_expiry)
    def __str__(self):
        return self.student

