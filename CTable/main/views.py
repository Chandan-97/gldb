from django.shortcuts import render
from django.db.models import Q
from .models import *


# Create your views here.

# home
def home(request):
	return render(request, "main/index.html")

def search(request):
	req_query = request.post.dict()

	_name = req_query.get("name")
	_email = req_query.get("email")
	_phoneno = req_query.get("phoneno")

	# query_val = Profile.

	# if email given
	query_val = ""
	if _email:
		query_val = Profile.objects.filter(email=_email).values()
	elif _phoneno:
		query_val = Profile.objects.filter(phoneno=_phoneno).values()

	return render(request, "usersearch.html", query_val)