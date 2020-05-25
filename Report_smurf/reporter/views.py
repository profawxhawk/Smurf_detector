from django.shortcuts import render, redirect
from .forms import rainbow_6form,cf_form
from django.urls import reverse
from .models import R6Final,Cffinal
from .scrap import extract_data
from .scrapcf import get_all_data
import math
# Create your views here.
minMaxVal = {"Level":[18,564], "Best MMR Rating":[0,9007], "Rank":[0,22], "Avg Seasonal MMR":[1966,9007],
"Wins":[19,12438], "Win %":[32.3,100], "Kills":[0.11,53.25], "KD":[0.11,53.25], "Deaths":[48,70247], 
"Headshots":[34,45749], "Losses":[0,7813], "Time Played":[0,5731], "Matches Played":[32,19214],
"Melee Kills":[0,13203], "Blind Kills":[0,170], "Time Played_casual":[0,1974], "Losses_casual":[0,3008],
"Matches_casual":[0,8073], "Deaths_casual":[1,30435], "Kills_casual":[0,34521], "Win%_casual":[0,100], "KD_casual":[0,37],
"Kills/match_casual":[0,3.77], "Time Played_ranked":[0,5169], "Wins_ranked":[0, 8962], "Losses_ranked":[0,7601],
"Matches_ranked":[0,15724], "Deaths_ranked":[0,68454], "Kills_ranked":[13,77020], "Win%_ranked":[0,100],
"KD_ranked": [0.07,124], "Kills/match_ranked":[0.24,21], "Kills/min_ranked":[0.02, 4.67] }

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
def logit(val):
    return val
def convert_type(arr):
    Rank_list={'NO_RANK':0,'COPPER V':1,'COPER IV':2,'COPPER III':3,'COPPER II':4,'COPPER I':5,'BRONZE IV':6,'BRONZE III':7,'BRONZE II':8,'BRONZE I':9,'SILVER V':10,'SILVER IV':11,'SILVER III':12,'SILVER II':13,'SILVER I':14,'GOLD IV':15,'GOLD III':16,'GOLD II':17,'GOLD I':18,'PLATINUM III':19,'PLATINUM II':20,'PLATINUM II':21,'DIMOND':22,'CHAMPION':23}
    arr[1]=logit(float(arr[1].replace(',','')))
    arr[2]=logit(float(arr[2].replace(',','')))
    arr[3]=Rank_list[arr[3]]
    arr[4]=logit(float(arr[4].replace(',','')))
    arr[5]=logit(float(arr[5].replace(',','')))
    arr[6]=logit(float(arr[6][:-1].replace(',','')))
    arr[7]=logit(float(arr[7].replace(',','')))
    arr[8]=logit(float(arr[8].replace(',','')))
    arr[9]=logit(float(arr[9].replace(',','')))
    arr[10]=logit(float(arr[10].replace(',','')))
    arr[11]=logit(float(arr[11].replace(',','')))
    arr[12]=logit(float(arr[12][:arr[12].find('H')].replace(',','')))
    arr[13]=logit(float(arr[13].replace(',','')))
    arr[14]=logit(float(arr[14].replace(',','')))
    arr[15]=logit(float(arr[15].replace(',','')))
    arr[16]=logit(float(arr[16][:arr[16].find('H')].replace(',','')))
    arr[17]=logit(float(arr[17].replace(',','')))
    arr[18]=logit(float(arr[18].replace(',','')))
    arr[19]=logit(float(arr[19].replace(',','')))
    arr[20]=logit(float(arr[20].replace(',','')))
    arr[21]=logit(float(arr[21][:-1].replace(',','')))
    arr[22]=logit(float(arr[22].replace(',','')))
    arr[23]=logit(float(arr[23].replace(',','')))
    arr[24]=logit(float(arr[24][:arr[24].find('H')].replace(',','')))
    arr[25]=logit(float(arr[25].replace(',','')))
    arr[26]=logit(float(arr[26].replace(',','')))
    arr[27]=logit(float(arr[27].replace(',','')))
    arr[28]=logit(float(arr[28].replace(',','')))
    arr[29]=logit(float(arr[29].replace(',','')))
    arr[30]=logit(float(arr[30][:-1].replace(',','')))
    arr[31]=logit(float(arr[31].replace(',','')))
    arr[32]=logit(float(arr[32].replace(',','')))
    arr[33]=logit(float(arr[33].replace(',','')))
    return arr

