from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.


def logout(request):
    auth.logout(request)
    return redirect('/')


def govote(request):
    return render(request, 'vote.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        u = User.objects.get(username=username)

        if user is not None:
            # auth.login(request, user)
            # return redirect('govote')
            if  user.is_staff == False:
                u.is_staff = True
                u.save()
                auth.login(request, user)
                return redirect('govote')

            else:
                messages.info(request, 'You have Already Voted')
                return redirect('signin')


            
        else:
            messages.info(request, 'Invalid')
            return redirect('signin')
    else:
        return render(request, 'sign-in.html')


def signin(request):
    return render(request, 'sign-in.html')


def signup(request):
    return render(request, 'signup.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']


        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                print('username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                print('email taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('signin')

        else:
            messages.info(request, 'password not matching....')
            print('Password not matching....')
            return redirect('signup')
        return redirect('/')

    else:
        return render(request, 'signup.html')
