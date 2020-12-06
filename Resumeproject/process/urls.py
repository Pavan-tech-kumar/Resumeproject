from django.urls import path
from process import views
from django.contrib import admin

urlpatterns=[
    path('',views.showIndex,name='main_page'),
    path('registration/',views.registration,name='registration'),
    path('user_registration/',views.registration,name='user_registration'),
    #otp uls
    path('user_otp/',views.userOTP,name="user-otp"),
    
]