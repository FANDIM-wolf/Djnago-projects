from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import User
from .models import Accounting
from .models import Post
from .models import Authour
from .forms import UserForm 
import datetime
import random
import time
import datetime
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.datastructures import MultiValueDictKeyError
#dictionary for post likes and another staff
Dictionary_stat_in_project={
	'name_of_user':""
}

#dictionary for log in and get session time
Dictionary_of_data = {
	'login':"",
	'password':"",
	'time':"",
	'hoursStart':0 ,
	'hoursEnd': 0 ,
	'PasswordForFirstFactor':"",
	'PasswordCheckOfUser':""
}
def index(request):
	#####################################
	#prepare code for check of user
	random_text_list = "abcdefghijklmnopuwxyz"
	random_text_result=""
	for i in range(4):
		symbol_for_code = random.choice(random_text_list)
		random_text_result = random_text_result+symbol_for_code
	Dictionary_of_data['PasswordCheckOfUser'] = random_text_result
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
		return redirect('acheck/')

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

	#ADVICE CYCLE 
	advices = ["If you wanna work better , rest more!","To get position higher , get new knowledges and work harder!","Be strong it means be patient "]
	advice = random.choice(advices)

	return render(request,'main/sessions.html',{'time_end':end_of_time,'result_of_job':result,"advice":advice})

# add post and show  it  , we show task actually 
def add_post_and_show_it(request,pk):
	authour=None
	user=None
	get_authour=None
	title=None
	remark=None
	post_created=None
	text="none"
	
	if request.method == "POST":
		title=request.POST['title_post']
		remark=request.POST['text_comment']
		post_created=Post(title_of_post=title,text_of_post=text,remark_of_post=remark)
		post_created.save()
		
	posts = Post.objects.all()					
	return render(request,'main/post.html',{ 'posts': posts })



#to send email 
def send_email_and_get_code(request):
	list_for_code = 'abcdefghijklmnopuwxyz'
	random_string ='' #for future password
	email_of_user='' #email of user
	email_is_sent=None
	email_password_for_check= '' #check password from email 
	for i in range(6):
		a=random.choice(list_for_code)
		random_string=random_string+a
	password_for_first_factor = random_string
	Dictionary_of_data['PasswordForFirstFactor']=password_for_first_factor	 
	message ="Your passcode:"+random_string
	#to get email
	if request.method == "POST":
		email_of_user=request.POST['email_entrance']
	

		email=EmailMessage(
			'First factor of Authrization',
			message, #content of message
			settings.EMAIL_HOST_USER,
			[email_of_user], #email of user for sending 
			)
		email.fail_silently=False
		email.send()
		
		return redirect('password_code/')	
	return render(request,'main/emailcheck.html',{'email':email_of_user,'email_is_sent':email_is_sent})			
#check password code 
def password_code(request):
	password_code = Dictionary_of_data['PasswordForFirstFactor']
	if request.method == "POST":

		email_password_for_check=request.POST['email_password']
		if email_password_for_check == password_code:
			return redirect('adduser/')
	return render(request,'main/password.html')



#check code and second part of autharization
def auth_check(request):
	code_auth_check = ""
	random_text_result_for_check=Dictionary_of_data['PasswordCheckOfUser']
	if request.method == "POST":
		code_auth_check = request.POST['code_check']
		if code_auth_check == random_text_result_for_check:
			return redirect('test/')	

	
	return render(request,'main/auth_check_page.html',{'random_text_result_for_check':random_text_result_for_check,'code_auth_check':code_auth_check}) 	
# Create your views here.
