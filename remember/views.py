from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RememberForm
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
    if request.method == 'POST':
        form = RememberForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.id_user = request.user
            post.save()
    else:
        form = RememberForm()
    return render(
        request,
        'add_remember.html',
        context={'form': form}
    )

