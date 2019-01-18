from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .forms import CampaignForm
from .models import Campaign

from .sqlGenerator import getSql, getSelect

# Create your views here.




def home(request):
    if request.method == "POST":
        login_data = request.POST.dict()
        print(login_data)
        user = authenticate(username=login_data["email"], password=login_data["pass"])

        if user is not None:
            login(request, user)
            return redirect("/campaign")
        else:
            return redirect("/")
    else:
        return render(request, "home/page1.html")


@login_required
def campaign(request):
    if request.method == "POST":
        campaign = CampaignForm(request.POST)

        if campaign.is_valid():
            campaign.save()
            return redirect("/criteria")
        else:
            print(campaign.errors)
            return HttpResponse(campaign.errors)
            return redirect("/campaign")
    else:
        print("[DEB] : " + str("Campaign Get Hit......."))
        return render(request, "home/page2.html")

@login_required
def criteria(request):
    if request.method == "POST":
        print(request.POST.dict())
        sql = getSql(request.POST.dict())
        request.session["where"] = sql
        return render(request, "home/page4.html")
        # return HttpResponse("Criteria Post route hit......")
    else:
        return render(request, "home/page3.html")

@login_required
def Logout(request):
    logout(request)
    print("[DEB] : " + str("Logout Success"))
    return redirect("/")

@login_required
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






