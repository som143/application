from django.shortcuts import render
from .forms import regForm,regform1
import requests
import random
from django.http import HttpResponse
from .models import reg
from django.contrib.auth.models import User
from django.contrib.auth import login
def regView(request):
    form = regForm()
    form1 = regform1()
    if request.method == 'POST':
        form = regForm(data=request.POST)
        form1 = regform1(data=request.POST)

        if form.is_valid() and form1.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            profile = form1.save(commit = False)
            profile.user = user
            profile.save()
            return HttpResponse('Register Successfully!!!')

    return render(request,'registration.html',{'form':form,'form1':form1})

def generate_otp(request):
    otp = random.randint(1000,9999)
    if 'number' in request.GET:
        message = "Here is your OTP {} for registration \n Don't share it with anyone".format(otp)
        number = request.GET['number']
        # api = requests.get('http://api.textlocal.in/send/?username=YOUR USERNAME &hash=YOUR HASH KEY&message='+message+'&sender=TXTLCL&numbers=91'+number+'&test=0')

    elif 'user' in request.GET:
        username = request.GET['user']
        check = User.objects.filter(username__iexact=username)
        if len(check) is not 0:
            for i in check:
                id = i.id
            getNumber = reg.objects.get(user_id=id)
            number = repr(getNumber.contact)
            message = "Here is your OTP {} for registration \n Don't share it with anyone".format(otp)
            # api = requests.get('http://api.textlocal.in/send/?username=YOUR USERNAME &hash=YOUR HASH KEY&message='+message+'&sender=TXTLCL&numbers=91'+number+'&test=0')
            strNum =repr(number)
            d = strNum.replace(strNum[:6],'******')
            item1 ='An OTP sent to your {} mobile number \n It may take a minute @'.format(d)
            list = [item1,otp]
            print(list)
            return HttpResponse(list)
        else:
            return HttpResponse('Please Enter Correct Username')

    return HttpResponse(otp)

def loginView(request):
    if request.method == 'POST':
        username = request.POST['un']
        user = User.objects.get(username=username)
        msg = 'Hello {} You are now Logged In to my registration app'.format(user.username)
        login(request,user)
        # return HttpResponse(msg)
        return render(request,'search.html', {'message':msg})  
    return render(request,'login.html')
# def new(request):
#     return render(request, "https://www.mapsofindia.com/worldmap/countries-capitals.html")
