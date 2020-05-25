from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import csv
import time
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

def extract_data(username):
    driver = webdriver.Firefox(executable_path=r'/mnt/c/Users/Bharath/Desktop/semester 6/psosm/Project/Report_smurf/Resources/geckodrive/geckodriver.exe')
    name=[username]
    for j,i in enumerate(name):
        r6_row=[]
        driver.get('https://r6.tracker.network/profile/pc/'+i)
        try:
            # level = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]/div/div[2]').text
            # Best_MMR_Rating = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div/div[2]').text
            # Rank= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[1]/div[2]/div[3]/div[2]').text
            level= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]/div/div[2]').text
            Best_MMR_Rating = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div/div[2]').text
            Ranking= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[1]/div[2]/div[3]/div[2]').text
            Avg_Seasonal_MMR= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[1]/div[2]/div[4]/div[2]').text
            Wins= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[1]/div[3]/div/div[1]/div[2]').text
            Win_p= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[1]/div[3]/div/div[2]/div[2]').text
            Kills= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[1]/div[3]/div/div[3]/div[2]').text
            KD= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[1]/div[3]/div/div[4]/div[2]').text
            Deaths= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[3]/div[2]').text
            Headshots= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[2]').text
            Losses= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[6]/div[2]').text
            Time_Played= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[8]/div[2]').text
            Matches_Played= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[9]/div[2]').text
            Melee_Kills= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[11]/div[2]').text
            Blind_Kills= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[12]/div[2]').text
            Time_Played_casual= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[2]').text
            Losses_casual= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[3]/div[2]').text
            Matches_casual= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[4]/div[2]').text
            Deaths_casual= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[5]/div[2]').text
            Kills_casual= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[6]/div[2]').text
            Win_p_casual= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[7]/div[2]').text
            KD_casual= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[8]/div[2]').text
            Kills_min_casual= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[10]/div[2]').text
            Time_Played_ranked= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[1]/div[2]').text
            Wins_ranked= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[2]/div[2]').text
            Losses_ranked= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[3]/div[2]').text
            Matches_ranked= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[4]/div[2]').text
            Deaths_ranked= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[5]/div[2]').text
            Kills_ranked= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[6]/div[2]').text
            Win_p_ranked= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[7]/div[2]').text
            KD_ranked= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[8]/div[2]').text
            Kills_match_ranked= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[9]/div[2]').text
            Kills_min_ranked= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[10]/div[2]').text

                
                # Avg_Seasonal_MMR= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[1]/div[2]/div[4]/div[2]').text
                # Wins= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[1]/div[3]/div/div[1]/div[2]').text
                # Win_p= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[1]/div[3]/div/div[2]/div[2]').text
                # Kills= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[1]/div[3]/div/div[3]/div[2]').text
                # KD= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[1]/div[3]/div/div[4]/div[2]').text
                # Deaths= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[3]/div[2]').text
                # Headshots= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[2]').text
                # Losses= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[6]/div[2]').text
                # Time_Played= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[8]/div[2]').text
                # Matches_Played= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[9]/div[2]').text
                # Melee_Kills= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[11]/div[2]').text
                # Blind_Kills= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[12]/div[2]').text
                # Time_Played_casual= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[2]').text
                # Losses_casual= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[3]/div[2]').text
                # Matches_casual= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[4]/div[2]').text
                # Deaths_casual= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[5]/div[2]').text
                # Kills_casual= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[6]/div[2]').text
                # Win_p_casual= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[7]/div[2]').text
                # KD_casual= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[8]/div[2]').text
                # Kills_min_casual= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[10]/div[2]').text
                # Time_Played_ranked= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[1]/div[2]').text
                # Wins_ranked= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[2]/div[2]').text
                # Losses_ranked= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[3]/div[2]').text
                # Matches_ranked= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[4]/div[2]').text
                # Deaths_ranked= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[5]/div[2]').text
                # Kills_ranked= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[6]/div[2]').text
                # Win_p_ranked= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[7]/div[2]').text
                # KD_ranked= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[8]/div[2]').text
                # Kills_match_ranked= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[9]/div[2]').text
                # Kills_min_ranked= driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[10]/div[2]').text
                
            r6_row=[name[j],level,Best_MMR_Rating,Ranking,Avg_Seasonal_MMR,Wins,Win_p,Kills,KD,Deaths,Headshots,Losses,Time_Played,Matches_Played,Melee_Kills,Blind_Kills,Time_Played_casual,
            Losses_casual,
            Matches_casual,
            Deaths_casual,
            Kills_casual,
            Win_p_casual,
            KD_casual,
            Kills_min_casual,
            Time_Played_ranked,
            Wins_ranked,
            Losses_ranked,
            Matches_ranked,
            Deaths_ranked,
            Kills_ranked,
            Win_p_ranked,
            KD_ranked,
            Kills_match_ranked,
            Kills_min_ranked]
            # r6_row=[name[j],level,Best_MMR_Rating,Rank]
            driver.close()
            return r6_row
        except:
            driver.close()
            return 0

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
            row.append(avg_upvote)
        else:
            res = data['result']
            if len(res)==0:
                row.append(avg_upvote)	
            else:  
                for y in res:
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

        
    