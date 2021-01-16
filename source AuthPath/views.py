from django.shortcuts import render , redirect
from django.http import HttpResponse

def index(request):
	login_from_input = ""
	password_from_input = ""
	if request.method == "POST":
		login_from_input = request.POST["login_input"]
		password_from_input = request.POST["password_input"]

	else:
		HttpResponse("Sorry , Account is not defined")


	return render(request,'main/index.html', {'login_from_input':login_from_input,'password_from_input':password_from_input})


# Create your views here.
