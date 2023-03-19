from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from library_manager import views
from django.contrib.auth.views import LoginView,LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('library_manager/',include('django.contrib.auth.urls') ),
    path('', views.home_view),

    path('admin_signup', views.admin_signup),
    path('admin_login', LoginView.as_view(template_name='library/admin_login.html')),
    path('logout', LogoutView.as_view(template_name='library/logout.html')),
    
    # displays after login
    path('afterlogin', views.dashboard_view),

    #book functions
    path('view_books', views.view_books),
    path('view_students', views.view_students),
]
