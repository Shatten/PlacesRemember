from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RememberForm
from .models import Remember
from django.contrib.auth.models import User
from django.contrib import auth
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
    remembers_list = Remember.objects.filter(id_user=request.user)

    return render(
        request,
        'user_remembers.html',
        context={'remembers_list': remembers_list}
    )

@login_required
def add_remember(request):
    if request.method == 'POST':
        form = RememberForm(request.POST)
        print(request.body)
        if form.is_valid():
            post = form.save(commit=False)
            post.id_user = request.user
            post.map_coordinates = request.POST['map_coordinates']
            post.save()
    else:
        form = RememberForm()
    return render(
        request,
        'add_remember.html',
        context={'form': form}
    )

