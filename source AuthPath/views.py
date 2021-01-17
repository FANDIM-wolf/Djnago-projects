from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import User
from .forms import UserForm
import datetime
import random
#dictionary for post likes and another staff
Dictionary_stat_in_project={
	'name_of_user':""
}

#dictionary for log in and get session time
Dictionary_of_data = {
	'login':"",
	'password':"",
	'time':""
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
		#in case login and password fields are empty
		if login_from_input == "" or password_from_input == "":
			return redirect('/')
		time_of_start = datetime.datetime.now() #to get date now , with hours 
		Dictionary_of_data["time"]=time_of_start
			
		return redirect('test/')

	else:
		HttpResponse("Sorry , Account is not defined")

	
	return render(request,'main/index.html', {'login_from_input':login_from_input,'password_from_input':password_from_input,'result_user':result_user})

#delete user from bd
def delete_user(request,pk):
	code=None #code of deleting
	user_delete = User.objects.filter(pk=pk)
	user_delete.delete()
	code=random.randint(12300,132345)
	return render(request,'main/delete.html',{'user':user_delete,'code':code})

def log(request):

	log_tost = Dictionary_of_data["login"]
	pas_tost = Dictionary_of_data["password"]
	time = Dictionary_of_data["time"]
	data_of_user =User.objects.all().filter(login_of_user=log_tost,password_of_user=pas_tost)


	return render(request,'main/user.html',{'data':data_of_user,'start_session':time})


#add user in data base with help 	
def adduserindatabase(request):
	form=None
	if request.method =="POST":
		form = UserForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()	
	return render(request,'main/adduser.html',{'form':form})

# Create your views here.
