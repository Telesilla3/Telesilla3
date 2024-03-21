import random
import time


player_name = ""
player_status = { 

    "HP" : 89,
    "Mana" : 100,
    "Stamina" : 81,

}

player_class = {}
player_inventory = { 
    "throwing knife" : 2, 
    "health potion" : 1,
    "stamina potion" : 1,
    "mana potion" : 1
    }



Classes = ["Archer", "Barbarian", "Mage"]
Class_Weapons = {   
    "archer" : "Bow",
    "barbarian" : "Axe",
    "mage" : "Wand"
}
player_weapon = []



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
        diceroll = random.randint(1, 12)
        dice_result = int(dice_roll(diceroll))
        for seconds in range(3,0,-1):
            print(seconds)
            time.sleep(1)
        print(f"The die speaks. {dice_result}")
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

def valid_weap(weap):
    while True:
        try:
            weap = input("")
            if weap.lower in player_weapon:
                return weap
            else:
                raise ValueError("(Invalid input, please input the weapon  your weapon).")
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
def use_potion(potion):
    while True:
        potion = input("Type the potion you wish to use: ")
        if potion == "":
            retry_potion = valid_input("No such thing as a nothing potion. Do you wish to retry?")
            if retry_potion == True:
                continue
            else:
                break
        elif potion.lower() not in player_inventory:
            retry_potion = valid_input("Potion not in your inventory. Do you wish to use a potion? (Input yes or no): ")
            if retry_potion == True:
                continue
            else:
                break        
        elif potion.lower() == "health potion":
            if player_status["HP"] == 100:
                print("HP Full. cannot use potion.")
                break
            elif player_status["HP"] <= 99:
                player_status["HP"] += 20
                if player_status["HP"] > 100:
                    player_status["HP"] = 100
                    print(f"Successfully healed. {player_status}")
                if player_inventory["health potion"] == 1:
                    del player_inventory["health potion"]
                    break
                else:
                    player_inventory["health potion"] -= 1
                    break
        elif potion.lower()== "stamina potion":
            if player_status["Stamina"] == 100:
                print("Stamina Full. cannot use potion.")
                break
            elif player_status["Stamina"] <= 99:
                player_status["Stamina"] += 20
                if player_status["Stamina"] > 100:
                    player_status["Stamina"] = 100
                    print(f"Stamina successfully recovered. {player_status}")
                if player_inventory["stamina potion"] == 1:
                    del player_inventory["stamina potion"]
                    break
                elif "stamina potion" not in player_inventory:
                    print("You don't have any stamina potions.")
                    break
                else:
                    player_inventory["stamina potion"] -= 1
                    break
        elif potion.lower() == "mana potion":
            if player_status["Mana"] == 100:
                print("Mana Full. cannot use potion.")
                break
            elif player_status["Mana"] <= 99:
                player_status["Mana"] += 20
                if player_status["Mana"] > 100:
                    player_status["Mana"] = 100
                    print(f"Mana successfully recovered. {player_status}")
                if player_inventory["mana potion"] == 1:
                    del player_inventory["mana potion"]
                    break
                else:
                    player_inventory["mana potion"] -= 1
                    break

def use_weapon(useweap):
    while True:
        useweap = input("What weapon are you assigned? (pertains to the class you chose.): ")
        if useweap.lower() in str(player_weapon).lower():
            if useweap.lower() == "axe":
                player_status["Stamina"] -=15
                return 30
            elif useweap.lower() == "bow":
                player_inventory[str(player_weapon)] -= 1
                return 20
            elif useweap.lower() == "wand":
                player_status["Mana"] -= 20
                return 40
            else:
                print("No such weapon")
                continue
        else:
            print(f"You do not carry.. whatever {useweap} is ")
        



#def player_combat(playerturn, opponentturn):



player_name = input("What's your name?: ")
print(f"Good day to you adventurer. So your name is.. {player_name}")
playerdec1 = valid_input("Do you wish to play? (input Yes or No): ")
if playerdec1 == True:
    player_classchoice = valid_class("What class will you be in? (Mage, Archer or Barbarian): ")
    player_class[player_classchoice] = Class_Weapons.get(str(player_classchoice.lower()))
    player_inventory[Class_Weapons.get(str(player_classchoice))] = 100 
    player_weapon.append(Class_Weapons.get(str(player_classchoice).lower()))
    print(player_weapon)
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

print("You begin your adventure, towards the dark forest. . . .")

for i in range(3,0,-1):
    time.sleep(1)
    


print("You walk deep into the woods with only the light of the moon, filtered by the leaves, guiding your path.")
print("From a distance, you notice an Orc clad in chainmail armor, guarding what seems to be a chest of treasure.")

potopp = valid_input("Do you wish to use your potion?: ")
if potopp == True:
    use_potion("Type the name of the potion that you want to use.: ")
    print(player_inventory)
    
else:
    pass

escape1 = False
stscheck1 = valid_input("Do
you wish to engage in combat?: ")
if stscheck1 == True:
    checkstatus("Check your status before combat?: ")
    pass
elif stscheck1 == False:
    print("You attempt to leave without alerting the Orc. (mandatory dice roll)")
    droll1 = roll_the_dice("")
    if droll1 >= 7:
        print("You successfully leave the encounter.")
        escape1 = True

else:
    print("You attempt to leave, but due to your lack of wariness, you step on a twig.")
    print("The twig alerts the Orc. Leaving you no choice but to engage.")
    checkstatus("Check your status before combat?: ")
    escape1 = False




Orc1 = {"HP" : 50} #First enemy encounter status
if escape1 == True:
    pass
else:
    print("The Orc jumps towards you, landing succesfully in front of you.")
    print("The Orc swings its sword vertically, but you see this and you attempt to dodge.")
    droll2 = roll_the_dice("")
    if droll2 >= 6:
        print("You evaded the orc's attack. You brush yourself off and attempt to retaliate.")
        pass
    elif droll2 <= 5:
        print("The blade cuts deep into your shoulder, leaving a significantly large wound.")
        print("(You take 20 damage.)")
        player_status["HP"] -= 20
        print(player_status)
        pass
    displayInventory("")
if escape1 == True:
    pass
else: 
    playertrn1 = valid_input("Use your weapon to retaliate? (Weapon assigned by class. Input Yes or No.): ")
    if playertrn1 == True:
        print(player_weapon)
        weapdmg = use_weapon("")
        print(f"You use your {player_weapon} to attack the Orc.")
        for i in range(3,0,-1):
            time.sleep(1)
        Orc1["HP"] -= int(weapdmg)
        print("The Orc screams in pain as you blast its shoulder, successfully removing its right arm. ")
        print(Orc1)
        print(player_status)
        for i in range(2,0,-1):
            time.sleep(1)
        print("The Orc struggles to balance itself, but it still attempts to retaliate")

    

    else:
        escapeattempt2 = valid_input("Do you try to escape? (Yes or No): ")
        if escapeattempt2 == True:
            dice_roll()
        pass


    

