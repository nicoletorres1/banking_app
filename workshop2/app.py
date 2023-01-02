from banking_pkg.account import *
# import will work as long as root folder is the same


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")
print("REGISTRATION: ")
global name
name = input("Enter name to register: ")

# Makes sure pin that is registered is always 4 chars.
while True:
    global pin
    pin = (input("Enter Pin: "))

    if len(pin) < 4:
        print("Your pin must be 4 characters long")
        continue
    elif len(pin) > 4:
        print("Your pin must be 4 characters long")
        continue
    else:
        break


balance = 0  # using f string so we will not need to type convert

print(f"{name} has a balance of: {balance}")

# TASK 3 -- can you incorporate a TRY EXCEPT
print("          === Automated Teller Machine ===          ")
print("LOGIN: ")

while True:
    name_to_validate = input("Please enter your name: ")
    pin_to_validate = input("Please enter your pin: ")
    if (name_to_validate == name) and (pin_to_validate == pin):
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")
        continue  # figure out how to only give 3 tries to login

while True:
    user = name
    atm_menu(user)
    option = input("Choose an option: ")
    # Start of task 5
    if option == "1":
        show_balance(balance)  # not sure what argument to give this function
    elif option == "2":
        updated_balance = deposit(balance)
        balance = updated_balance
        show_balance(balance)  # not sure what argument to give this function
    elif option == "3":
        # updated_balance is just the variable that calls the withdraw func.
        updated_balance = withdraw(balance)
        balance = updated_balance
        show_balance(balance)  # not sure what argument to give this function
    elif option == "4":
        logout(name)
        break
    else:
        continue
