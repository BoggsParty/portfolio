from django.conf.urls import include, url
from . import views

urlpatterns = [
url(r'^about/$', views.about, name='about'),
url(r'^contact/$', views.contact, name='contact'),
url(r'^resume/$', views.resume, name='resume'),
url(r'^$', views.home, name='home'),
]