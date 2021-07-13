from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('register/',views.register, name='registration'),
    path('login/',views.login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('employeeHome/',views.employeeHome,name='employeeHome'),
    path('employeeProfile/',views.employeeProfile,name='employeeProfile'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('profile/',views.profile,name='profile'),
    ]