from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer
from .models import Data
from .forms import Employee, UserUpdateForm
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    @loginrequird
    def profile(request):
        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            if u_form.is_valid():
                u_form.save()

        else:
            u_form = UserUpdateForm(instance=request.user)
             
        context ={
            'u_form': u_form,

        }
        subject = 'Profile Updation mail'
        message = 'Hey' + reg.first_name +, Your Profile is updated.
        to = user_email_id
        send_mail(
            subject,
            message,
            'abhinavk806@gmail.com'
            [to],

 
        )
        return render(request,'',context)


    def profile_reg(request):
        if request.method == 'POST':
            fm = Employee(request.POST) 
            if fm.is_valid():
                nm = fm.cleaned_data['first_name']
                lm = fm.cleaned_data['last_name']
                cn = fm.cleaned_data['company_name']
                em = fm.cleaned_data['email_id']
                pn = fm.cleaned_data['phone_number']
                pw = fm.cleaned_data['password']
                cpw = fm.cleaned_data['confirm_password']

                reg = Data(first_name=nm ,last_name=lm,company_name=cn,email_id=em,phone_number=pn,password=pw,confirm_password=cpw)
                reg.save()
                fm = Employee() 

        else:
            fm = Employee() 

        return render(request,{'form':fm})
        profile_reg.reg = reg
        profile.save()
        #to send email notifications
        subject = 'Thanks for register'
        message = 'Hey' + reg.first_name +, You are now succesfully registered with us.
        to = user_email_id
        send_mail(
            subject,
            message,
            'abhinavk806@gmail.com'
            [to],

 
        )
        def password_reset(request):
            subject = 'Password Rest Mail'
            message = Someone asked for password reset for email {{ email }}. Follow the linkbelow:
            {{ protocol }}://{{ domain }}{% url "password_reset_confirm" uidb64=uid token=token %}Your username, in case you've forgotten: {{ user.get_first_name }}
            to = user_email_id
            send_mail(
                subject,
                message,    
                'abhinavk806@gmail.com'
                [to],
            )
           message = 'passwod has been changed'
        
    

        

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

