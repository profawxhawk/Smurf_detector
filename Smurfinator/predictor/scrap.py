from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import csv
import time

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



        
    