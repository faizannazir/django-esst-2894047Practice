from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    # render take 3 arguments first request 2nd page to render 3rd additional info dictionary
    return render(request, 'home/welcome.html', {'today':datetime.today(),'name':"Faizan"})
    

def index(request):
    return HttpResponse("Welcome to home page")

@login_required(login_url="/admin")
def authorized(request):
    return render(request,'home/authorize.html',{})