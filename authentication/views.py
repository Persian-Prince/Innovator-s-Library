from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
# Create your views here.


@csrf_exempt
def loginView(request):
    return render(request, 'login.html')

@csrf_exempt
def loggingIn(request):
    if request.method=="POST":    
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')

        if(username1 == "" or password1 == ""):
            messages.info(request, 'Please fill all fields')
            return redirect("/userAccounts/loggingIn/")
        user = authenticate(username=username1, password=password1)
        if user is not None:
            login(request, user)
            return redirect("/books/")

            # A backend authenticated the credentials
        else:
            messages.info(request, 'Inavlid Username/Password')
            return redirect("/userAccounts/loggingIn/")
    return render(request, 'login.html')

@csrf_exempt
def logoutView(request):
    pass


@csrf_exempt
def registerScreenView(request):
    return render(request, 'register.html')


@csrf_exempt
def registerView(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if(username == "" or password == "" or email == "" or firstname == ""):
            messages.info(request, 'Please fill all fields')
            return redirect("/userAccounts/registerScreen/")

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists')
            return redirect("/userAccounts/registerScreen/")

        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists')
            return redirect("/userAccounts/registerScreen/")
        user = User.objects.create_user(
            username, email, password)
        user.last_name = lastname
        user.first_name = firstname
        user.save()
        if user is not None:
            login(request, user)
            return redirect("/books/")
