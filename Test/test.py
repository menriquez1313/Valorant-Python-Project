"""
Created October 10, 2022

This is a test using the Valorant API

"""

import requests
import valorant


response = requests.get("API")
val_status = requests.get("API")

def user_info_status():
    response.raise_for_status()
    val_status.raise_for_status()

    data = response.json()
    data_val_status = val_status.json()

    id = data["gameName"]
    tag = data["tagLine"]
    
    location = data_val_status["name"]
    locales = data_val_status["locales"][2]
    valorantTag = (id, tag)
    location_info = (location, locales)

    print(f"User's Valorant Tag: {valorantTag}")
    print(f"Location: {location_info}")
    

on = TRUE
while on == TRUE:
    print("/////////Welcome to VALORANT info///////")
    print("1: User and locale")
    print("0: Exit")
    choose = input("What info would you like to know?: ")
    if choose == 1:
        user_info_status()
        print("\n")
    elif choose == 0:
        print("GLHF on your Games!")
        on == FALSE
    else:
        print("Please enter a number showed on the list.")
        




