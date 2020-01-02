from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mainpage(request) :
    context = {'linktext': 'go to login page!'}
#    return HttpResponse('hello world!')
    return render(request, 'mainpage/mainpage.html', context)
