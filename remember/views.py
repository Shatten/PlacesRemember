from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RememberForm
from .models import Remember
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


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
def add_remember(request):
    if request.method == 'POST':
        form = RememberForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.id_user = request.user

            post.save()
        return HttpResponseRedirect(reverse('remembers'))
    else:
        form = RememberForm()

    return render(
        request,
        'add_remember.html',
        context={'form': form}
    )


class RememberListView(LoginRequiredMixin, generic.ListView):
    model = Remember

    def get_queryset(self):
        queryset_all = super(RememberListView, self).get_queryset()
        queryset_user = queryset_all.filter(id_user=self.request.user)
        return queryset_user


class RememberDetailView(LoginRequiredMixin, generic.DetailView):
    model = Remember

    def get_queryset(self):
        queryset_all = super(RememberDetailView, self).get_queryset()
        return queryset_all

    def get_context_data(self, **kwargs):
        temp = super(RememberDetailView, self).get_context_data(**kwargs)
        remember = temp.get('remember')
        if remember:
            if remember.id_user != self.request.user:
                temp = None
        return temp



