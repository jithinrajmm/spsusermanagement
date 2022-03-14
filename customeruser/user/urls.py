from unicodedata import name
from django.urls import path 
from user import views


urlpatterns = [
    path('',views.home, name='home'),
    path('register/',views.userCreation,name='register'),
    path('login/',views.userLogin,name='login'),
    path('logout/',views.logoutView,name='logout'),
    ]