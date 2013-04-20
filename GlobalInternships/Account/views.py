# Create your views here.

from django.http import HttpResponse,Http404
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from Account.models import Profile
from datetime import datetime
from django.db.models import Max
from django.db import IntegrityError
from django.core.mail import send_mail
from mail import mail
from GlobalInternships.Constants import *;

def create(request):
	if request.method=='GET':
		return render_to_response('Account/create.html', RequestContext(request))
	elif request.method=='POST':
		try:
			maxid = User.objects.aggregate(Max('id'))
			newUser = User(id=maxid['id__max']+1,first_name=request.POST['firstname'],last_name=request.POST['lastname'],email=request.POST['email'],password=request.POST['password'],username=request.POST['username'])
			newUser.profile=Profile(activated=False,interests=request.POST['interests'], user=newUser,major=request.POST['major'],email_subscribed='wantemails' in request.POST.keys(), gradmonth=request.POST['gradmonth'], gradyear=request.POST['gradyear']);
			newUser.save();
			newUser.profile.save();

			mail(request.POST['email'],"Account Confirmation",genMessage(request.POST,newUser.id));

			return render(request,'Account/create_success.html', {'firstname':request.POST['firstname'],'email':request.POST['email']});
		except IntegrityError:
			return render(request,'Account/create_error.html', {'message':"Username '{0}' is already taken.".format(request.POST['username'])});
		except Exception:
			return render(request,'Account/create_error.html', {'message':'An unexpected exception has occurred. Please try again later. If the problem persists, please contact gib@ocf.berkeley.edu.'});

#Create helper method
def genMessage(data,user_id):
	dathash=(MYDOMAIN+"/users/activate/{0}").format(user_id)
	return "Hello {0}!\n\nYour Global Internships @ Berkeley member account is ready for activation. Please click the link below to finalize your account creation:\n{1}".format(data['firstname'],dathash)

def activate(request,user_id):
	p=User.objects.all().filter(id=user_id)[0].get_profile()
	p.activated=True
	p.save()
	return render(request,'Account/activate.html', {'firstname':p.firstName});


