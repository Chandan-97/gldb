from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .forms import CampaignForm
from .models import Campaign

from .sqlGenerator import getSql, getSelect

# custom sql queries
from django.db import connection

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
    if request.method == "POST":
        campaign = CampaignForm(request.POST)

        if campaign.is_valid():
            campaign.save()
            return redirect("/criteria")
        else:
            print(campaign.errors)
            return HttpResponse(campaign.errors)
            # return redirect("/campaign")
    else:
        return render(request, "home/product_new.html")

@login_required(login_url='/')
def criteria(request):
    if request.method == "POST":
        print(request.POST.dict())
        sql = getSql(request.POST.dict())
        request.session["where"] = sql
        return render(request, "home/page4.html")
        # return HttpResponse("Criteria Post route hit......")
    else:
        return render(request, "home/page3.html")

@login_required(login_url='/')
def Logout(request):
    logout(request)
    print("[DEB] : " + str("Logout Success"))
    return redirect("/")

@login_required(login_url='/')
def selection(request):
    if request.method == "POST":
        form_data = request.POST.dict()
        print(form_data)
        select = getSelect(form_data)
        print(select)

        sql = select + " [Table Joins] "
        try:
            sql += request.session["where"]
            print("Where Query Found into Session.....")
        except Exception as e:
            print("Where query not found")
            sql += "(WHERE not FOUND), "

        return render(request, "home/page5.html", {"sql": sql})
    else:
        return render(request, "home/page4.html")

@login_required(login_url='/')
def confirm(request):
    if request.method == "POST":
        query = request.POST.dict()
        try:
            query = query["query"]
        except Exception as e:
            print("[confirm] : " + str(query))
            query = "SELECT * FROM rw_service_mst"

        print("[confirm] : " + str(query))

        # for testing only
        # Start
        query = "SELECt * FROM rw_service_mst"
        # End

        print("===========================================")
        print("===========================================")

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
        return HttpResponse("Query Executed")
    else:
        return render(request, "home/page5.html")

def test(request):
    return render(request, "home/product_new.html")






