# Python Banking Program

def show_balance():
    pass


def deposite():
    pass


def withdraw():
    pass


balance = 0
is_running = True

while is_running:
    print("Banking Program")
    print("1. Show Balance")
    print("2. Deposite")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        show_balance()
    elif choice == '2':
        deposite()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the banking program!")






