from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def bview(request):
    if request.GET['hub.verify_token'] == '121fa08134':
        return HttpResponse(request.GET['hub.challenge'])
    else :
        return HttpResponse('Invalid Token !')

def home(request):
    return render(request, 'index.html')