from django.contrib import admin
from django.urls import path, include
from store.views import *

urlpatterns = [
    path('', index, name="index"),
    
    
]
