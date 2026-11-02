##############################
# Course: COMP 1113 FA01, 2025
# Assignment #11
# Author: Alec Pringle
# Student ID: 0313459
# email address: 0313459p@acadiau.ca
# Date: 2025-11-24
# I certify that this code is my own.  I have not broken any rules concerning Academic Dishonesty.
##############################


with open("soccer-m.txt", "r") as lines:
    soccer_mList = [line.strip() for line in lines]

with open("soccer-w.txt", "r") as lines:
    soccer_wList = [line.strip() for line in lines]
    
with open("hockey-m.txt", "r") as lines:
    hockey_mList = [line.strip() for line in lines]


soccerM_Players = []
soccerM_Positions = []

soccerW_Players = []
soccerW_Positions = []

hockeyM_Players = []
hockeyM_Positions = []

Defence = []
Midfield = []
Wingers = []
Forwards = []
Goalkeepers = []
Goalies = []


for element in soccer_mList:
    preComma, postComma = element.split(",")

    soccerM_Players.append(preComma)
    soccerM_Positions.append(postComma)

for element in soccer_wList:
    preComma, postComma = element.split(",")

    soccerW_Players.append(preComma)
    soccerW_Positions.append(postComma)
    
for element in hockey_mList:
    preComma, postComma = element.split(",")

    hockeyM_Players.append(preComma)
    hockeyM_Positions.append(postComma)
    

userInput = str(input("\nWhich roster would you like printed?\n\n1) Men's Soccer\n2) Women's Soccer\n3) Men's Hockey\n4) Quit\n\nEnter here (1-4): "))
while (True): #loops until break
    try:
        userChoice = int(userInput)
        if ((userChoice == 1) or (userChoice == 2) or (userChoice == 3) or (userChoice == 4)):
            break
        else:
            userInput = input("\nInput must be (1-4): ")
    except:
        userInput = input("\nInput must be an integer (1-4): ")

if (userChoice == 1):
    
    for index, item in enumerate(soccerM_Players):
        if (soccerM_Positions[index] == "D"):
            Defence.append(item)
        elif (soccerM_Positions[index] == "MF"):
            Midfield.append(item)
        elif (soccerM_Positions[index] == "W"):
            Wingers.append(item)
        elif (soccerM_Positions[index] == "F"):
            Forwards.append(item)
        else:
            Goalkeepers.append(item)
            
elif (userChoice == 2):
    
    for index, item in enumerate(soccerW_Players):
        if (soccerW_Positions[index] == "D"):
            Defence.append(item)
        elif (soccerW_Positions[index] == "MF"):
            Midfield.append(item)
        elif (soccerW_Positions[index] == "W"):
            Wingers.append(item)
        elif (soccerW_Positions[index] == "F"):
            Forwards.append(item)
        else:
            Goalkeepers.append(item)
            
elif (userChoice == 3):
    
    for index, item in enumerate(hockeyM_Players):
        if (hockeyM_Positions[index] == "D"):
            Defence.append(item)
        elif (hockeyM_Positions[index] == "F"):
            Forwards.append(item)
        else:
            Goalies.append(item)
            
print("\n\n")

if (Defence != []):
    print ("\nYour defence:\n")
    for x in Defence:
        print (x)
if (Midfield != []):
    print ("\nYour midfielders:\n")
    for x in Midfield:
        print (x)
if (Wingers != []):
    print ("\nYour wingers:\n")
    for x in Wingers:
        print (x)
if (Forwards != []):
    print ("\nYour forwards:\n")
    for x in Forwards:
        print (x)
if (Goalkeepers != []):
    print ("\nYour goalkeepers:\n")
    for x in Goalkeepers:
        print (x)
if (Goalies != []):
    print ("\nYour goalies:\n")
    for x in Goalies:
        print (x)