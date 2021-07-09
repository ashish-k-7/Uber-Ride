# In this python file we create the urls for myapp.
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^test',views.test,name='test'),
]