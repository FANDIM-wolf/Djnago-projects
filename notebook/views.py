from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import User
from .forms import UserForm
def index(request):
	users = User.objects.all()
	return render(request,'main/notebook.html',{'title':'Page of users','users':users})

def adduser(request):
	error=""
	if request.method =="POST":
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			redirect('')
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
# Create your views here.
