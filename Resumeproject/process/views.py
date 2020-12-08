from django.shortcuts import render,redirect
from process.models import *
from process.forms import RegistrationForm
from process.models import RegistrationModel
from django.contrib.messages import success

# Create your views here.
def showIndex(request):
    return render(request,'process_templates/main.html')

def registration(request):
    print("========1==========")
    rf=RegistartionForm(request.POST)
    if request.method == "POST":
        print("=======3======")
        if rf.is_valid():
            print("======4====")
            rf.save()
            return redirect('user-otp')   
        else:
            return render(request,'process_templates/registration.html',{"form":rf})
    else:
        print("========2========")
        return render(request,'process_templates/registration.html',{"form":rf})

def userOTP(request):
    return render(request,'process_templates/otp.html')


def validate_otp(request):
    try:
        result=RegistrationModel.objects.get(contact=request.POST.get("t1"),otp=request.POST.get("t2"))
        if result.status == "pending":
            result.status = "approved"
            result.save()
            success(request,"thanks for registration")
            return redirect("conformation")
        elif result.status == "approved":
            success(request,"you have already registered")
            return redirect("conformation")
    except RegistrationModel.DoesNotExist:
        message="Sorry Invalid Details Please try again"
        return render(request,"process_templates/otp.html",{"message":message})


def conformation(request):
    return render(request,"process_templates/conformation.html")


def login(request):
    return render(request,'process_templates/login.html')