from django.shortcuts import render, redirect,HttpResponse
from member.EmailBackend import  EmailBackend
from django.contrib import  messages
from django.contrib.auth import login, authenticate, logout





def BASE(request):
          return render(request, 'BASE.html')

def login(request):
          return render(request, 'login.html')

def dologin(request):
    if request.method == "POST":
        user =   EmailBackend.authenticate(
            request,
            username=request.POST.get('email'),
            password=request.POST.get('password')
        )

        if user!= None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
             return HttpResponse('This is HOD portal')
            elif user_type == '2':
             return HttpResponse('This is STAFF portal')
            elif user_type == '3':
             return HttpResponse('This is STUDENT portal')
            else:
                messages.error(request,'emailid or password are rong')
                return redirect('login')
        else:
            messages.error(request,'emailid or password are rong')
            return redirect('login')
       
      