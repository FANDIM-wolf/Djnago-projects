from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import User
from .models import Accounting
from .models import Post
from .models import Authour
from .forms import UserForm , PostForm
import datetime
import random
import time
import datetime
#dictionary for post likes and another staff
Dictionary_stat_in_project={
	'name_of_user':""
}

#dictionary for log in and get session time
Dictionary_of_data = {
	'login':"",
	'password':"",
	'time':"",
	'hoursStart':None ,
	'hoursEnd':  None  
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
		start_of_time = time.ctime()	 
		Dictionary_of_data["time"]=start_of_time
		#############################################
		#get hours of start work
		now = datetime.datetime.now()
		hour_start = now.hour
		Dictionary_of_data["hoursStart"]=hour_start
		##############################################	
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
#get previous data and load user 
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

#over session and make note 
def session_end(request,pk):
	now_time = datetime.datetime.now()
	hour_end = now_time.hour
	start_of_job = Dictionary_of_data["hoursStart"]
	result = hour_end - start_of_job
	employee_to_get_object=User.objects.get(pk=pk)
	exit_of_employee = employee_to_get_object.name_of_user
	#field of getting time
	end_of_time = time.ctime()
	session =Accounting(end_of_session=end_of_time,employee=exit_of_employee) #create line of end session
	session.save()
	return render(request,'main/sessions.html',{'time_end':end_of_time,'result_of_job':result})

# add post and show  it  , we show task actually 
def add_post_and_show_it(request,pk):
	authour=None
	user=None
	get_authour=None
	posts = Post.objects.all()
	if request.method == "POST":
		formPost = PostForm(request.POST)
		if formPost.is_valid():
			formPost.save()
	else:
		formPost = PostForm()
	return render(request,'main/post.html',{'formPost':formPost, 'posts': posts })		

# Create your views here.
