from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.
def index(request):
    return render(request, 'user/index.html')
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/registration.html', {'form': form})
def login(request):
    return render(request, 'user/login.html')
def dashboard(request):
    return render(request, 'user/dashboard.html')
def employeeHome(request):
    return render(request, 'user/employeeHome.html')
def employeeProfile(request):
    return render(request, 'user/employeeProfile.html')
def portfolio(request):
    return render(request, 'user/portfolio.html') 
def profile(request):
    return render(request, 'user/profile.html')   