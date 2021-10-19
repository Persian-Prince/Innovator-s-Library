from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
# Create your views here.


def loginView(request):
    pass

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



def logoutView(request):
    pass


def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@csrf_exempt
def registerScreenView(request):
    return render(request, 'register.html')
