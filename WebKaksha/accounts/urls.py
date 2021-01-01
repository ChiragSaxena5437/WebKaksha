from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('sign_up/',views.sign_up,name="sign-up"),
    path("logout/", views.logout_request, name="logout"),
    
]
"""
Enter Student Info Form	-http://127.0.0.1:8000/home/Students/form/
Home Page 	            -http://127.0.0.1:8000/home/Students/form/
Login Student	        -http://127.0.0.1:8000/home/accounts/login
Log into Student	    -http://127.0.0.1:8000/home/accounts/login/
account home	        -http://127.0.0.1:8000/home/accounts/
Sign Up Form	        -http://127.0.0.1:8000/home/accounts/sign_up/
"""
