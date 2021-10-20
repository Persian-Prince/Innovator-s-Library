from django.urls import path
from authentication.views import *

urlpatterns = [
    path('login/', loginView, name="login"),
    path('loggingIn/', loggingIn, name="loggingIn"),
    path('registerScreen/', registerScreenView, name="registerScreen"),
    path('register/', registerView, name="register"),
    
]
