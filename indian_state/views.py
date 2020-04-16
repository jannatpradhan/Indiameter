import json
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
import requests


# Create your views here.
def home(request):
    req = requests.get('https://api.covid19india.org/data.json')
    data = req.json()
    s=data['statewise']
    return render(request,'index.html',{'s':s})

def check_symptom(request):
    return render(request,'check_symptom.html')


