player = 


Classes = ["Archer", "Barbarian", "Mage"]
Class_Weapons = {
    
    "Archer" : "Bow",
    "Barbarian" : "Axe",
    "Mage" : "Wand"


}
    

def valid_input(TorF):
    while True:
        try:
            value = input(TorF)
            if value.lower() == "yes":
                return True
            elif value.lower() == "no":
                return False
            else:
                raise ValueError("Invalid input, please type only 'Yes' or 'No'")
        except ValueError as ve:
            print(ve)
def valid_class(cls):
    while True:
        try:
            value = input(cls)
            if value.lower() == "archer":
                return value
            elif value.lower() == "barbarian":
                return value
            elif value.lower() == "mage":
                return value
            else:
                raise ValueError("Invalid input, please type only choose amongst the listed classes (Mage, Archer, Barbarian).")
        except ValueError as ve:
            print(ve)

player_name = input("What's your name?: ")
pl
print(f"Good day to you {player_name}")
playerdec1 = valid_input("Are you down to fight for good? (input Yes or No): ")
if playerdec1 == True:
    player_class = valid_class("What class will you be in? (Mage, Archer or Barbarian): ")
elif playerdec1 == False:
    print("Alright. Then another shall take your place.")
    exit
    