def norm(data):
    temp=[0]
    for i,j in zip(data[1:34],minMaxVal.keys()):
        j=minMaxVal[j]
        if i < j[0]:
            j[0]=i
        if i>j[1]:
            j[1]=i
        i=(i-j[0])/(j[1])
        temp.append(i)
    return temp

def add_user(request,username,val):
    data=extract_data(username)
    if data==0:
        return data
    else:
        data=convert_type(data)
        data=norm(data)
        temp=R6Final.objects.all().last()
        r6=R6Final()
        r6.field1=temp.field1+1
        r6.username = username
        r6.level =  data[1]
        r6.best_mmr_rating =  data[2]
        r6.ranking =  data[3]
        r6.avg_seasonal_mmr =  data[4]
        r6.wins =  data[5]
        r6.win_p =  data[6]
        r6.kills =  data[7]
        r6.kd =  data[8]
        r6.deaths =  data[9]
        r6.headshots =  data[10]
        r6.losses =  data[11]
        r6.time_played = data[12]
        r6.matches_played =  data[13]
        r6.melee_kills =  data[14]
        r6.blind_kills =  data[15]
        r6.time_played_casual = data[16]
        r6.losses_casual =  data[17]
        r6.matches_casual =  data[18]
        r6.deaths_casual =  data[19]
        r6.kills_casual =  data[20]
        r6.win_p_casual =  data[21]
        r6.kd_casual =  data[22]
        r6.killsmin_casual =  data[23]
        r6.time_played_rankinged =  data[24]
        r6.wins_rankinged =  data[25]
        r6.losses_rankinged =  data[26]
        r6.matches_rankinged =  data[27]
        r6.deaths_rankinged =  data[28]
        r6.kills_rankinged =  data[29]
        r6.win_p_rankinged =  data[30]
        r6.kd_rankinged =  data[31]
        r6.killsmatch_rankinged =  data[32]
        r6.killsmin_rankinged =  data[33]
        if val==False:
            r6.smurf = False
            r6.count_no_smurf = 1
            r6.count_smurf = 0
        else:
            r6.smurf = True
            r6.count_no_smurf = 0
            r6.count_smurf = 1
        r6.save()
        return 1

def check_username_cf(username):
    
    user=Cffinal.objects.filter(handle=username)
    if len(user)==0:
        return 0
    return 1

def update_user_cf(username,val):
    user =Cffinal.objects.get(handle=username)
    if val==False:
        user.count_no_smurf+=1
    else:
        user.count_smurf+=1
    
    if user.count_no_smurf>user.count_smurf:
        user.smurf=False
    else:
        user.smurf=True
    # user.save()

def add_user_cf(request,username,val):
    data=get_all_data(username)
    if data==0:
        return data
    else:
        cf=Cffinal()
        temp=Cffinal.objects.all().last()

        cf.field1=temp.field1+1
        cf.handle=username
        cf.firstname=data[0]
        cf.lastname=data[1]
        cf.city=data[2]
        cf.maxrank =data[3]
        cf.maxrating =int(data[4])
        cf.contribution = int(data[5])
        cf.friendofcount = int(data[6])
        cf.upvotes = float(data[7])
        cf.ac_percentage = float(data[8])
        cf.hashing =int(data[9])
        cf.bitmasks = int(data[10])
        cf.ternary_search = int(data[11])
        cf.flows = int(data[12])
        cf.string_suffix_structures = int(data[13])
        cf.fft = int(data[14])
        cf.meetinthemiddle =int(data[15])
        cf.intelligence =float(data[16])
        if val==False:
            cf.smurf = False
            cf.count_no_smurf = 1
            cf.count_smurf = 0
        else:
            cf.smurf = True
            cf.count_no_smurf = 0
            cf.count_smurf = 1
        cf.save()
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
        form = cf_form()
        args = {'form': form}
        return render(request, 'reporter/Cf_form.html', args)