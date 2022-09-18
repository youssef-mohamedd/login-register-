

from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('login', views.loginpage,name='login'),
    path('logout', views.logoutUser,name='logoutUser'),
    path('register', views.register,name='register')
]