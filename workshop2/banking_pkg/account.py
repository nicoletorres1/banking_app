# from app import name
# from banking_pkd.modulename
# fromo banking_pkd import functions
# from banking_pkd import app as newname
# from module import functions

# show_balance()
def show_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")


# deposit()
# use a try except
def deposit(balance):
    while True:
        try:
            # how to make user input with 2 decimal points
            amount = float(input("Enter amount to deposit: "))
            break  # break out of loop once converted correctly
        except:  # exception
            print("invalid amount!")
    return balance + amount


# withdraw()
def withdraw(balance):
    while True:
        try:
            # should have named the amount variable withdraw_amt
            amount = float(input("Enter amount to withdraw: "))
            # bonus task 3
            if amount > balance:
                print("Insufficient funds.")
                continue
            else:
                updated_amount = balance - amount
                break  # break out of loop once converted correctly
        except:  # exception
            print("invalid amount!")

    return updated_amount


# logout()
def logout(name):
    print(f"Goodbye, {name}!")


# Format string to have two decimals
# f-string: print(f"Your balance is: ${balance:.2f}"
# replace balance variable inside the {} with variable you need
