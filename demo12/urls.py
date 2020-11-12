
from django.contrib import admin
from django.conf.urls import url
from student.views import *

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',homev),
    url(r'homel',homev, name='homel'),
    url(r'regl',regv, name='regl'),
    url(r'regprocessl',regprocessv, name='regprocessl'),
    url(r'show/',showv,name='show'),
    url(r'showone/', showone, name='showone'),
    url(r'showoneprocess/', showoneprocess, name='showoneprocess'),
    url(r'updateform/', updateform, name='updateform'),
    url(r'updateprocess',updateprocess, name='updateprocess'),
    url(r'updateprocess1',updateprocess1, name='updateprocess1'),
    url(r'deleteform',deleteform, name='deleteform'),
    url(r'deleteprocess', deleteprocess, name='deleteprocess'),

]
