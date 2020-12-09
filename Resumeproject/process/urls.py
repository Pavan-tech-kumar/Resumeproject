from django.urls import path
from process import views
from django.contrib import admin

urlpatterns=[
    path('',views.showIndex,name='main_page'),
    path('registration/',views.registration,name='registration'),
    path('user_registration/',views.registration,name='user_registration'),
    #otp uls
    path('user_otp/',views.userOTP,name="user-otp"),
    #conformation
    path("validate_otp/",views.validate_otp,name="validate"),
    path("conformation/",views.conformation,name="conformation"),
    #login
    path('login/',views.login,name="login"),
    path("login_check/",views.login_check,name="login_check"),
    path("view_profile/",views.view_profile,name='view_profile'),
    path("log_out/",views.log_out,name="log_out"),
    
    
]