from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import User
Dictionary_of_data = {
	'login':"",
	'password':""


}
def index(request):
	login_from_input = ""
	password_from_input = ""
	result_user = ""
	if request.method == "POST":
		login_from_input = request.POST["login_input"]
		password_from_input = request.POST["password_input"]
		result_user = User.objects.all().filter(login_of_user = login_from_input , password_of_user = password_from_input)
		Dictionary_of_data["login"] =login_from_input
		Dictionary_of_data["password"]=password_from_input

	else:
		HttpResponse("Sorry , Account is not defined")

	redirect('test/')
	return render(request,'main/index.html', {'login_from_input':login_from_input,'password_from_input':password_from_input,'result_user':result_user})


def log(request):
	log_tost = Dictionary_of_data["login"]
	pas_tost = Dictionary_of_data["password"]
	return render(request,'main/user.html',{'login':log_tost,'password':pas_tost})


# Create your views here.