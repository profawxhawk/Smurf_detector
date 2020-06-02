from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from sklearn.decomposition import PCA
from django.urls import reverse
from .models import R6Final,Cffinal
import pandas as pd
from .scrap import extract_data,get_all_data
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from django.http import JsonResponse
from .forms import predictform
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import plot
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.naive_bayes import GaussianNB
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

def logit(val):
    return val
    print(val)
    
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
    # if len(user)==1:
    #     return (user.count_smurf*100/(user.count_no_smurf+user.count_smurf))
    
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

    temp1=[1,"Rgr3"]
    temp1.extend(temp)
    temp1.append(2)
    temp1.append(0)
    temp1.append(1)
    data.loc[data.size]=temp1
    

    data[columns]=data[columns].astype('float')
    data['smurf']=data['smurf'].astype('int')

    # i1=0
    # i2=0
    # while(i1<len(y_train)):
    #     temp1[i1].append(y_train[i1])
    #     i1+=1
    # while(i2<len(y_test)):
    #     temp1[i1].append(y_train[i2])
    #     i1+=1
    #     i2+=1
    # temp1[i1]=1
    columns.append('smurf')
    pca = PCA(n_components=2).fit(data[columns])
    pca_2d = pca.transform(data[columns])

    
    logisticRegr = LogisticRegression()
    x_train=x_train.astype('float')
    x_test=x_test.astype('float')
    y_train=y_train.astype('int')
    y_test=y_test.astype('int')
    logisticRegr.fit(x_train, y_train)
    score = logisticRegr.score(x_test, y_test)
    temp=np.asarray(temp).reshape(1, 33)
    predict=logisticRegr.predict_proba(temp)

    return (score,predict[0][1],pca_2d,data['smurf'])
    
    
def r6_result(request):
    return render(request, 'predictor/prediction.html',{'name':'BUST1N.','score':95.5,'prediction':86.9})

def column(matrix, i):
    return [row[i] for row in matrix]

def get_plot(x,y,z,fg=1):
    smurf=[]
    non_smurf=[]
    cur_user=[]
    for i,j,k in zip(x,y,z):
        if k==1.0:
            smurf.append([i,j])
        elif k==0.0:
            non_smurf.append([i,j])
        else:
            cur_user.append([i,j])
    
    name1="Smurf"
    name2="Non-Smurf"
    if fg==0:
        cur_user.append([x[x.size-1],y[y.size-1]])
        name2="Smurf"
        name1="Non-Smurf"
    
    trace1 = go.Scatter(
        x = column(smurf,0),
        y = column(smurf,1),
        mode = 'markers',
        marker=dict(size=15, color='rgb(255,0,0)'),
        name=name1
    )
    trace2 = go.Scatter(
        x = column(non_smurf,0),
        y = column(non_smurf,1),
        mode = 'markers',
        marker=dict(size=15, color='rgb(0,255,0)'),
        name=name2
    )
    trace3 = go.Scatter(
        x = column(cur_user,0),
        y = column(cur_user,1),
        mode = 'markers',
        marker=dict(size=15, color='rgb(0, 0, 0)'),
        name="Current User"
    )

    data = plot([trace1, trace2,trace3],output_type='div')
    return data

def cfmodel(df,pred):
    x=df
    del x['field1']
    del x['city']
    del x['firstname']
    del x['lastname']
    del x['handle']
    del x['maxrank']
    del x['count_smurf']
    del x['count_no_smurf']
    del x['smurf']
    del x['bitmasks']
    pred.pop(6)
    # idk what the name of aaron's function is and the df part
    # everything below this works
    x.loc[x.size]=pred
    
    # for i in range(len(x['bitmasks'])):
    #     x['bitmasks'].iloc[i]=int.from_bytes(x['bitmasks'].iloc[i], "big")

    kmeans = KMeans(n_clusters=2, random_state=0,max_iter=200).fit(x)
    arr=kmeans.labels_

    pca = PCA(n_components=2).fit(x)
    pca_2d = pca.transform(x)



    
    clf = GaussianNB()
    clf.fit(x, arr)
    # replace x.loc[:0] with the output of the function
    temp=np.asarray(pred).reshape(1,12)
    predict=clf.predict_proba(temp)

    if arr[len(arr)-1]==0:
        return ("Smurf",pca_2d,arr)
    else:
        return ("Non-Smurf",pca_2d,arr)

    

def cfpredictor(username):
    user=Cffinal.objects.filter(handle=username)
    data=Cffinal.objects.all()
    data=pd.DataFrame([vars(s) for s in data])
    data.drop('_state', axis=1, inplace=True)
    data.fillna(data.mean(),inplace=True)
    
    temp=get_all_data(username)
    if temp==0:
        return -1
        
    score=cfmodel(data,temp[4:])
    pca_2d=score[1]
    plot=get_plot(pca_2d[:,0],pca_2d[:,1],score[2],0)
    return (score[0],plot)
    



    
    


@csrf_exempt
def selector(request):
    if request.method=='POST':
        form = predictform(data=request.POST)
        if form.is_valid():
            
            website=form.cleaned_data['website']
            username=form.cleaned_data['username']
            
            form = predictform()
            if website!='R6' and website!='Cf':
                return render(request, 'predictor/Homepage.html',{'Message':3,'form': form})

            if website=='R6':
                res=r6predictor(username)
                if res==-1:
                    return render(request, 'predictor/Homepage.html',{'Message':1,'form': form})
                else:
                    plot=get_plot(res[2][:,0],res[2][:,1],res[3])
                    return render(request, 'predictor/prediction.html',{'website':'Rainbow6 Siege Smurfinator','name':username,'score':str(res[0]*100)[:5]+'%','prediction':str(res[1]*100)[:5]+'%','plot':plot})
            if website=='Cf':
                res=cfpredictor(username)
                if res==-1:
                    return render(request, 'predictor/Homepage.html',{'Message':1,'form': form})
                print(res[0])
                return render(request, 'predictor/prediction.html',{'website':'Codeforces Smurfinator','name':username,'group':res[0],'plot':res[1]})
                # return render(request, 'predictor/prediction.html',{'website':'Codeforces Smurfinator','name':username,'score':'88.53%','prediction':'56.5%'})
    elif request.method=='GET':
        form = predictform()
        args = {'form': form}
        return render(request, 'predictor/Homepage.html', args)

