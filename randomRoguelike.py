import random
import time


player_name = ""
player_status = { 

    "HP" : 89,

}

player_class = {}
player_inventory = { 
    "Throwing Knife" : 2, 
    "Health Potion" : 1,
    }



Classes = ["Archer", "Barbarian", "Mage"]
Class_Weapons = {   
    "archer" : "Bow",
    "barbarian" : "Axe",
    "mage" : "Wand"
}

def exitabs(prompt):
        prompt
        print("From within your wise countenance, a god whispers. 'Perish'.")
        exit()

def gameover(GO):
    GO
    print("You hear a faint voice of plea as you lie down. Incapable, cold, and dead.")
    exit()



def dice_roll(dice):
    if dice == 1:
        return 1
    elif dice == 2:
        return 2
    elif dice == 3:
        return 3
    elif dice == 4:
        return 4
    elif dice == 5:
        return 5
    elif dice == 6:
        return 6
    elif dice == 7:
        return 7
    elif dice == 8:
        return 8
    elif dice == 9:
        return 9
    elif dice == 10:
        return 10
    elif dice == 11:
        return 11
    elif dice == 12:
        return 12

def roll_the_dice(diceroll):
    while True:
        diceroll = random.randint(0, 11)
        dice_result = dice_roll(diceroll)
        dice_result += 1
        for seconds in range(3,0,-1):
            print(seconds)
            time.sleep(1)
        return dice_result

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

def checkstatus(statck):
    check = valid_input(statck)
    if check:
        print(player_status)
    else:
        pass

def displayInventory(dispinvent):
    check = valid_input(dispinvent)
    if check == True:
        print("Inventory: ")
        for k, v in player_inventory.items():
            print(str(v) + ' ' + str(k))
    else:
        pass
def use_hppotion(potion):
    potion = input("Type the hp potion you wish to use: ")
    if potion.lower() == "health potion":
        if player_status["HP"] == 100:
            print("HP Full. cannot use potion.")
        elif player_status["HP"] <= 99:
            player_status["HP"] = int(player_status.get("HP")) + 20
            if player_status["HP"] > 100:
                player_status["HP"] = 100
            print(f"Successfully healed. {player_status}")
            if player_inventory["Health Potion"] == 1:
                del player_inventory["Health Potion"]
            else:
                player_inventory["Health Potion"] = int(player_inventory.get("Health Potion")) - 1
    else:
        print("No such potion")


#def player_combat(playerturn, opponentturn):



player_name = input("What's your name?: ")
print(f"Good day to you adventurer. So your name is.. {player_name}")
playerdec1 = valid_input("Do you wish to play? (input Yes or No): ")
if playerdec1 == True:
    player_classchoice = valid_class("What class will you be in? (Mage, Archer or Barbarian): ")
    player_class[player_classchoice] = Class_Weapons.get(str(player_classchoice.lower()))
    player_inventory[Class_Weapons.get(str(player_classchoice))] = 100 
    print(f"Your weapon is {Class_Weapons.get(str(player_classchoice.lower()))}")
    

elif playerdec1 == False:
    print("Alright. Then another shall take your place.")
    exitabs(prompt=0)
else:
    exitabs()

print(player_class)
checkstatus("Check status? (Yes or No): ")
displayInventory("Check inventory? (Yes or No): ")
print("Note: Player weapon shows durability, not amount.")

diceroll1 = roll_the_dice("")
print(f"The die speaks: {diceroll1}.")

for i in range(3,0,-1):
    time.sleep(1)

print("You walk deep into the woods with only the light of the moon, filtered by the leaves, guiding your path.")
print("From a distance, you notice an Orc clad in chainmail armor, guarding what seems to be a chest of treasure.")

potopp = valid_input("Do you wish to use your potion?: ")
if potopp == True:
    use_hppotion("Type the name of the potion that you want to use.: ")
    
else:
    pass

Orc1 = {"HP" : 50} #First enemy encounter status

combat1 = valid_input("Do you wish to engage in combat?: ")
if combat1 == True:
    checkstatus("Check your status before combat?: ")
    
elif combat1 == False:
    leave1 = valid_input("Do you wish to take a different path? (get away from the encounter?): ")
    if leave1 == True:
        print("You attempt to leave without alerting the Orc. (mandatory dice roll)")
        droll1 = roll_the_dice("")
        print(droll1)
        if droll1 >= 5:
            print("You successfully leave the ")
    

