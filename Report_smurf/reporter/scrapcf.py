import requests
import pandas

url = "https://codeforces.com/api/user.info"
url2="https://codeforces.com/api/user.ratedList"
url3="https://codeforces.com/api/contest.standings"
url4 = "https://codeforces.com/api/user.blogEntries"
url5 = "https://codeforces.com/api/user.status"

PARAMS = {'lang':'en','handles':'SARS-CoV-2;COVID-19;KwanghyunOn;fatwizard2020;fan_of_lxy;deeepeshthakur;usaxena95'}
PARAMS2 = {'lang':'en','activeOnly':'true'}
PARAMS3 = {'contestId':629,'from' : 1,'count':110,'showUnofficial':False}


def get_all_data(handle):
    try:
        row = []
        PARAMS4 = {'lang':'en','handles':handle}
        r1 = requests.get(url,params=PARAMS4)
        data = r1.json()
        res = data['result']
        obj = res[0]
        if 'firstName' in obj.keys():
            row.append(obj['firstName'])
        else:
            row.append('NULL')
        if 'lastName' in obj.keys():
            row.append(obj['lastName'])
        else:
            row.append('NULL')
        if 'city' in obj.keys():
            row.append(obj['city'])
        else:
            row.append('NULL')
        if 'maxRank' in obj.keys():
            row.append(obj['maxRank'])
        else:
            row.append('NULL')
        if 'maxRating' in obj.keys():
            row.append(obj['maxRating'])
        else:
            row.append('NULL')
        row.append(obj['contribution'])
        row.append(obj['friendOfCount'])
        #fn,ln,city,max_rank,max_rating,contib,friend
        PARAMS5 = {'lang':'en','handle':handle}
        r = requests.get(url4,params=PARAMS5)
        data = r.json()
        avg_upvote=0.0
        if 'result' not in data.keys():
            #print(1)
            row.append(avg_upvote)
        else:
            res = data['result']
            if len(res)==0:
                row.append(avg_upvote)	
            else:  
                for y in res:
                    #print(y['rating'])
                    avg_upvote+=y['rating']
                avg_upvote/=len(res)
                row.append(avg_upvote)
        #avg_upvote_received appended
        tags = ['hashing','bitmask','ternary search','flows','string suffix structures','fft','meet-in-the-middle']
        tags2 = ['dp','geometry','probabilities']
        lis_of_lis = [[],[],[],[],[],[],[]]
        PARAMS6 = {'lang':'en','handle':handle,'from':1,'count':500}
        r = requests.get(url5,params=PARAMS6)
        data = r.json()
        res = data['result']
        temp_lis=[]
        temp = {}
        for k in tags:
            temp[k]=0	
        ac = 0
        for obj in res:
            for k in tags:
                if k in obj['problem']['tags']:
                    temp[k]+=1
            if ('verdict' in obj.keys()) and (obj['verdict'] == 'OK'):
                ac+=1
            val=1
            rating = 1800
            if 'rating' in obj['problem'].keys():
                rating = obj['problem']['rating']
            for x in obj['problem']['tags']:
                if x in tags:
                    val = max(val,3)
                elif x in tags2:
                    val = max(val,2)
            temp_lis.append(val*(rating/1))
        temp_lis.sort(reverse=True)
        cur_intel=0
        div=0
        for q in range(0,min(len(temp_lis),25)):
            div+=1
            cur_intel+=temp_lis[q]
        cur_intel/=div
        final_intel = cur_intel/row[4]
            #lis_of_intel.append(cur_intel/rating_list[iter_var])
        #iter_var+=1
        ac/=max(len(res),1)
        ac*=100
        it=0
        for tag in tags:
            lis_of_lis[it].append(temp[tag])
            it+=1
        row.append(ac)
        #ac done
        for w in range(7):
            row.append(lis_of_lis[w][0])
        #tags done
        row.append(final_intel)
        return row
    except:
        return 0
print(get_all_data('fatwizard2020'))
        