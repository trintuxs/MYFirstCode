from django.shortcuts import render
from django.http import HttpResponse

from gyventojai.models import Gyventojas


# Create your views here.



def index(request):
    return HttpResponse("app gyventojas respondina!")



