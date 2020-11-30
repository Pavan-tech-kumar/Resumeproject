from django.urls import path
from process import views
from django.contrib import admin

urlpatterns=[
    path('',views.showIndex,name='main_page'),
    
]