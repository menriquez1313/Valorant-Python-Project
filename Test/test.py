"""
Created October 10, 2022

This is a test using the Valorant API

"""

import requests

response = requests.get("") #ACCOUNT-V1 
val_status = requests.get("") #VAL-STATUS-v1

data = response.json()
data_val_status = val_status.json()

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

    print(f"User's Valorant Tag: {valorantTag}")
    print(f"Location: {location_info}")

#Checks for status in specified region (NA)
def valorant_status():
    val_status.raise_for_status()
    2
    maintenances = data_val_status["maintenances"]
    incidents = data_val_status["incidents"][0]["updates"][0]["translations"][0]["content"]
    
    print(f"Maintenances: {maintenances}")
    print(f"Updates: {incidents}")

on = True
while on == True:
    print("/////////Welcome to VALORANT info///////")
    print("1: User and locale")
    print("2: Update/Status on Valorant")
    print("0: Exit")
    choose = int(input("What info would you like to know?: "))
    
    
    if choose == 1:
        user_info_status()
        print("\n")
    elif choose == 2:
        valorant_status()
        print("\n")
    elif choose == 0:
        print("GLHF on your Games!")
        on = False
        print("\n")
    else:
        print("Please enter a number showed on the list.")

