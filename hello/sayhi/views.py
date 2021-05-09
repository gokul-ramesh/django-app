from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sayhi(request,yourname):
    #return HttpResponse('Hello, World!')
    context={'yourname':yourname}
    return render(request,'temp.html',context)