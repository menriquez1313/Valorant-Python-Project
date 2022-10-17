"""
Created October 10, 2022

This is a test using the Valorant API

"""

import requests

response = requests.get("") #ACCOUNT-V1 
val_status = requests.get("") #VAL-STATUS-v1
val_content = requests.get("") #VAL-CONENT-V1
val_ranked = requests.get("") #VAL-RANKED-V1

data = response.json()
data_val_status = val_status.json()
data_val_content = val_content.json()
data_val_ranked = val_ranked.json()

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
    
on = True
while on == True:
    print("/////////Welcome to VALORANT info///////")
    print("1: User and locale")
    print("2: Update/Status on Valorant")
    print("3: Current Act Info")
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
    elif choose == 0:
        print("//////////////////////////////")
        print("///////GLHF on your Games!/////")
        on = False
        print("//////////////////////////////")
    else:
        print("Please enter a number showed on the list.")