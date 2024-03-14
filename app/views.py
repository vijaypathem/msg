from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required
from .models import Message



def HomeView(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        User.objects.create_user(username=username, password=password, email=email)
        return redirect('login')
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inbox')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def ViewMessage(request):
    user_messages = Message.objects.filter(recipient=request.user).order_by('-created_at')
    return render(request, 'inbox.html', {'user_messages': user_messages})


def send_message(request):
    if request.method == 'POST':
        recipient_username = request.POST.get('recipient_username').strip()
        content = request.POST.get('content')
        try:
            recipient = User.objects.get(username=recipient_username)
            Message.objects.create(recipient=recipient, content=content)
            return redirect('home')
        except User.DoesNotExist:
            error_message = 'User does not exist. Please check the username.'
            return render(request, 'send_message.html', {'error_message': error_message})
    return render(request, 'send_message.html')