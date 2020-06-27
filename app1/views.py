from django.shortcuts import render,HttpResponse
from .models import Employee, Blog


def hello(request):
	b = '<h2>Welcome akshra!</h2>'
	return HttpResponse(b)

def software(request):
	Blog.objects.all()
	return (render, "regex.html",{})

def Employeedata(request):
    a = Employee.objects.all()
    b = Employee.objects.get(pk = 1)
    print(a)
    print(b)

    context = {
    'data' : a,
    'data1' : b,
    'message' :"hey, wass up!",
    }
    return render(request, 'homee.html', context)
    #return HttpResponse(a)
