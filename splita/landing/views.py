from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import RegistrationForm

##test
@login_required(login_url='/login')
def landing(request):
    return render(request, 'landing/landing.html')
##endoftest

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/landing')
    else:
        form = RegistrationForm()

    return render(request, 'landing/signup.html', {"form": form})
 
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/landing')
        else:
            messages.error(request, 'Email or Password does not exist')
    
    return HttpResponse(request, 'landing/login.html')

