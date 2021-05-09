from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import author,book


def books(request):
    if request.method == 'POST':
        if request.POST.get('author') and request.POST.get('book'):
            p1=author()
            p2=book()
            p1.name= request.POST.get('author')
            p2.name= request.POST.get('book')
            p2.author=p1
            p1.save()
            p2.save()
            return render(request, 'getname.html')  
        else:
        	return render(request, 'error.html')
    else:
    	return render(request, 'getname.html')

def display(request):
	query=book.objects.all()
	return render(request,'display.html',{'query':query})