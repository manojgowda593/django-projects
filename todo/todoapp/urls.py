from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('',views.home,name='home'),
    path('delete/<int:id>',views.delete,name='delete'),
]
