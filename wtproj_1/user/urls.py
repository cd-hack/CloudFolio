from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name='index'),
    path('register/',views.register, name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('employeeHome/',views.employeeHome,name='employeeHome'),
    path('employeeProfile/',views.employeeProfile,name='employeeProfile'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('profile/',views.profile,name='profile'),
    ]