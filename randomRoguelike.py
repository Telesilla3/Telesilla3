def valid_input(TorF):
    value = input(TorF)
    try:
        int(value)
        if value.lower == "yes":
            return True
        if value.lower == "no":
            return False
    except ValueError:
        print("Invalid input, please try again.")
    

player_name = input("What's your name?: ")
print(f"Good day to you {player_name}")
playerdec1 = valid_input("Are you down to fight for good? (input Yes or No): ")
if playerdec1 == True:
    print(playerdec1) 
else:
    print("Alright. Then another shall take your place.")
    exit
