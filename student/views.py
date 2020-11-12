from django.shortcuts import render
from django.http import HttpResponse
from student.models import Student
from django.core.exceptions import ObjectDoesNotExist

def regv(request):
    return render(request, 'reg.html')

def homev(request):
    return render(request, 'home.html')


def regprocessv(request):
    #1. Get data from html form
    v1 = request.GET.get('n1')
    v2 = request.GET.get('n2')
    v3 = request.GET.get('n3')
    v4 = request.GET.get('n4')


    try:
        x = Student.objects.get(userid=v2)
        return render(request, 'regerror.html')
    except ObjectDoesNotExist:
        obj = Student(fullname=v1, pwd=v3, address=v4, userid=v2)
        obj.save()
        return render(request, 'regsuccess.html')

def showv(request):
    rows = Student.objects.all()
    return render(request, "show.html", {'rows':rows})

def showone(request):
    return render(request, "showone.html")

def showoneprocess(request):
    v1 = request.GET.get('n1')
    try:
        x = Student.objects.get(userid=v1)
        return render(request, 'showoneresult.html', {'row':x})
    except ObjectDoesNotExist:
        return HttpResponse('<h2> userid doesnt exist</h2>')

def updateform(request):
    return render(request, 'updateform.html')

def updateprocess(request):
    v1 = request.GET.get('n1')
    try:
        x = Student.objects.get(userid=v1)
        return render(request, 'updateprocess.html', {'row': x})
    except ObjectDoesNotExist:
        return HttpResponse('<h2> userid doesnt exist</h2>')

def updateprocess1(request):
    v1 = request.GET.get('n1')
    v2 = request.GET.get('n2')
    v3 = request.GET.get('n3')
    v4 = request.GET.get('n4')
    x = Student.objects.get(userid=v2)
    x.fullname = v1
    x.pwd = v3
    x.address = v4
    x.save()
    return render(request, 'updateresult.html')

def deleteform(request):
    return render(request, 'deleteform.html')

def deleteprocess(request):
    v1 = request.GET.get('n1')
    try:
        x = Student.objects.get(userid=v1)
        x.delete()
        return render(request, 'deleteresult.html')
    except ObjectDoesNotExist:
        return HttpResponse('<h2> userid doesnt exist</h2>')