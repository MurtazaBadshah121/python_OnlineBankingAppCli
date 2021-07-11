# Project by: Murtaza Badshah
# Date: 06/10/2021

#--------Big Data Programming-------


# Define all the necessary variable for the system

account_number = []
account_balance = []


# Define a new method for creating a new account

def create_account():
    print("Let's create a new account, please read the following information carefully")

    acctno = input("Please enter a 5 digit account number: ")
    account_number.append(acctno)

    firstamt = str(input("Please enter amount of money you are depositing today: "))
    account_balance.append(firstamt)

    print("Congratulations! Your new account has been created!")
    print("==================================================")



    input("Press enter to view main menu...")


# define a new method for depositing money to a bank account

def deposit():
    i = 0
    while i < 1:

        position = -1
        cust_no = input("Please enter your 5 digit account number for verification: ")

        while position < len(account_number)-1:
            position += 1

            if cust_no == account_number[position]:
                i = i + 1

                print("Your current balance is:", end=" ")
                print("$" + account_balance[position], end=" ")
                print("\n")
                balance = int(account_balance[position])

                n = -1
                while n < 0:
                    try:
                        n = eval(input("Enter deposit amount: "))
                    except ValueError:
                        continue

                deposit = n
                balance = balance + deposit
                print("-\n")
                print("----Deposit Successful!----")
                account_balance[position] = str(balance)
                print("Your New Balance: ", balance, end=" ")
                print("$\n")

        if i < 1:
            print("Your account number does not match!\n")
            break

    input("Press enter to view main menu...")

# define a new method for viewing the current balance amount

def balance():
    i = 0
    while i < 1:

        position = -1
        cust_no = input("Please enter your 5 digit account number to view your balance: ")

        while position < len(account_number) - 1:
            position += 1

            if cust_no == account_number[position]:
                i = i + 1

                print("Your current balance is:", end=" ")
                print("$" + account_balance[position], end=" ")
                print("\n")

        if i < 1:
            print("Your account number does not match!\n")
            break

    input("Press enter to view main menu...")

# define a new method for withdrawing money from bank account

def withdraw():
    i = 0
    while i < 1:

        position = -1
        cust_no = input("Please enter your 5 digit account number for verification: ")

        while position < len(account_number)-1:
            position += 1

            if cust_no == account_number[position]:
                i = i + 1

                print("Your current balance is:", end=" ")
                print("$" + account_balance[position], end=" ")
                print("\n")
                balance = int(account_balance[position])

                n = -1
                while n < 0:
                    try:
                        n = eval(input("Enter withdrawal amount: "))
                    except ValueError:
                        continue
                withdraw = n

                if withdraw > balance:

                    print("Error! Not enough money to withdraw. Please deposit more cash!")

                else:


                    balance = balance - withdraw
                    print("-\n")
                    print("----Withdraw Successful!----")
                    account_balance[position] = str(balance)
                    print("Your New Balance: ", balance, end=" ")
                    print("$\n")

        if i < 1:
            print("Your account number does not match!\n")
            break

    input("Press enter to view main menu...")



# define method to exit the program once done.
def exit():
    print("Thank you for banking with us today! Hope you have a good day. Bye!")





# method to start up the banking application
def start():
    print("Welcome to the new online Badshah Banking System!")
    main = str.casefold(input("Are you a new user? Y or N: "))
    if main == "y":
        create_account()
    elif main == "n":
        i = 0
        while i < 1:

            position = -1
            cust_no = input("Please enter your 5 digit account number: ")

            while position < len(account_number) - 1:
                position += 1

                if cust_no == account_number[position]:
                    i = i + 1

                    print("Your current balance is:", end=" ")
                    print("$" + account_balance[position], end=" ")
                    print("\n")

            if i < 1:
                print("Your account number does not match!\n")
                start()

        input("Welcome to Badshah's bank please press enter to continue")

start()
while True:
    print("===========================================")
    print("--------Welcome to Badshah's Bank!---------")
    print("*******************************************")
    print("  Please read the instructions carefully.  ")
    print("*****   1. Create another account     *****")
    print("*****   2. Withdraw Money             *****")
    print("*****   3. Deposit Money              *****")
    print("*****   4. View Balance               *****")
    print("*****   5. Exit/Quit                  *****")
    print("*******************************************")

    selection = input("Please enter the appropriate number for the option: ")

    if selection == "1":
        create_account()
    elif selection == "2":
        withdraw()
    elif selection == "3":
        deposit()
    elif selection == "4":
        balance()
    elif selection == "5":
        exit()
        break
    else:
        print("Incorrect input please try again!")