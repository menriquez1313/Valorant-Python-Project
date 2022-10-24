"""
Created October 10, 2022

This is a test using the Valorant API


https://numpy.org/doc/ 
"""


KEY = ""

import requests
import pandas
import numpy as np

response = requests.get(f"key={KEY}") #ACCOUNT-V1 
val_status = requests.get(f"key={KEY}") #VAL-STATUS-v1
val_content = requests.get(f"key={KEY}") #VAL-CONTENT-V1
val_ranked = requests.get(f"key={KEY}") #VAL-RANKED-V1


data = response.json()
data_val_status = val_status.json()
data_val_content = val_content.json()
data_val_ranked = val_ranked.json()

##### Calculations #######
#finding average
def average(num1, num2):
    avg = round((((abs(num1 - num2)) / ((num1 + num2) / 2)) * 100), 2)
    return avg

##########################

#Gives out basic info of User
def user_info_status():
    response.raise_for_status()
    val_status.raise_for_status()

    id = data["gameName"]
    tag = data["tagLine"]
    #puuid = data["puuid"]
    
    location = data_val_status["name"]
    locales = data_val_status["locales"][2]
    valorantTag = (id, tag) #puuid)
    location_info = (location, locales)

    print("//////////////////////////////")
    print(f"User's Valorant Tag: {valorantTag}")
    print(f"Location: {location_info}")
    print("//////////////////////////////")
    
#Checks for status in specified region (NA)
def valorant_status():
    val_status.raise_for_status()
    maintenances = data_val_status["maintenances"]
    
    if len(data_val_status["incidents"]) == 0: #checks if there is any incidents in the dictionary by counting content in the dictionary
        print("//////////////////////////////")
        print("Currently no information for incidents")
        print("//////////////////////////////")
    
    else:
           
        content = data_val_status["incidents"][0]["updates"][0]["translations"][0]["content"]
        incident_severity = data_val_status["incidents"][0]["incident_severity"]
    
        print("//////////////////////////////")
        print(f"Maintenances: {maintenances}")
        print(f"Updates: {content}")
        print(f"Incident: {incident_severity}")
        print("//////////////////////////////")
    
#fix this to automatically update the Epiode/ACT
def current_act_info():
    val_content.raise_for_status()
    episode = data_val_content["acts"][16]["name"]
    act = data_val_content["acts"][19]["name"]
    print("//////////////////////////////")
    print(f"Episode: {episode}")
    print(f"Act: {act}")
    print(f"Top 5 players for {episode}:{act} \n")
    
    for i in range(5):
        player = data_val_ranked["players"][i]["gameName"]
        leaderboardRank = data_val_ranked["players"][i]["leaderboardRank"]
        wins = data_val_ranked["players"][i]["numberOfWins"]
        
        print("------------------------------------")
        print(f"Player: {player}")
        print(f"Leaderboard Rank: {leaderboardRank}")
        print(f"Wins: {wins}")
    print("------------------------------------")

#All Agents   
def current_agents():
    val_content.raise_for_status()
    
    print("------------------------------------")
    n=0 #counter
    for i in range(len(data_val_content["characters"])):
        
        agents = data_val_content["characters"][i]["name"]
        if agents == "Null UI Data!":
            pass
        else:
            n+=1
            print(f"{n}.{agents}")
    print("------------------------------------")

def current_maps():
    val_content.raise_for_status()
    
    print("------------------------------------")
    n=0 # counter 
    for i in range(len(data_val_content["maps"])):
            
        maps = data_val_content["maps"][i]["name"]
        if maps == "Null UI Data!":
            pass
        else:
            n+=1
            print(f"{n}.{maps}")
    print("------------------------------------")
    

#Using a test sample file "data.csv" to output information from ranked games
def rank_games():
    rank_info = pandas.read_csv("valorant_data_sample.csv")
    print(rank_info)
    
    #calculate average of kills, deaths, and assists
    kill_count = rank_info["Kills"].tolist()
    death_count = rank_info["Deaths"].tolist()
    assist_count = rank_info["Assists"].tolist()
    
    kill_average = np.average(kill_count)
    death_average = np.average(death_count)
    assist_average = np.average(assist_count)
    
    #percentage difference of the last and second to last game
    # kill_perc = ((abs(kill_count[0] - kill_count[1])) / ((kill_count[0] + kill_count[1]) / 2)) * 100
    # death_perc = ((abs(death_count[0] - death_count[1])) / ((death_count[0] + death_count[1]) / 2)) * 100
    # assist_perc = ((abs(assist_count[0] - assist_count[1])) / ((assist_count[0] + assist_count[1]) / 2)) * 100
    
    kill_perc = average(kill_count[0], kill_count[1])
    death_perc = average(death_count[0], death_count[1])
    assist_perc = average(assist_count[0], assist_count[1])
    
    #print info
    print("--------------------------------------------------------")
    print(f"Average Kill: {kill_average}")
    print(f"Average Death: {death_average}")
    print(f"Average Assist: {assist_average}")
    print("--------------------------------------------------------")
    print("Percentage Differance of your last two games:")
    print(f"K: {kill_perc}%\nD: {death_perc}%\nA: {assist_perc}%")
    
#body
on = True
while on == True:
    print("/////////Welcome to VALORANT info///////")
    print("1: User and locale")
    print("2: Update/Status on Valorant")
    print("3: Current Act Info")
    print("4: Current Agents")
    print("5: Current Maps")
    print("6: Ranked Games")
    print("0: Exit")
    choose = int(input("What info would you like to know?: "))
    
    if choose == 1:
        user_info_status()
        print("\n")
    elif choose == 2:
        valorant_status()
        print("\n")
    elif choose == 3:
        current_act_info()
        print("\n")
    elif choose == 4:
        current_agents()
        print("\n")
    elif choose == 5:
        current_maps()
        print("\n")
    elif choose == 6:
        rank_games()
        print("\n")   
    elif choose == 0:
        print("//////////////////////////////")
        print("///////GLHF on your Games!/////")
        print("//////////////////////////////")
        on = False
    else:
        print("Please enter a number showed on the list.")