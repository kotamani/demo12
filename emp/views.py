from django.shortcuts import render
from emp.models import Emp
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Welcome to Home Page</h1>')


def saverow(request):
    v1 = 'K Ajay'
    v2 = 45000
    v3 = 'ajay'
    v4 = 'apple'
    v5 = 'hyd'
    s1 = Emp(ename=v1, esalary=v2, userid=v3, pswd=v4, address=v5)
    s1.save()
    return HttpResponse('<h1> Ur record is saved </h1>')


def getallrows(request):
    rows = Emp.objects.all()
    print('Type=',type(rows))
    return HttpResponse('<h1>Ur rows arean conosle</h1>')

def updaterow(request):
    row = Emp.objects.get(userid='ajay')
    row.ename='K Ajay'
    row.esalary = 55000
    row.save()
    return HttpResponse('<h1>records is updates</h1>')

def delectrow(request):
    row = Emp.objects.get(userid='ajay')
    row.delete()
    return HttpResponse('<h1>records is delete</h1>')
