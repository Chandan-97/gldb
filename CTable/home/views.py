from django.shortcuts import render, HttpResponse, redirect
import json

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

from .CreateQuery import CreateQuery
from .GetQuery import getQuery
from .RunQuery import runQuery
from .FilterCampData import filterCampData

from .models import Campaign


# Create your views here.

def home(request):
    if request.method == "POST":
        login_data = request.POST.dict()
        print(login_data)
        user = authenticate(username=login_data["username"], password=login_data["password"])

        if user is not None:
            login(request, user)
            return redirect("/campaign")
        else:
            return redirect("/")
    else:
        if request.user.is_authenticated:
            return redirect("/campaign")
        return render(request, "home/index_new.html")

@login_required(login_url='/')
def campaign(request):
    if request.is_ajax():
        print(request.POST)
        print("===============")
        query = CreateQuery(request.POST)
        CampInfo = filterCampData(request.POST)
        data = {}

        try:
            obj = Campaign(campaign_name=CampInfo[0], requester_name=CampInfo[1], request_date=CampInfo[2], campaign_start_date=CampInfo[3], campaign_end_date=CampInfo[4], campaign_email=CampInfo[5])
        except Exception as e:
            data["success"] = False
            data["error"] = str(e)
            return HttpResponse(data)

        err = "Campdata not valid"
        if(CampInfo[-1] == False):
            data["success"] = False
        else:
            data["success"] = False

        data["query"] = query

        print("Query : %s"%(query))
        return HttpResponse(query)
    return render(request, "home/product_new.html")

@login_required(login_url="/")
def confirm(request):
    if request.is_ajax():
        query = getQuery(request.POST)
        print(query)
        print("----------------------")
        res = runQuery(request, query, "test")

        if res[0] == False:
            return HttpResponse("Error with Query : "+str(query))

        return HttpResponse(res[2])
    return render(request, "home/product_new.html")

@login_required(login_url='/')
def Logout(request):
    logout(request)
    return redirect("/")

def test(request):
    return HttpResponse("Test Route Hit")






