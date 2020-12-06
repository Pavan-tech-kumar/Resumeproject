from django import forms
from Resumeproject.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from process.models import *
from process.utils import sendTextMessage
import random
class RegistartionForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    def clean_otp(self):
        cno=self.cleaned_data['contact']
        em=self.cleaned_data['email']
        #otp=self.cleaned_data['otp']
        otp=random.randint(100000,999999)
        print("=====5====")
        message='welcome to RMS and your OTP is '+ str(otp)
        subject="OTP verification"
        sendTextMessage(message,cno)
        send_mail(subject,message,EMAIL_HOST_USER,[em])
        print("======6======")
        return otp
        print(otp)

    class Meta:
        model=RegistrationModel
        exclude=('status',)