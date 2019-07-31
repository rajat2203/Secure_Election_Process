from django.shortcuts import render

# Create your views here.


def register(request):
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    return render(request, 'login.html')
