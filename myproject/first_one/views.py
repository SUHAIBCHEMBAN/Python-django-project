from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from .forms import SignUpForm


""" this is sign up """


def signup(request):
    
    if request.user.is_authenticated:
        return redirect('firstpage')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['pass1']

            # Create the user
            myuser = get_user_model().objects.create_user(username=username, email=email, password=password)
            myuser.save()

            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, "signup.html", {'form': form})


""" if you authenticated you return frirspage otherwaise return home page"""

def home(request):
    if request.user.is_authenticated:
        return redirect('firstpage')
    return render(request, 'index.html')

    
""" this is user login """


def user_login(request):

    if request.user.is_authenticated:
        return redirect('firstpage')
    
    elif request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:

            login(request, user) 
            return redirect('firstpage')
        
    return render(request, "login.html")


""" this is user logout"""


def user_logout(request):
    if request.user.is_authenticated:
        # Delete the 'visit_count' cookie from the response
        response = redirect('home')
        response.delete_cookie('visit_count')
        # Log out the user
        logout(request)
        return response
    return redirect('home')

