
from django.contrib import admin
from django.conf.urls import url
from emp.views import home,saverow,getallrows,updaterow,delectrow


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',home),
    url(r'save',saverow),
    url(r'all',getallrows),
    url(r'update',updaterow),
    url(r'delete',delectrow),
]
