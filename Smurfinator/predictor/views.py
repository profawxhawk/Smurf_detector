from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from sklearn.decomposition import PCA
from django.urls import reverse
from .models import R6Final
import pandas as pd
from .scrap import extract_data
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from django.http import JsonResponse
import numpy as np
# data.fillna(data.mean(),inplace=True)
# columns=['Level','Best MMR Rating','Rank','Avg Seasonal MMR' ,'Wins','Win_p','Kills' ,'KD','Deaths','Headshots','Losses','Time Played','Matches Played','Melee Kills','Blind Kills','Time Played_casual','Losses_casual','Matches_casual','Deaths_casual','Kills_casual','Win_p_casual','KD_casual','Kills/min_casual','Time Played_ranked','Wins_ranked','Losses_ranked','Matches_ranked','Deaths_ranked','Kills_ranked','Win_p_ranked','KD_ranked','Kills/match_ranked','Kills/min_ranked','Smurf']
# pca = PCA(n_components=2).fit(data[columns])
# pca_2d = pca.transform(data[columns])

# Create your views here.
minMaxVal = {"Level":[18,564], "Best MMR Rating":[0,9007], "Rank":[0,22], "Avg Seasonal MMR":[1966,9007],
"Wins":[19,12438], "Win %":[32.3,100], "Kills":[0.11,53.25], "KD":[0.11,53.25], "Deaths":[48,70247], 
"Headshots":[34,45749], "Losses":[0,7813], "Time Played":[0,5731], "Matches Played":[32,19214],
"Melee Kills":[0,13203], "Blind Kills":[0,170], "Time Played_casual":[0,1974], "Losses_casual":[0,3008],
"Matches_casual":[0,8073], "Deaths_casual":[1,30435], "Kills_casual":[0,34521], "Win%_casual":[0,100], "KD_casual":[0,37],
"Kills/match_casual":[0,3.77], "Time Played_ranked":[0,5169], "Wins_ranked":[0, 8962], "Losses_ranked":[0,7601],
"Matches_ranked":[0,15724], "Deaths_ranked":[0,68454], "Kills_ranked":[13,77020], "Win%_ranked":[0,100],
"KD_ranked": [0.07,124], "Kills/match_ranked":[0.24,21], "Kills/min_ranked":[0.02, 4.67], "Smurf": [0,1] }
def home(request):
    return render(request, 'predictor/Homepage.html')


def logit(val):
    return val
def convert_type(arr):
    Rank_list={'NO_RANK':0,'COPPERIV':1,'COPERIV':2,'COPPERIII':3,'COPPERII':4,'COPPERI':5,'BRONZEIV':6,
    'BRONZEIII':7,'BRONZEII':8,'BRONZEI':9,'SILVERV':10,'SILVERIV':11,'SILVERIII':12,'SILVERII':13,'SILVERI':14,
    'GOLDIV':15,'GOLDIII':16,'GOLDII':17,'GOLDI':18,'PLATINUMIII':19,'PLATINUMII':20,'PLATINUMII':21,'DIMOND':22,'CHAMPION':23}
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
    temp=[]
    for i,j in zip(data[1:34],minMaxVal.keys()):
        j=minMaxVal[j]
        if i < j[0]:
            j[0]=i
        if i>j[1]:
            j[1]=i
        i=(i-j[0])/(j[1])
        temp.append(i)
    return temp

def r6predictor(username):
    user=R6Final.objects.filter(username=username)
    if len(user)==1:
        return (user.count_smurf*100/(user.count_no_smurf+user.count_smurf))
    
    data=extract_data(username)

    if data==0:
        return -1

    data=convert_type(data)
    temp=norm(data)

    columns=['level', 'best_mmr_rating', 'ranking',
    'avg_seasonal_mmr', 'wins', 'win_p', 'kills', 'kd', 'deaths',
    'headshots', 'losses', 'time_played', 'matches_played', 'melee_kills',
    'blind_kills', 'time_played_casual', 'losses_casual', 'matches_casual',
    'deaths_casual', 'kills_casual', 'win_p_casual', 'kd_casual',
    'killsmin_casual', 'time_played_rankinged', 'wins_rankinged',
    'losses_rankinged', 'matches_rankinged', 'deaths_rankinged',
    'kills_rankinged', 'win_p_rankinged', 'kd_rankinged',
    'killsmatch_rankinged', 'killsmin_rankinged']
    
    data=R6Final.objects.all()
    data=pd.DataFrame([vars(s) for s in data])
    data.drop('_state', axis=1, inplace=True)
    data.fillna(data.mean(),inplace=True)
    for i in range(len(data['smurf'])):
        data['smurf'].iloc[i]=int.from_bytes(data['smurf'].iloc[i], "big")
    
    
    x_train, x_test, y_train, y_test = train_test_split(data[columns], data['smurf'], test_size=0.40, random_state=0)
    x_train=x_train.astype('float')
    x_test=x_test.astype('float')
    y_train=y_train.astype('int')
    y_test=y_test.astype('int')
    logisticRegr = LogisticRegression()
    x_train=x_train.astype('float')
    x_test=x_test.astype('float')
    y_train=y_train.astype('int')
    y_test=y_test.astype('int')
    logisticRegr.fit(x_train, y_train)
    score = logisticRegr.score(x_test, y_test)
    temp=np.asarray(temp).reshape(1, 33)
    predict=logisticRegr.predict_proba(temp)
    return (score,predict[0][1])
    
    
def r6_result(request):
    return render(request, 'predictor/prediction.html',{'name':'efe','score':95.5,'prediction':86.9})

@csrf_exempt
def selector(request):
    if request.method=='POST':
        username=request.POST['username']
        website=request.POST['website']

        if website!='Rainbow6 Siege' and website!='Codeforces':
            return render(request, 'predictor/Homepage.html',{'Message':3})

        if website=='Rainbow6 Siege':
            res=r6predictor(username)
            if res==-1:
                return render(request, 'predictor/Homepage.html',{'Message':2})
            else:
                return JsonResponse({'name':username,'score':str(res[0])+'%','prediction':str(res[1])+'%'},safe=False)

    else:
        return redirect(reverse('home'))

