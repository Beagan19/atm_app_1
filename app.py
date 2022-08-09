from banking_pkg.account import show_balance
from banking_pkg.account import deposit
from banking_pkg.account import withdraw
from banking_pkg.account import logout


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


# Login
while True:
    print("          === Automated Teller Machine ===          ")
    name = input("Enter name to register: ")
    name_length = len(name)
    if name_length > 10:
        print("Maximum name legth is 10 characters.")
        continue
    else:
        break
while True:
    pin = input("Enter PIN: ")
    pin_length = len(pin)
    if pin_length > 4:
        print("PIN must contain 4 numbers")
        continue
    else:
        break
balance = 0
print(name, "has been registered with a starting balance of $ " + str(balance))
while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    name_to_validate = input("Enter Name: ")
    pin_to_validate = input("Enter PIN: ")
    if name == name_to_validate and pin == pin_to_validate:
        print("Login successful!")
        break
    else:
        print("Invalid credentials")
        continue
while True:
    print("          === Automated Teller Machine ===          ")
    print("User: ", name)
    user = ""
    atm_menu(user)
    option = input("Choose an option: ")
    print("Current Balance:", balance)
    if option == "1":
        show_balance(balance)

    elif option == "2":
        total = deposit(balance)
        print("Current Balance:", total)
    elif option == "3":
        total = withdraw(balance)
        print("Current Balance:", total)
    elif option == "4":
        logout(balance)
        break
    balance = total
