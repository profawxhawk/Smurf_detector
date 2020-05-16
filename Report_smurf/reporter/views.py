from django.shortcuts import render, redirect
from .forms import rainbow_6form,cf_form
from django.urls import reverse
from .models import R6Final
from .scrap import extract_data
# Create your views here.
def home(request):
    return render(request, 'reporter/Homepage.html')

def check_username(username):
    
    user=R6Final.objects.filter(username=username)
    if len(user)==0:
        return 0
    return 1

def update_user(username,val):
    user=R6Final.objects.get(username=username)
    if val==False:
        user.count_no_smurf+=1
    else:
        user.count_smurf+=1
    
    if user.count_no_smurf>user.count_smurf:
        user.smurf=False
    else:
        user.smurf=True
    user.save()

def add_user(request,username,val):
    data=extract_data(username)
    if data==0:
        return data
    else:
        print(data)
        return 1

def check_username_cf(username):
    
    user=R6Final.objects.filter(username=username)
    if len(user)==0:
        return 0
    return 1

def update_user_cf(username,val):
    user=R6Final.objects.get(username=username)
    if val==False:
        user.count_no_smurf+=1
    else:
        user.count_smurf+=1
    
    if user.count_no_smurf>user.count_smurf:
        user.smurf=False
    else:
        user.smurf=True
    user.save()

def add_user_cf(request,username,val):
    data=extract_data(username)
    if data==0:
        return data
    else:
        print(data)
        return 1



def Rainbow_handler(request):
    if request.method == 'POST':
            form = rainbow_6form(data=request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']
                val=form.cleaned_data['smurf']
                if(check_username(username)==1):
                    update_user(username,val)
                    return render(request, 'reporter/Homepage.html',{'Message':2})
                else:
                    ret=add_user(request,username,val)
                    return render(request, 'reporter/Homepage.html',{'Message':ret+1})
                return redirect(reverse('home'))
            else:
                return redirect(reverse('Rainbow'))

    elif request.method=='GET':
        form = rainbow_6form()
        args = {'form': form}
        return render(request, 'reporter/Rainbow_form.html', args)

def codeforces_handler(request):
    if request.method == 'POST':
            form = cf_form(data=request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']
                val=form.cleaned_data['smurf']
                if(check_username_cf(username)==1):
                    update_user_cf(username,val)
                    return render(request, 'reporter/Homepage.html',{'Message':2})
                else:
                    ret=add_user_cf(request,username,val)
                    return render(request, 'reporter/Homepage.html',{'Message':ret+1})
                return redirect(reverse('home'))
            else:
                return redirect(reverse('Codeforces'))

    elif request.method=='GET':
        form = rainbow_6form()
        args = {'form': form}
        return render(request, 'reporter/codeforces_form.html', args)