import datetime
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from library_manager import forms, models


# shows the homepage
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('dashboard')
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
            return redirect(dashboard_view)
    return render(request,'library/admin_signup.html',{'form':form})

def dashboard_view(request):
    return render(request,'library/dashboard.html')

@login_required
def view_books(request):
    books = models.Book.objects.all()
    if books:
        return render(request,'library/view_books.html',{'books':books})
    else:
        return render(request,'library/errors.html',{'error': 'No books found'})

@login_required
def issued_books(request):
    book_issues = models.IssueBook.objects.all()
    if book_issues:
        return render(request, 'library/issued.html', {'book_issues': book_issues})
    else:
        return render(request, 'library/errors.html', {'error': 'No books have been issued'})
@login_required
def view_students(request):
    students = models.Student.objects.all()
    if students:
        return render(request,'library/view_students.html',{'students':students})
    else:
        return render(request,'library/errors.html',{'error': 'No students found'})
@login_required
def add_book(request):
    form = forms.BookForm()
    if request.method=='POST':
        form = forms.BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(view_books)
    return render(request,'library/add_book.html',{'form':form})

@login_required
def add_student(request):
    form = forms.StudentForm()
    if request.method=='POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(view_students)
    return render(request,'library/add_student.html',{'form':form})

@login_required
def issue_book(request):
    if request.method == 'POST':
        student_num = request.POST.get('student_num')
        book_title = request.POST.get('book_title')
        if not models.Student.objects.filter(student_num=student_num).exists():
            return render(request, 'library/errors.html', {'error': 'Student with this student number does not exist'})
        else:
            student = models.Student.objects.get(student_num=student_num)

        if not models.Book.objects.filter(title=book_title).exists():
            return render(request, 'library/errors.html', {'error': 'Book with this title does not exist'})
        else:
            book = models.Book.objects.get(title=book_title)
       
        if book.copies > 0:
            if student.issued_books < student.book_limit:
                book.copies -= 1
                book.save()
                student.issued_books += 1
                student.book_limit -= 1
                student.save()
                book_issue = models.IssueBook(student=student, book=book)
                book_issue.save()
                return redirect('issued_books')
            else:
                return render(request, 'library/errors.html', {'error': 'Maximum number of books borrowed'})
        else:
            return render(request, 'library/errors.html', {'error': 'Book not available'})
    else:
        return render(request, 'library/issue_book.html')

@login_required
def return_book(request, book_issue_id):
    issue = models.IssueBook.objects.get(id=book_issue_id)
    book = issue.book
    student = issue.student
    student.book_limit += 1
    student.issued_books -= 1
    student.save()

    book.copies += 1
    book.save()

    issue.delete()
    return redirect(reverse('issued_books'))

@login_required
def student_delete(request, pk):
    student = get_object_or_404(models.Student, student_num=pk)

    if student.issued_books != 0:
        return render(request, 'library/errors.html', {'error': 'This student still has books outstanding. Please return them first.'})
    else:
        student.delete()
    return redirect(view_students)

@login_required
def book_delete(request, pk):
    obj = models.Book.objects.get(id=pk)
    obj.delete()
    return redirect(view_books)

@login_required
def book_update(request, pk):
    obj = models.Book.objects.get(id=pk)
    form = forms.BookForm(instance=obj)
    if request.method == 'POST':
        form = forms.BookForm(data=request.POST, files=request.FILES, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect(view_books)
    return render(request, 'library/add_book.html', locals())

@login_required
def student_update(request, pk):
    obj = models.Student.objects.get(student_num=pk)
    form = forms.StudentForm(instance=obj)
    if request.method == 'POST':
        form = forms.StudentForm(data=request.POST, files=request.FILES, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect(view_students)
    return render(request, 'library/add_student.html', locals())

