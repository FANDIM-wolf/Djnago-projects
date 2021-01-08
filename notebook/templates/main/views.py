from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import User
from .forms import UserForm
#show all USERS 
def index(request):
	users = User.objects.all()
	return render(request,'main/notebook.html',{'title':'Page of users','users':users})

#to add user with help of method POST
def adduser(request):
	error=""
	if request.method =="POST":
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			
		else:
			error="Form is uncorrect"
		  	

	form=UserForm()
	context = {
		'form':form
	}
	return render(request,'main/addnote.html',context)

#get information about user
def get_user(request,pk):
	user= User.objects.get(pk=pk)
	#user = User.objects.filter(user_id)
	return render(request,'main/user.html',{'user':user})

def search(request):
	result=0
	if request.method == "POST":
		number_1 = request.POST["first"]
		number_2 = request.POST["second"]
		result = int(number_1)*int(number_2)

		
	else:
		HttpResponse("Sorry !")
	return render(request,'main/addnote.html',{'result':result})

	