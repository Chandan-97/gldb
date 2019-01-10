from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from .models import *


# Create your views here.

# home
def home(request):
	return render(request, "main/index.html")

def search(request):
    req_query = request.POST.dict()
    print(req_query)
    _name = req_query.get("name")
    _email = req_query.get("email")
    _phoneno = req_query.get("phoneno")

    # return HttpResponse("Url Hit")

    query_val = ""
    user = {}
    if _email:
        query_val = Profile.objects.filter(email=_email).values()[0]
    elif _phoneno:
        query_val = Profile.objects.filter(phoneno=_phoneno).values()[0]

    return render(request, "main/userlist.html", query_val)

def redirectHome(request):
    response = redirect('/user/home/')
    return response