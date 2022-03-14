from unicodedata import name
from django.urls import  path
from adminpanel import views



urlpatterns = [
    path('',views.AdminHome, name='adminhome'),
    path('adminLogin/',views.adminLogin,name='adminLogin'),
    path('detail/<str:pk>/',views.details,name='detail'),
    path('update/<str:pk>/',views.update_view,name='update'),
    path('useractivation/',views.user_activation,name='useractivation'),
    path('adminLogout/',views.logout_admin,name='adminLogout')
]