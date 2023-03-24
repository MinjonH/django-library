from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, static
from django.urls import path
from library_manager import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('library_manager/',include('django.contrib.auth.urls') ),
    path('', views.home_view),

    path('signup/', views.admin_signup, name='admin_signup'),
    path('login/', LoginView.as_view(template_name='library/admin_login.html'), name='admin_login'),
    path('logout/', LogoutView.as_view(template_name='library/logout.html'), name='logout'),
    
    # displays after login
    path('dashboard/', views.dashboard_view, name='dashboard'),

    #book functions
    path('books', views.view_books, name='view_books'),
    path('books/issued', views.issued_books, name='issued_books'),
    path('book/add', views.add_book, name='add_book'),
    path('book/issue', views.issue_book, name='issue_book'),
    path('book/update/<int:pk>', views.book_update, name='book_update'),
    path('book/delete/<int:pk>', views.book_delete, name='book_delete'),
    
    path('return/<int:book_issue_id>', views.return_book, name='return_book'),

    #student functions
    path('students', views.view_students, name='view_students'),
    path('student/add', views.add_student, name='add_student'),
    path('student/update/<int:pk>', views.student_update, name='student_update'),
    path('student/delete/<int:pk>', views.student_delete, name='student_delete'),
]
