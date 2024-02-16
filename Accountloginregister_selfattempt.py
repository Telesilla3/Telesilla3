registered_account = ["Telesilla"]
acc_pw = {"Telesilla" : "123456"}

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

def register_account(accn):
    username1 = input(accn)
    if username1 not in registered_account:
        registered_account.append(username1)
        acc_pw[str(username1)] = ""
        return username1
    else:
        print("Account already in the system. Try again and log in.")
    

def register_password(regp):
    while True:  # Loop until a valid password is entered
        password1 = input(regp)
        if password1:  # Check if password1 is not empty
            password2 = input("Confirm your password: ")
            if password1 == password2:
                return password1  # Return the password if it's confirmed
            else:
                print("Passwords do not match. Please try again.")
        else:
            print("Blank is not a valid password. Please input something.")

        

def check_account(acc2):
    username1 = input(acc2)
    if username1 in acc_pw.keys():
        return username1
    else:
        print("Account not in the database. Please register account.")
        return False

def check_password(pwn):
    password1 = input(pwn)
    if password1 in acc_pw.values():
        return password1
    else:
        return password1 + " <3"

        
counter = 1
username_check = check_account("Good day. Please input your username: ")
while not username_check:
    print("Please try again.")
    print(acc_pw)
    Register_bool = valid_input("Do you want to register your account? (Please input Yes or No): ")
    if Register_bool:
        new_username = register_account("Please input your username: ")
        if new_username in registered_account:
            continue
        new_password = register_password("Please input your password twice: ")
        acc_pw[new_username] = new_password
        print("Successfully Registered. Please try and log in again.")
        print(acc_pw)
        print(registered_account)
        break 
    else:
        print("See you! Have a good day!")   
        break 


else:
    password_check = check_password("Please input your password: ")
    while username_check in acc_pw and acc_pw[username_check] != str(password_check) and counter <=5:
        print(f"Incorrect password. please try again. try no.{counter}")
        password_check = check_password("Please input your password: ")
        counter += 1
        if counter > 5:
            print("You reached the maximum amount of tries. Please register your account again.")
            symbol2_remove = "<3"
            username_removed = username_check.replace(symbol2_remove, "") 
            del acc_pw[username_removed]
            break
        if username_check in acc_pw and acc_pw[username_check] == str(password_check):
            break
    if username_check in acc_pw and acc_pw[username_check] == str(password_check):
        print("welcome back. " + username_check)



print(acc_pw)

    



    

        





    
