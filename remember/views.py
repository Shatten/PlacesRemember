from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    return render(
        request,
        'index.html'
    )

def login(request):
    return render(request, 'login.html')

@login_required
def user_remembers(request):
    return render(
        request,
        'user_remembers.html'
    )

@login_required
def add_remember(request):
    return render(
        request,
        'add_remember.html'
    )

