from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.login, name='login'),
    url('remembers/$', views.RememberListView.as_view(), name='remembers'),
    url('index/$', views.index, name='index'),
    url(r'^add/$', views.add_remember, name='add_remember'),
    url(r'remembers/(?P<pk>[a-z0-9-]+)$', views.RememberDetailView.as_view(), name='remember_detail')
]
