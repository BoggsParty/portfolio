from django.conf.urls import include, url
from . import views

urlpatterns = [
url(r'^$', views.projects, name='projects'),
url(r'^design/$', views.design, name='design'),
url(r'^built/$', views.built, name='built'),
url(r'^(?P<slug>[\w-]+)/$', views.project_main, name='project_main'),
url(r'^(?P<slug>[\w-]+)/(?P<order>[\d-]+)/$', views.project_detail, name='project_detail'),
]