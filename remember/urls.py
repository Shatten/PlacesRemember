from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.login, name='login'),
    url('remembers/', views.user_remembers, name='user_remembers'),
    url('index/', views.index, name='index'),
    url(r'^add_remember/$', views.add_remember, name='add_remember'),
]